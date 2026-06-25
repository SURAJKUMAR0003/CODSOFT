public class Main {
    public static void main(String[] args) {
        // Create a sample bank account with initial balance of Rs. 25,000
        BankAccount account = new BankAccount("Rahul Sharma", "123456789012", 25000.00);

        // Create ATM and start session
        ATM atm = new ATM(account);
        atm.start();
    }
}
