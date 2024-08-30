package Time;
public class Time {
    int hour;
    int minute;
    int second;

    // Constructors
    Time() {
        setTime(0, 0, 0);
    }

    Time(int h) {
        setTime(h, 0, 0);
    }

    Time(int h, int m) {
        setTime(h, m, 0);
    }

    Time(int h, int m, int s) {
        setTime(h, m, s);
    }

    // Set time method
    Time setTime(int h, int m, int s) {
        setHour(h);
        setMinute(m);
        setSecond(s);
        return this;
    }

    // Setters for hour, minute, and second
    Time setHour(int h) {
        hour = (h >= 0 && h < 24) ? h : 0;
        return this;
    }

    Time setMinute(int m) {
        minute = (m >= 0 && m < 60) ? m : 0;
        return this;
    }

    Time setSecond(int s) {
        second = (s >= 0 && s < 60) ? s : 0;
        return this;
    }

    // Getters for hour, minute, and second
    int getHour() {
        return hour;
    }

    int getMinute() {
        return minute;
    }

    int getSecond() {
        return second;
    }

    // Overriding toString method to format the time in 12-hour format
    @Override
    public String toString() {
        return "" + ((hour == 12 || hour == 0) ? 12 : hour % 12) +
                ":" + (minute < 10 ? "0" : "") + minute +
                ":" + (second < 10 ? "0" : "") + second +
                (hour < 12 ? " AM" : " PM");
    }
}
