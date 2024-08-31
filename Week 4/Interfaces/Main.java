// Main.java

// Lớp triển khai interface
class Implementation implements InterfaceWithNestedClass {
    @Override
    public void displayMessage() {
        System.out.println("Hello from the implemented interface!");
    }
}

// Lớp Main để chạy chương trình
public class Main {
    public static void main(String[] args) {
        // Tạo thể hiện của lớp triển khai
        Implementation impl = new Implementation();

        // Gọi phương thức tĩnh của lớp lồng nhau
        InterfaceWithNestedClass.Nested.callInterfaceMethod(impl);
    }
}
