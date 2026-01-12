// write a program to handle user registration(id, name, age, email)

import java.util.Scanner;

public class user {
    private static void getUserDetails(int id, String name, int age, String email, Scanner sc) throws Exception {
        System.err.println("Enter you id : ");
        id = sc.nextInt();
        if (id < 9999) {
            throw new Exception("Id should be at least 5 digit long!");
        }

        System.err.println("Enter you name : ");
        name = sc.next();
        if (name.contains("1234567890")) {
            throw new Exception("Name should not have numbers in it!\n");
        }

        System.out.println("Enter you email : ");
        email = sc.next();
        if (email == null || !email.toLowerCase().endsWith("@gmail.com")) {
            throw new Exception("Invalid Email, Try again!");
        }

        System.out.println("Enter your age : ");
        age = sc.nextInt();
        if (age < 18) {
            throw new IllegalArgumentException("Age should be greater than 18!\n");
        }

        System.out.println("Name\t\tEMAIL\t\tAGE\n");
        System.out.println(name + "\t\t" + email + "\t\t" + age + "\n");
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String name = new String();
        String email = new String();
        int id = 0, age = 0;

        try {
            getUserDetails(id, name, age, email, sc);

        } catch (Exception e) {
            System.err.println("Error : " + e);
        } finally {
            sc.close();
        }
    }
}
