// Lớp A với constructor có tham số
class A {
    A(int i) {
        System.out.println("Constructor của A với giá trị: " + i);
    }
}

// Lớp B với constructor có tham số
class B {
    B(String s) {
        System.out.println("Constructor của B với giá trị: " + s);
    }
}

// Lớp C kế thừa từ A và có một thành viên của B
class C extends A {
    B bMember; // Thành viên của lớp B

    // Constructor của C, gọi constructor của A và B
    C(int i, String s) {
        super(i);  // Gọi constructor của lớp A
        bMember = new B(s);  // Khởi tạo đối tượng của B
        System.out.println("Constructor của C");
    }

    public static void main(String[] args) {
        // Tạo đối tượng của lớp C và quan sát quá trình khởi tạo
        C obj = new C(5, "Xin chào");
    }
}
