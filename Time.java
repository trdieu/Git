/*Time setTime(int h, int m, int s) {
    setHour(h);
    setMinute(m);
    setSecond(s);
    return this;
    }
    Time setHour(int h) {
    hour = (( h >= 0 && h < 24 ) ? h : 0 );
    return this;
    }
*/
public class Time {
    private int hour;   // 0 - 23
    private int minute; // 0 - 59
    private int second; // 0 - 59

    // Constructor mặc định
    public Time() {
        this.hour = 0;
        this.minute = 0;
        this.second = 0;
    }

    // Phương thức setTime: thiết lập giờ, phút, giây
    public Time setTime(int h, int m, int s) {
        setHour(h);
        setMinute(m);
        setSecond(s);
        return this;
    }

    // Phương thức setHour: thiết lập giờ
    public Time setHour(int h) {
        this.hour = (h >= 0 && h < 24) ? h : 0;
        return this;
    }

    // Phương thức setMinute: thiết lập phút
    public Time setMinute(int m) {
        this.minute = (m >= 0 && m < 60) ? m : 0;
        return this;
    }

    // Phương thức setSecond: thiết lập giây
    public Time setSecond(int s) {
        this.second = (s >= 0 && s < 60) ? s : 0;
        return this;
    }

    // Phương thức toString: trả về thời gian dưới dạng chuỗi
    @Override
    public String toString() {
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }

    public static void main(String[] args) {
        Time t = new Time();           // Khởi tạo đối tượng Time
        t.setTime(13, 45, 30);         // Thiết lập thời gian
        System.out.println(t);         // In ra thời gian đã thiết lập
    }
}
