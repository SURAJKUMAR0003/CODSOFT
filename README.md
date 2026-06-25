# CODSOFT Java Development Internship Tasks

This repository contains Java programs developed as part of the **CodSoft Java Development Internship**.

---

## 📁 Repository Structure

```
CODSOFT/
├── Task1_NumberGame/
│   └── NumberGame.java
├── Task2_StudentGradeCalculator/
│   └── StudentGradeCalculator.java
├── Task3_ATMInterface/
│   ├── BankAccount.java
│   ├── ATM.java
│   └── Main.java
└── README.md
```

---

## ✅ Task 1 — Number Guessing Game

### Features:
- Generates a random number between 1 and 100
- User has **7 attempts** to guess the number
- Feedback given: Too High / Too Low / Correct
- **Multiple rounds** with play again option
- **Score system** based on attempts taken
- Win rate displayed at the end

### How to Run:
```bash
cd Task1_NumberGame
javac NumberGame.java
java NumberGame
```

---

## ✅ Task 2 — Student Grade Calculator

### Features:
- Enter any number of subjects with their names
- Calculates **Total Marks** and **Average Percentage**
- Assigns **Grade** (A+, A, B, C, D, F) based on percentage
- Displays a formatted **Result Card**
- Supports multiple students in one session

### Grade Table:
| Percentage | Grade | Remarks              |
|------------|-------|----------------------|
| 90 - 100   | A+    | Outstanding!         |
| 80 - 89    | A     | Excellent!           |
| 70 - 79    | B     | Very Good!           |
| 60 - 69    | C     | Good                 |
| 50 - 59    | D     | Needs Improvement    |
| Below 50   | F     | Fail                 |

### How to Run:
```bash
cd Task2_StudentGradeCalculator
javac StudentGradeCalculator.java
java StudentGradeCalculator
```

---

## ✅ Task 3 — ATM Interface

### Features:
- PIN authentication (default PIN: `1234`) with 3 attempts
- **Check Balance**
- **Deposit** money (max Rs. 1,00,000 per transaction)
- **Withdraw** money (max Rs. 50,000 per transaction)
- Input validation for insufficient funds
- Masked account number display for security

### How to Run:
```bash
cd Task3_ATMInterface
javac BankAccount.java ATM.java Main.java
java Main
```

---

## 🛠 Technologies Used
- **Language:** Java (JDK 8+)
- **IDE:** Any (VS Code / IntelliJ IDEA / Eclipse / Notepad++)
- **Build:** Manual `javac` compilation

---

## 👤 Author
- **Internship:** CodSoft Java Development Internship
- **LinkedIn:** [Your LinkedIn Profile]
- **GitHub:** [Your GitHub Profile]

---

*#codsoft #internship #java #javadevelopment*
