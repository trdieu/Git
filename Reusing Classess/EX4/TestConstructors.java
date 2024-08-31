// Lớp cơ sở
class BaseClass {
    BaseClass() {
        System.out.println("BaseClass constructor");
    }
}

// Lớp dẫn xuất
class DerivedClass extends BaseClass {
    DerivedClass() {
        // Constructor của lớp cơ sở sẽ được gọi trước khi constructor của lớp dẫn xuất chạy
        System.out.println("DerivedClass constructor");
    }
}

public class TestConstructors {
    public static void main(String[] args) {
        System.out.println("Creating DerivedClass object:");
        DerivedClass derived = new DerivedClass(); // Khởi tạo đối tượng của lớp dẫn xuất
    }
}