// Lớp cơ sở chỉ có constructor không mặc định
class Base {
    Base(String message) {
        System.out.println("Constructor cua Base voi thong diep: " + message);
    }
}

// Lớp dẫn xuất với cả constructor không đối số và có tham số
class Derived extends Base {
    // Constructor không đối số
    Derived() {
        super("Thong diepp tu Derived (khong doi so)");
        System.out.println("Constructor khong doi so cua Derived");
    }

    // Constructor có tham số
    Derived(int number) {
        super("Thong diep tu Derived voi so: " + number);
        System.out.println("Constructor co tham so cua Derived voi so: " + number);
    }

    public static void main(String[] args) {
        // Tạo đối tượng của lớp Derived bằng constructor không đối số
        System.out.println("Tao doi tuong cua Derived bang constructor khong doi so:");
        Derived obj1 = new Derived();

        // Tạo đối tượng của lớp Derived bằng constructor có tham số
        System.out.println("\nTao doi tuong cua Derived bang constructor co tham so:");
        Derived obj2 = new Derived(42);
    }
}
