public class NameNumber {
    private String lastName;
    private String telNumber;

    // Constructor không tham số
    public NameNumber() {}

    // Constructor có tham số
    public NameNumber(String name, String num) {
        lastName = name;
        telNumber = num;
    }

    // Phương thức lấy họ tên
    public String getLastName() {
        return lastName;
    }

    // Phương thức lấy số điện thoại
    public String getTelNumber() {
        return telNumber;
    }
}

	