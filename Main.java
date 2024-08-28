import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Nhập họ và tên
        System.out.println("Nhập vào họ và tên:");
        String hoVaten = sc.nextLine(); // Đọc chuỗi

        // Nhập mã sinh viên
        System.out.println("Nhập mã sinh viên:");
        long maSinhVien = sc.nextLong();

        // Nhập điểm thi
        System.out.println("Nhập vào điểm thi:");
        float diemthi = sc.nextFloat();

        // Hiển thị thông tin
        System.out.println("Họ và tên là: " + hoVaten);
        System.out.println("Mã sinh viên là: " + maSinhVien);
        System.out.println("Điểm thi là: " + diemthi);

        // Đóng Scanner
        sc.close();
    }
}
