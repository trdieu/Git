// AbstractWithoutAbstractMethods.java
// Lớp abstract không chứa phương thức abstract
abstract class AbstractWithoutAbstractMethods {
    // Phương thức cụ thể
    public void showMessage() {
        System.out.println("Đây là một phương thức cụ thể trong lớp abstract.");
    }
}

// Lớp kiểm tra khởi tạo lớp abstract
public class TestAbstractInstantiation {
    public static void main(String[] args) {
        // Cố gắng khởi tạo lớp abstract
        // Dòng lệnh này sẽ gây lỗi biên dịch
        // AbstractWithoutAbstractMethods obj = new AbstractWithoutAbstractMethods();

        // Nếu dòng lệnh trên bị chú thích, bạn có thể gọi phương thức nếu việc khởi tạo là hợp lệ
        // AbstractWithoutAbstractMethods obj = new ConcreteClass(); // Đây là ví dụ cho lớp con cụ thể
        // obj.showMessage();
    }
}
