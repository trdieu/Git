// ProtectedDataExample.java
class FirstClass {
    protected int protectedData = 100;

    public void displayData() {
        System.out.println("Protected data: " + protectedData);
    }
}

class SecondClass {
    public void manipulateProtectedData(FirstClass firstClass) {
        firstClass.protectedData += 50; // Thao tác với dữ liệu protected
        System.out.println("After manipulation: " + firstClass.protectedData);
    }
}

public class ProtectedDataExample {
    public static void main(String[] args) {
        FirstClass first = new FirstClass();
        SecondClass second = new SecondClass();

        // Hiển thị dữ liệu trước khi thao tác
        first.displayData();

        // Thao tác với dữ liệu protected
        second.manipulateProtectedData(first);

        // Hiển thị dữ liệu sau khi thao tác
        first.displayData();
    }
}
