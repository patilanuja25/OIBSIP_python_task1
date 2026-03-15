
# 🧮 BMI Calculator – Python Internship Project

## 📌 Project Description
The **BMI Calculator** is a Python command-line application that calculates the **Body Mass Index (BMI)** using a user's weight and height.

The program determines the **BMI category** and provides a **health tip** based on the result. It also saves every calculation in a history file so users can view their previous BMI records.

---

## 👩‍💻 Intern Details
**Intern Name:** Anuja Patil  

---

## ⚙️ Features
- Accepts user information such as **Name, Age, Gender, Weight, and Height**
- Supports **height input in meters (m) or centimeters (cm)**
- Performs **input validation**
- Calculates BMI using the standard formula
- Displays **BMI category and health advice**
- Saves results to **bmi_history.txt**
- Option to **view full BMI history**
- Allows **multiple BMI calculations**

---

## 🧠 BMI Formula

BMI = Weight (kg) / Height² (m)

---

## 📂 Project Structure

```
BMI-Calculator/
│
├── bmi_cal.py        # Main Python program
├── bmi_history.txt   # Stores BMI records
└── README.md         # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Python
Make sure Python is installed.

Check using:

```
python --version
```

---

### 2️⃣ Run the Program

Navigate to the project folder and run:

```
python bmi_cal.py
```

---

### 3️⃣ Enter User Details

Example:

```
Enter your name: Anuja
Enter your age: 20
Enter your gender (male/female): female
Enter weight in kg: 55
Height unit (m/cm): cm
Enter height: 160
```

---

## 📊 BMI Categories

| BMI Range | Category |
|-----------|----------|
| Less than 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25 – 29.9 | Overweight |
| 30 and above | Obese |

---

## 📝 History Feature

Every calculation is saved in:

```
bmi_history.txt
```

Saved information includes:
- Date & Time
- Name
- Age
- Gender
- Weight
- Height
- BMI
- Category
- Health Tip

Users can also choose to **view the full history**.

---

## 🛠 Technologies Used
- Python
- File Handling
- Input Validation
- Datetime Module

---

## 📌 Conclusion
This project demonstrates Python programming concepts such as:
- User input handling
- Conditional statements
- Loops
- Functions
- File handling
- Error handling

It provides a simple and practical **health monitoring tool**.

---

⭐ Developed as part of a **Python Internship Project**
