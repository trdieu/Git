// Main.java
// Lớp cơ sở trừu tượng không có phương thức
abstract class AbstractBaseClass {
    // Không có phương thức trong lớp cơ sở
}

// Lớp dẫn xuất với một phương thức
class DerivedClass extends AbstractBaseClass {
    void display() {
        System.out.println("Phuong thuc display() duoc goi tu lop dan xuat.");
    }
}

// Lớp chứa phương thức tĩnh để thực hiện downcast và gọi phương thức
class Util {
    static void callDisplay(AbstractBaseClass base) {
        // Downcast từ AbstractBaseClass sang DerivedClass và gọi phương thức display()
        if (base instanceof DerivedClass) {
            DerivedClass derived = (DerivedClass) base;
            derived.display();
        } else {
            System.out.println("Khong the downcast thanh DerivedClass.");
        }
    }
}

// Lớp cơ sở trừu tượng với phương thức abstract
abstract class AbstractBaseClassWithMethod {
    // Phương thức abstract phải được triển khai trong lớp dẫn xuất
    abstract void display();
}

// Lớp dẫn xuất với việc triển khai phương thức display()
class DerivedClassWithAbstractMethod extends AbstractBaseClassWithMethod {
    @Override
    void display() {
        System.out.println("Phuong thuc display() duoc goi tu lop dan xuat.");
    }
}

// Lớp kiểm tra để tạo đối tượng và gọi phương thức static
public class Main {
    public static void main(String[] args) {
        // Test 1: Downcast và gọi phương thức display()
        System.out.println("Test 1:");
        AbstractBaseClass obj1 = new DerivedClass();
        Util.callDisplay(obj1);
        
        // Test 2: Gọi phương thức display() trực tiếp mà không cần downcast
        System.out.println("\nTest 2:");
        AbstractBaseClassWithMethod obj2 = new DerivedClassWithAbstractMethod();
        obj2.display();
    }
}
