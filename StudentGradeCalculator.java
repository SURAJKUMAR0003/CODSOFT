import java.util.Scanner;

public class StudentGradeCalculator {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("     STUDENT GRADE CALCULATOR          ");
        System.out.println("========================================");

        while (true) {
            calculateGrade();

            System.out.print("\nCalculate for another student? (yes/no): ");
            String choice = scanner.nextLine().trim().toLowerCase();
            if (!choice.equals("yes") && !choice.equals("y")) {
                break;
            }
        }

        System.out.println("\nThank you for using Student Grade Calculator!");
    }

    static void calculateGrade() {
        System.out.print("\nEnter Student Name: ");
        String name = scanner.nextLine().trim();

        System.out.print("Enter number of subjects: ");
        int numSubjects;
        try {
            numSubjects = Integer.parseInt(scanner.nextLine().trim());
            if (numSubjects <= 0) {
                System.out.println("Number of subjects must be greater than 0.");
                return;
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input! Please enter a valid number.");
            return;
        }

        String[] subjectNames = new String[numSubjects];
        double[] marks = new double[numSubjects];
        double totalMarks = 0;

        System.out.println("\nEnter marks for each subject (out of 100):");
        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Subject " + (i + 1) + " name: ");
            subjectNames[i] = scanner.nextLine().trim();

            while (true) {
                System.out.print("Marks obtained in " + subjectNames[i] + ": ");
                try {
                    marks[i] = Double.parseDouble(scanner.nextLine().trim());
                    if (marks[i] < 0 || marks[i] > 100) {
                        System.out.println("Marks must be between 0 and 100. Try again.");
                    } else {
                        totalMarks += marks[i];
                        break;
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Invalid input! Please enter a valid number.");
                }
            }
        }

        double averagePercentage = totalMarks / numSubjects;
        String grade = calculateGradeFromPercentage(averagePercentage);
        String remarks = getRemarks(grade);

        // Display Results
        System.out.println("\n========================================");
        System.out.println("           RESULT CARD                  ");
        System.out.println("========================================");
        System.out.printf("Student Name        : %s%n", name);
        System.out.println("----------------------------------------");
        System.out.printf("%-20s %-10s%n", "Subject", "Marks");
        System.out.println("----------------------------------------");
        for (int i = 0; i < numSubjects; i++) {
            System.out.printf("%-20s %.2f%n", subjectNames[i], marks[i]);
        }
        System.out.println("----------------------------------------");
        System.out.printf("Total Marks         : %.2f / %d%n", totalMarks, numSubjects * 100);
        System.out.printf("Average Percentage  : %.2f%%%n", averagePercentage);
        System.out.printf("Grade               : %s%n", grade);
        System.out.printf("Remarks             : %s%n", remarks);
        System.out.println("========================================");
    }

    static String calculateGradeFromPercentage(double percentage) {
        if (percentage >= 90) return "A+";
        else if (percentage >= 80) return "A";
        else if (percentage >= 70) return "B";
        else if (percentage >= 60) return "C";
        else if (percentage >= 50) return "D";
        else return "F";
    }

    static String getRemarks(String grade) {
        switch (grade) {
            case "A+": return "Outstanding!";
            case "A":  return "Excellent!";
            case "B":  return "Very Good!";
            case "C":  return "Good";
            case "D":  return "Average - Needs Improvement";
            case "F":  return "Fail - Please Work Harder";
            default:   return "N/A";
        }
    }
}
