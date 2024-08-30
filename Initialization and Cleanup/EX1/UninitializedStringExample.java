package EX1;
public class UninitializedStringExample {
    // Khai báo một tham chiếu String nhưng chưa khởi tạo
    private String uninitializedString;

    public void displayString() {
        // In ra giá trị của uninitializedString
        if (uninitializedString == null) {
            System.out.println("The string is initialized to null by default.");
        } else {
            System.out.println("The string is: " + uninitializedString);
        }
    }

    public static void main(String[] args) {
        // Tạo đối tượng và gọi phương thức để kiểm tra giá trị mặc định
        UninitializedStringExample example = new UninitializedStringExample();
        example.displayString();
    }
}
