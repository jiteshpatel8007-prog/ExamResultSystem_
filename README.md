# 🎓 Exam Result Management System

A simple web-based **Exam Result Management System** developed using Python and Flask. This project helps manage student records, calculate examination results, and generate student rankings.

---

## 📌 Project Description

The Exam Result Management System is designed to simplify the process of managing student examination records.

It allows users to add student details, enter subject marks, view records, update information, and delete student records.

The system automatically calculates total marks, percentage, pass/fail status, and displays a rank list based on student performance.

This project demonstrates the practical implementation of Python programming, web development, and database management.

---

## ✨ Features

- **Add Student:** Add new student details and examination marks.
- **View Records:** Display all registered student records.
- **Edit Student:** Update existing student details and marks.
- **Delete Student:** Remove student records with confirmation.
- **Dashboard Statistics:** Display total students, passed students, failed students, and average percentage.
- **Automatic Result Calculation:** Calculate total marks and percentage automatically.
- **Pass/Fail Status:** Determine results based on subject-wise marks.
- **Rank List:** Display students according to their total marks.
- **Search Student:** Search student records using name or roll number.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| SQLite | Database Management |
| Pandas | Data Processing |
| HTML5 | Frontend Structure |
| CSS3 | Styling and Design |
| Jinja2 | Dynamic HTML Templates |

---

## 📂 Project Structure

```text
ExamResultSystem_v2/
│
├── app.py
├── database.py
├── results.db
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── base.html
    ├── index.html
    ├── add.html
    ├── view.html
    ├── edit.html
    └── rank.html
```

---

## ⚙️ Installation Instructions

Follow these steps to run the project on your computer.

### Step 1: Clone the Repository

```bash
git clone https://github.com/jiteshpatel8007-prog/ExamResultSystem_.git
```

### Step 2: Open Project Folder

```bash
cd ExamResultSystem_
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Visit the following address:

```text
http://127.0.0.1:5000
```

The Exam Result Management System is now ready to use.

---

## 📊 Result Calculation

The system uses the following formulas:

**Total Marks**

```text
Total = Maths + Physics + Chemistry
```

**Percentage**

```text
Percentage = (Total Marks / 300) × 100
```

**Result Criteria**

- Pass: Minimum 40 marks in each subject.
- Fail: Less than 40 marks in any subject.

---

## 💾 Database Information

The project uses SQLite to store student examination records.

**Database Table:** `students`

| Field | Data Type |
|---|---|
| roll | TEXT (Primary Key) |
| name | TEXT |
| maths | INTEGER |
| physics | INTEGER |
| chemistry | INTEGER |

---

## 🎯 Project Objective

The main objective of this project is to reduce manual work in examination result management and make student record handling easier, faster, and more accurate.

---

## 👨‍💻 Developer

**Jitesh Patel**

B.Tech – Computer Science Engineering

Rungta International Skills University

---

## 📜 License

This project is developed for educational and academic purposes.

---

⭐ If you find this project useful, feel free to explore the repository!