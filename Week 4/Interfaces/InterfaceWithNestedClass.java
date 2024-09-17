// InterfaceWithNestedClass.java

// Interface với lớp lồng nhau
public interface InterfaceWithNestedClass {
    // Phương thức của interface
    void displayMessage();

    // Lớp lồng nhau với phương thức tĩnh
    class Nested {
        // Phương thức tĩnh gọi phương thức của interface
        public static void callInterfaceMethod(InterfaceWithNestedClass obj) {
            obj.displayMessage(); // Gọi phương thức của interface
        }
    }
}
