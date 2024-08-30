public class VarArgs {
    // Phương thức nhận tham số biến độ dài
    static void f(Object... x) {
        for (Object obj : x) {
            System.out.println(obj);
        }
    }

    public static void main(String[] args) {
        f(47, new VarArgs(), 3.14, 11.11);
        f("one", "two", "three");
        f(new A(), new A(), new A());
    }
}

class A {
    int i;
}
