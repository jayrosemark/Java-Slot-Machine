import java.util.Scanner;
public class MyProgram
{
    public static void main(String[] args)
    { 
        Scanner reader = new Scanner(System.in);
        // Variables //
        int m = 0;
        String jay = "y";
        int n1 = 0;
        int n2 = 0;
        int n3 = 0;
        // Code //
        System.out.print("Enter Starting amount: ");
        m = reader.nextInt();
        reader.nextLine(); // Consume the newline character after the number input
        
        while (m > 0 && jay.equals("y"))
        {
            n1 = (int)(Math.random() * 9) + 1;
            n2 = (int)(Math.random() * 9) + 1;
            n3 = (int)(Math.random() * 9) + 1;
            System.out.print("Roll is: " + n1 + " ");
            System.out.print(n2 + " ");
            System.out.println(n3 + " ");
            m--;
            if (n1 == n2 && n2 == n3)
            {
                System.out.println("Jackpot! You won $" + (n1 * 20));
                m = m + (n1 * 20);
            }
            else if (n1 == n2 || n1 == n3)
            {
                System.out.println("Mini Jackpot! You won $" + n1);
                m = m + n1;
            }
            else if (n2 == n3)
            {
                System.out.println("Mini Jackpot! You won $" + n2);
                m = m + n2;
            }
            System.out.println("You are currently at $" + m);
            if (m > 0)
            {
                System.out.print("Enter y to keep playing and n to stop: ");
                jay = reader.nextLine();
            }
            else
            {
                jay = "n";
            }
            System.out.println(" ");
        }
        if (m > 0)
            System.out.println("You left with $" + m);
        else
            System.out.println("You went Bankrupt!");
    }
}
