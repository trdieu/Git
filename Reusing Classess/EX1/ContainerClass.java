// Define the first class
class SimpleClass {
    private String message;

    // Constructor for SimpleClass
    public SimpleClass() {
        System.out.println("SimpleClass Constructor Called");
        message = "Hello from SimpleClass!";
    }

    // Method to return message
    public String getMessage() {
        return message;
    }
}

// Define the second class that uses lazy initialization
public class ContainerClass {
    private SimpleClass simpleObject; // Reference to SimpleClass

    // Method to get SimpleClass object, with lazy initialization
    public SimpleClass getSimpleObject() {
        if (simpleObject == null) {
            simpleObject = new SimpleClass(); // Instantiate when needed
        }
        return simpleObject;
    }

    // Method to print message from SimpleClass object
    public void printMessage() {
        System.out.println(getSimpleObject().getMessage());
    }

    // Main method to run the program
    public static void main(String[] args) {
        ContainerClass container = new ContainerClass();
        container.printMessage(); // This will trigger lazy initialization
    }
}
