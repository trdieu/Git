// File: OutsideClass.java
import mypackage.BaseClass;

public class OutsideClass {
    public static void main(String[] args) {
        BaseClass base = new BaseClass();
        // Không thể truy cập phương thức protectedMethod() từ bên ngoài package
        // base.protectedMethod(); // Lỗi biên dịch
    }
}
