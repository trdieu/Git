// Lớp cơ sở
class BaseClass {
    BaseClass() {
        System.out.println("BaseClass constructor");
    }
}

// Lớp dẫn xuất
class DerivedClass extends BaseClass {
    DerivedClass() {
        // Lớp cơ sở sẽ được tự động khởi tạo trước
        System.out.println("DerivedClass constructor");
    }
}

public class TestInheritance {
    public static void main(String[] args) {
        System.out.println("Creating DerivedClass object:");
        DerivedClass derived = new DerivedClass(); // Khởi tạo đối tượng của lớp dẫn xuất
    }
}