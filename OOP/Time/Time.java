public class Time {
    private int hour;
    private int minute;
    private int second;

    // Constructor mặc định
    public Time() {
        this.hour = 0;
        this.minute = 0;
        this.second = 0;
    }

    // Constructor có tham số
    public Time(int hour, int minute, int second) {
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    // Các phương thức set
    public Time setHour(int hour) {
        this.hour = hour;
        return this;
    }

    public Time setMinute(int minute) {
        this.minute = minute;
        return this;
    }

    public Time setSecond(int second) {
        this.second = second;
        return this;
    }

    // Ghi đè phương thức toString để in thời gian
    @Override
    public String toString() {
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }
}
