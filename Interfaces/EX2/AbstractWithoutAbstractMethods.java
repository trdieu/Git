// ConcreteClass.java
class ConcreteClass extends AbstractWithoutAbstractMethods {
    // Không cần phải triển khai thêm gì, vì không có phương thức abstract nào cần triển khai
}

// Cập nhật lớp kiểm tra để sử dụng lớp cụ thể
public class AbstractWithoutAbstractMethods {
    public static void main(String[] args) {
        // Khởi tạo lớp cụ thể
        AbstractWithoutAbstractMethods obj = new ConcreteClass();
        obj.showMessage(); // Gọi phương thức cụ thể
    }
}