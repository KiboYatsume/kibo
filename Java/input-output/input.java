import java.util.Scanner;
public class input {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("what is your name");
        String Name = scanner.nextLine();

        System.out.println("Hello," + Name);

        System.out.println("what is your age ?");

        int age = scanner.nextInt();

        if (age >= 18)
        {
            System.out.println(Name+" you are eligible to vote !");

        }
        else
        {
            System.out.println(Name+" you are eligible to vote !");
        }
        scanner.close();
    }
}