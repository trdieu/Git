class Cycle {
    public void ride() {
        System.out.println("Riding a cycle");
    }
}

// Lớp dẫn xuất Unicycle
class Unicycle extends Cycle {
    @Override
    public void ride() {
        System.out.println("Riding a unicycle");
    }
}

// Lớp dẫn xuất Bicycle
class Bicycle extends Cycle {
    @Override
    public void ride() {
        System.out.println("Riding a bicycle");
    }
}

// Lớp dẫn xuất Tricycle
class Tricycle extends Cycle {
    @Override
    public void ride() {
        System.out.println("Riding a tricycle");
    }
}

// Lớp chính để kiểm tra
public class TestCycles {
    public static void main(String[] args) {
        // Tạo các đối tượng của từng lớp
        Cycle myCycle = new Cycle();
        Cycle myUnicycle = new Unicycle(); // Upcast
        Cycle myBicycle = new Bicycle();   // Upcast
        Cycle myTricycle = new Tricycle(); // Upcast

        // Gọi phương thức ride() từ từng đối tượng
        myCycle.ride();     // Output: Riding a cycle
        myUnicycle.ride();  // Output: Riding a unicycle
        myBicycle.ride();   // Output: Riding a bicycle
        myTricycle.ride();  // Output: Riding a tricycle
    }
}