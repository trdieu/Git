public class TestTime {
    public static void main(String[] args) {
        // Tạo đối tượng t1 và t2 của lớp Time
        Time t1 = new Time();           // Sử dụng constructor mặc định
        Time t2 = new Time(20, 3, 45);  // Khởi tạo với giá trị cụ thể (giờ, phút, giây)

        // Thay đổi thời gian của t1
        t1.setHour(7).setMinute(32).setSecond(23);

        // In thời gian của t1 và t2
        System.out.println("t1 is " + t1);
        System.out.println("t2 is " + t2);
    }
}
