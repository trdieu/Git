// Define the class
public class Dog {

    // No argument bark method
    public void bark() {
        System.out.println("Woof!");
    }

    // Overloaded bark method for int argument
    public void bark(int times) {
        System.out.println("Woof! Woof! Woof! (repeated " + times + " times)");
    }

    // Overloaded bark method for double argument
    public void bark(double volume) {
        System.out.println("Woof! (volume: " + volume + " decibels)");
    }

    // Overloaded bark method for boolean argument
    public void bark(boolean isHappy) {
        if (isHappy) {
            System.out.println("Woof! Woof! (I'm happy!)");
        } else {
            System.out.println("Woof! (I'm not happy...)");
        }
    }

    // Overloaded bark method for char argument
    public void bark(char type) {
        if (type == 'H') {
            System.out.println("Howl!");
        } else if (type == 'B') {
            System.out.println("Bark!");
        } else {
            System.out.println("Unknown sound!");
        }
    }

    // Overloaded bark method for int and double arguments (reversed order)
    public void bark(double volume, int times) {
        System.out.println("Woof! (volume: " + volume + " decibels, repeated " + times + " times)");
    }

    // Overloaded bark method for double and int arguments (reversed order)
    public void bark(int times, double volume) {
        System.out.println("Woof! Woof! Woof! (repeated " + times + " times with volume: " + volume + " decibels)");
    }

    // Main method to run the program
    public static void main(String[] args) {
        // Create an object of Dog
        Dog myDog = new Dog();

        // Call each overloaded version of bark()
        myDog.bark();                     // No arguments
        myDog.bark(3);                    // int argument
        myDog.bark(85.5);                 // double argument
        myDog.bark(true);                // boolean argument
        myDog.bark('H');                  // char argument
        myDog.bark(90.0, 5);              // double and int arguments (reversed order)
        myDog.bark(4, 70.0);              // int and double arguments (reversed order)
    }
}