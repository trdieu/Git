// Define the class
public class MyClass {

    // Default constructor
    public MyClass() {
        // Print a message when an object is created
        System.out.println("Object of MyClass created!");
    }

    // Overloaded constructor with a String argument
    public MyClass(String message) {
        // Print the message along with the default message
        System.out.println("Object of MyClass created with message: " + message);
    }

    // Main method to run the program
    public static void main(String[] args) {
        // Create an object of MyClass using the default constructor
        MyClass obj1 = new MyClass();

        // Create an object of MyClass using the overloaded constructor
        MyClass obj2 = new MyClass("Hello, World!");
    }
}