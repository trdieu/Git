public class TestNameNumber {
    public static void main(String[] args) {
        // Tạo các đối tượng NameNumber
        NameNumber nn1 = new NameNumber("Lewis", "268-1234");
        NameNumber nn2 = new NameNumber("Clay", "268-5678");
        NameNumber nn3 = new NameNumber("McCoy", "555-0000");
        NameNumber nn4 = new NameNumber("Day", "555-1234");

        // Kiểm tra các phương thức của lớp NameNumber
        System.out.println("Testing NameNumber class:");

        System.out.println("Name: " + nn1.getLastName() + ", Phone Number: " + nn1.getTelNumber());
        System.out.println("Name: " + nn2.getLastName() + ", Phone Number: " + nn2.getTelNumber());
        System.out.println("Name: " + nn3.getLastName() + ", Phone Number: " + nn3.getTelNumber());
        System.out.println("Name: " + nn4.getLastName() + ", Phone Number: " + nn4.getTelNumber());
    }
}
	