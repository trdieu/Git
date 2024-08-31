package example;

// Tạo interface với các phương thức không khai báo public
interface ExampleInterface {
    void method1(); // Tự động là public
    void method2(); // Tự động là public
}

// Lớp cài đặt interface
class ExampleClass implements ExampleInterface {
    @Override
    public void method1() {
        System.out.println("Method1 implemented.");
    }

    @Override
    public void method2() {
        System.out.println("Method2 implemented.");
    }
}

// Lớp chính để kiểm tra và chứng minh rằng tất cả các phương thức trong interface là public
public class ExampleTest {
    public static void main(String[] args) {
        ExampleClass example = new ExampleClass();
        example.method1();
        example.method2();
    }
}