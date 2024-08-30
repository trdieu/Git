// File: Main.java
package main;

public class Main {
    public static void main(String[] args) {
        MyInterface obj = new MyInterfaceImpl();
        
        obj.method1();
        obj.method2();
        obj.method3();
    }
}

// Interface định nghĩa ba phương thức
interface MyInterface {
    void method1();
    void method2();
    void method3();
}

// Lớp triển khai interface
class MyInterfaceImpl implements MyInterface {
    @Override
    public void method1() {
        System.out.println("Implementing method1");
    }

    @Override
    public void method2() {
        System.out.println("Implementing method2");
    }

    @Override
    public void method3() {
        System.out.println("Implementing method3");
    }
}
