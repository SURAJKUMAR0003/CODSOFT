import java.util.Random;
import java.util.Scanner;

public class NumberGame {
    static Scanner scanner = new Scanner(System.in);
    static Random random = new Random();

    public static void main(String[] args) {
        System.out.println("========================================");
        System.out.println("       WELCOME TO THE NUMBER GAME       ");
        System.out.println("========================================");

        int totalRounds = 0;
        int roundsWon = 0;

        while (true) {
            totalRounds++;
            boolean won = playRound(totalRounds);
            if (won) roundsWon++;

            System.out.print("\nDo you want to play again? (yes/no): ");
            String choice = scanner.nextLine().trim().toLowerCase();
            if (!choice.equals("yes") && !choice.equals("y")) {
                break;
            }
        }

        System.out.println("\n========================================");
        System.out.println("             FINAL SCORE               ");
        System.out.println("========================================");
        System.out.println("Total Rounds Played : " + totalRounds);
        System.out.println("Rounds Won          : " + roundsWon);
        System.out.println("Rounds Lost         : " + (totalRounds - roundsWon));
        System.out.printf("Win Rate            : %.1f%%\n", (roundsWon * 100.0 / totalRounds));
        System.out.println("========================================");
        System.out.println("Thanks for playing! Goodbye!");
    }

    static boolean playRound(int roundNumber) {
        int numberToGuess = random.nextInt(100) + 1; // 1 to 100
        int maxAttempts = 7;
        int attempts = 0;

        System.out.println("\n--- Round " + roundNumber + " ---");
        System.out.println("I have picked a number between 1 and 100.");
        System.out.println("You have " + maxAttempts + " attempts to guess it.");

        while (attempts < maxAttempts) {
            attempts++;
            System.out.print("\nAttempt " + attempts + "/" + maxAttempts + " - Enter your guess: ");

            int guess;
            try {
                guess = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input! Please enter a number between 1 and 100.");
                attempts--; // Don't count invalid input as attempt
                continue;
            }

            if (guess < 1 || guess > 100) {
                System.out.println("Please enter a number between 1 and 100.");
                attempts--;
                continue;
            }

            if (guess == numberToGuess) {
                System.out.println("\n🎉 CORRECT! You guessed the number " + numberToGuess + "!");
                System.out.println("You won this round in " + attempts + " attempt(s)!");
                int score = calculateScore(attempts, maxAttempts);
                System.out.println("Score for this round: " + score + " points");
                return true;
            } else if (guess < numberToGuess) {
                System.out.println("Too LOW! Try a higher number.");
            } else {
                System.out.println("Too HIGH! Try a lower number.");
            }

            System.out.println("Remaining attempts: " + (maxAttempts - attempts));
        }

        System.out.println("\n❌ You've used all " + maxAttempts + " attempts!");
        System.out.println("The correct number was: " + numberToGuess);
        return false;
    }

    static int calculateScore(int attempts, int maxAttempts) {
        return (maxAttempts - attempts + 1) * 10;
    }
}
