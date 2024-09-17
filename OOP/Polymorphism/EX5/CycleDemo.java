// Lớp cơ sở Cycle
class Cycle {
    // Phương thức để trả về số bánh xe
    public int wheels() {
        return 0; // Mặc định trả về 0
    }

    // Phương thức ride sử dụng wheels()
    public void ride() {
        System.out.println("Cycle with " + wheels() + " wheels is being ridden.");
    }
}

// Lớp dẫn xuất Unicycle
class Unicycle extends Cycle {
    @Override
    public int wheels() {
        return 1; // Unicycle có 1 bánh xe
    }
}

// Lớp dẫn xuất Bicycle
class Bicycle extends Cycle {
    @Override
    public int wheels() {
        return 2; // Bicycle có 2 bánh xe
    }
}

// Lớp dẫn xuất Tricycle
class Tricycle extends Cycle {
    @Override
    public int wheels() {
        return 3; // Tricycle có 3 bánh xe
    }
}

// Lớp chính để kiểm tra polymorphism
public class CycleDemo {
    public static void main(String[] args) {
        Cycle[] cycles = { new Unicycle(), new Bicycle(), new Tricycle() };

        for (Cycle cycle : cycles) {
            cycle.ride(); // Gọi phương thức ride() sẽ gọi wheels() tương ứng
        }
    }
}