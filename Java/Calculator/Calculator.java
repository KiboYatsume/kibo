package Java.Calculator;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        double num1, num2;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter The Number");

        num1 = sc.nextDouble();
        num2 = sc.nextDouble();

        System.out.println("Enter the operators (+,-,/,*):");
        char op = sc.next().charAt(0);
        double result = 0;

        switch (op) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;              
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            default:
                System.out.println("You Entered Wrong Input!");
        }

        System.out.println("The final result:");
        System.out.println(num1 + " " + op + " " + num2 + " = " + result);

        // Close the scanner to prevent resource leak
        sc.close();
    }
}
