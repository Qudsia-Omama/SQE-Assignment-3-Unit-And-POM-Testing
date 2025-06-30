#  SQE Assignment 3 – Selenium Testing using Python & Page Object Model

This repository contains the complete solution to **Assignment #3** of **SWE–305: Software Quality Engineering**, submitted by **Qudsia Omama (2022F-BSE-002)**.

The assignment implements:
1. Selenium-based Unit Testing
2. Page Object Model (POM) structure
using Python on UI forms provided by **TutorialsPoint Practice Site**.

---

## 📌 Assignment Tasks

### 🔹 Question 1: Selenium Unit Testing
**Target Page:**  
👉 [Student Registration Form](https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php)

**Test Objective:**
- Validate registration form fields
- Automate input of name, email, gender, profession, tools, etc.
- Assert correct form behavior on submission
- Capture output results (screenshots)

---

### 🔹 Question 2: Page Object Model (POM)
**Target Pages:**
- 🔐 [Login Page](https://www.tutorialspoint.com/selenium/practice/login.php)
- 📝 [Text Box Page](https://www.tutorialspoint.com/selenium/practice/register.php)

**POM Design:**
- Created separate page classes for login and registration
- Test scripts handle positive/negative form submissions
- Validates field-level input, button clicks, and success/error messages

---

## 🧰 Technologies Used

| Technology        | Purpose                           |
|-------------------|-----------------------------------|
| Python            | Programming Language              |
| Selenium WebDriver| Browser Automation                |
| ChromeDriver      | Automates Chrome Browser          |
| unittest          | Python Testing Framework          |
| POM Classes       | Encapsulation of UI interactions  |

---

## 🗂️ Folder Structure

```

SQE-Assignment-3/
├── Pages/
│   ├── loginPage.py             # Login page POM class
│   └── registrationPage.py      # Registration page POM class
│
├── Tests/
│   ├── login.py                 # Login test using POM
│   ├── registration.py          # Registration form test using POM
│   └── studentRegistrationTest.py  # Unit test on automation practice form
│
├── screenshots/                 # Output images (optional)
├── SQE-ASSIGNMENT-3.docx        # Report with screenshots
└── README.md                    # This file

````

Each script opens a Chrome browser, interacts with the target form, and prints success/error messages in the terminal.

---

## 📸 Sample Output

Included in the assignment report (`.docx`) are:

* ✅ Success message screenshots
* ❌ Validation errors for missing or invalid inputs
* ⚠️ Page redirects and output confirmations

---

## 👩‍🎓 Student Information

| Name         | Roll Number   | Section |
| ------------ | ------------- | ------- |
| Qudsia Omama | 2022F-BSE-002 | B       |

* **University**: Sir Syed University Of Engineering & Technology
* **Program**: BS Software Engineering
* **Course**: SWE–305 – Software Quality Engineering
* **Instructor**: Miss Aiman Qasim
* **Date Submitted**: July 1, 2025

---

This assignment demonstrates the ability to:

* Write modular Selenium test scripts
* Implement the Page Object Model (POM) in Python
* Validate UI elements and automate real-world form behavior

These testing techniques contribute to better software reliability, maintainability, and robustness during development.

