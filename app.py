
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd

from database import (
    init_db,
    add_student,
    get_all_students,
    get_ranked_students,
    get_student_by_roll,
    update_student,
    delete_student
)

app = Flask(__name__)
app.secret_key = "ibm_exam_system_secret"

init_db()


def process_dataframe(df):
    """Total, Percentage, Result calculate karta hai"""

    if df.empty:
        return df

    df['total'] = df['maths'] + df['physics'] + df['chemistry']
    df['percentage'] = (df['total'] / 300) * 100

    df['result'] = df.apply(
        lambda row: 'Pass'
        if (
            row['maths'] >= 40
            and row['physics'] >= 40
            and row['chemistry'] >= 40
        )
        else 'Fail',
        axis=1
    )

    return df


# ==================== HOME PAGE ====================

@app.route('/')
def index():

    df = process_dataframe(get_all_students())

    total_students = len(df)

    if not df.empty:
        passed_students = int((df['result'] == 'Pass').sum())
        failed_students = int((df['result'] == 'Fail').sum())
        average_percentage = round(df['percentage'].mean(), 2)
    else:
        passed_students = 0
        failed_students = 0
        average_percentage = 0

    return render_template(
        'index.html',
        total_students=total_students,
        passed_students=passed_students,
        failed_students=failed_students,
        average_percentage=average_percentage
    )


# ==================== ADD PAGE ====================

@app.route('/add', methods=['GET'])
def add_page():

    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add():

    roll = request.form.get('roll', '').strip()
    name = request.form.get('name', '').strip()

    if not roll or not name:
        flash("Roll number and Name cannot be empty.", "error")
        return redirect(url_for('add_page'))

    try:
        maths = int(request.form.get('maths'))
        physics = int(request.form.get('physics'))
        chemistry = int(request.form.get('chemistry'))

    except (ValueError, TypeError):
        flash("Marks must be valid integers.", "error")
        return redirect(url_for('add_page'))

    if not (
        0 <= maths <= 100
        and 0 <= physics <= 100
        and 0 <= chemistry <= 100
    ):
        flash("Marks must be between 0 and 100.", "error")
        return redirect(url_for('add_page'))

    success, message = add_student(
        roll, name, maths, physics, chemistry
    )

    if not success:
        flash(message, "error")
        return redirect(url_for('add_page'))

    total = maths + physics + chemistry
    percentage = total / 3.0

    result = (
        "Pass"
        if maths >= 40 and physics >= 40 and chemistry >= 40
        else "Fail"
    )

    flash(
        f"Record added: {roll} | {name} | "
        f"Total: {total} | Percentage: {percentage:.2f}% | "
        f"Result: {result}",
        "success"
    )

    return redirect(url_for('add_page'))


# ==================== EDIT STUDENT PAGE ====================

@app.route('/edit/<roll>', methods=['GET', 'POST'])
def edit(roll):

    student = get_student_by_roll(roll)

    if student is None:
        flash("Student record not found.", "error")
        return redirect(url_for('view'))

    if request.method == 'POST':

        name = request.form.get('name', '').strip()

        if not name:
            flash("Student name cannot be empty.", "error")
            return redirect(url_for('edit', roll=roll))

        try:
            maths = int(request.form.get('maths'))
            physics = int(request.form.get('physics'))
            chemistry = int(request.form.get('chemistry'))

        except (ValueError, TypeError):
            flash("Marks must be valid integers.", "error")
            return redirect(url_for('edit', roll=roll))

        if not all(
            0 <= mark <= 100
            for mark in [maths, physics, chemistry]
        ):
            flash("Marks must be between 0 and 100.", "error")
            return redirect(url_for('edit', roll=roll))

        update_student(
            roll, name, maths, physics, chemistry
        )

        flash("Student record updated successfully!", "success")

        return redirect(url_for('view'))

    return render_template('edit.html', student=student)


# ==================== DELETE STUDENT ====================

@app.route('/delete/<roll>', methods=['POST'])
def delete(roll):

    success = delete_student(roll)

    if success:
        flash("Student record deleted successfully!", "success")
    else:
        flash("Student record not found.", "error")

    return redirect(url_for('view'))


# ==================== VIEW PAGE WITH SEARCH ====================

@app.route('/view')
def view():

    search_query = request.args.get('search', '').strip()

    df = get_all_students()
    df = process_dataframe(df)

    if not df.empty and search_query:
        search_lower = search_query.lower()

        df = df[
            df['name'].astype(str).str.lower().str.contains(
                search_lower, na=False
            )
            |
            df['roll'].astype(str).str.lower().str.contains(
                search_lower, na=False
            )
        ]

    records = df.to_dict('records') if not df.empty else []

    return render_template(
        'view.html',
        records=records,
        search_query=search_query
    )


# ==================== RANK PAGE ====================

@app.route('/rank')
def rank():

    df = get_ranked_students()
    df = process_dataframe(df)

    records = df.to_dict('records') if not df.empty else []

    return render_template('rank.html', records=records)


# ==================== RUN APPLICATION ====================

if __name__ == '__main__':
    app.run(debug=True)
