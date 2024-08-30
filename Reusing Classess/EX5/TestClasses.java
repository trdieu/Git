// Lớp A với constructor mặc định
class A {
    A() {
        System.out.println("Constructor of class A");
    }
}

// Lớp B với constructor mặc định
class B {
    B() {
        System.out.println("Constructor of class B");
    }
}

// Lớp C kế thừa từ lớp A và chứa một thành viên của lớp B
class C extends A {
    B b = new B(); // Tạo đối tượng của lớp B bên trong lớp C
}

public class TestClasses {
    public static void main(String[] args) {
        System.out.println("Creating object of class C:");
        C c = new C(); // Khởi tạo đối tượng của lớp C
    }
}
