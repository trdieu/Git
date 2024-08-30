// TestAccess.java
public class TestAccess {
    public static void main(String[] args) {
        AccessModifiersExample example = new AccessModifiersExample();

        // Truy cập các trường
        System.out.println("Public Field: " + example.publicField);
        // System.out.println("Private Field: " + example.privateField); // Lỗi
        System.out.println("Protected Field: " + example.protectedField);
        System.out.println("Package Field: " + example.packageField);

        // Gọi các phương thức
        example.publicMethod();
        // example.privateMethod(); // Lỗi
        example.protectedMethod();
        example.packageMethod();
    }
}
