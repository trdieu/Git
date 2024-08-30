public class StringInitializationExample {
    // Trường String được khởi tạo tại điểm định nghĩa
    private String initializedAtDefinition = "Initialized at definition";

    // Trường String được khởi tạo thông qua constructor
    private String initializedInConstructor;

    // Constructor để khởi tạo initializedInConstructor
    public StringInitializationExample(String value) {
        this.initializedInConstructor = value;
    }

    // Phương thức để hiển thị giá trị của hai trường String
    public void displayStrings() {
        System.out.println("String initialized at definition: " + initializedAtDefinition);
        System.out.println("String initialized in constructor: " + initializedInConstructor);
    }

    public static void main(String[] args) {
        // Tạo đối tượng với giá trị được khởi tạo trong constructor
        StringInitializationExample example = new StringInitializationExample("Initialized in constructor");
        example.displayStrings();
    }
}
