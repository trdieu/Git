// BaseClass.java
// Lớp cơ sở với phương thức abstract print()
abstract class BaseClass {
    // Constructor của lớp cơ sở
    BaseClass() {
        // Gọi phương thức print() trong constructor của lớp cơ sở
        print();
    }

    // Phương thức abstract để các lớp dẫn xuất phải triển khai
    abstract void print();
}

// DerivedClass.java
// Lớp dẫn xuất ghi đè phương thức print()
class DerivedClass extends BaseClass {
    // Biến số nguyên trong lớp dẫn xuất
    int number = 10;

    // Ghi đè phương thức print() từ lớp cơ sở
    @Override
    void print() {
        System.out.println("Gia tri cua bien number la: " + number);
    }
}

// TestPrintMethod.java
// Lớp kiểm tra để tạo đối tượng của lớp dẫn xuất và gọi phương thức print()
public class TestPrintMethod {
    public static void main(String[] args) {
        // Tạo đối tượng của lớp dẫn xuất
        DerivedClass derived = new DerivedClass();

        // Gọi phương thức print() của lớp dẫn xuất
        derived.print();
    }
}