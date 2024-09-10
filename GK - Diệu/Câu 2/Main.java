import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// Giao diện Signal
interface Signal {
    double getValue(int n);
}

// Lớp tín hiệu rời rạc DiscreteSignal
class DiscreteSignal implements Signal {
    private List<Double> signalValues;

    // Hàm khởi tạo tín hiệu với giá trị đầu vào
    public DiscreteSignal(List<Double> values) {
        this.signalValues = values;
    }

    // Hàm tính giá trị tín hiệu tại thời điểm n
    @Override
    public double getValue(int n) {
        if (n < 0 || n >= signalValues.size()) {
            return 0;  // Mặc định nếu n ngoài phạm vi
        }
        return signalValues.get(n);  // Giá trị của tín hiệu tại n
    }

    // Xung đơn vị delta(n)
    private int delta(int n) {
        return n == 0 ? 1 : 0;
    }

    // Tính tổng theo công thức tín hiệu rời rạc
    public double calculateDiscreteSignal(int n) {
        double result = 0;
        for (int k = 0; k < signalValues.size(); k++) {
            result += signalValues.get(k) * delta(n - k);
        }
        return result;
    }
}

// Lớp Radar phân tích tín hiệu
class Radar {
    
    // Tín hiệu X(n) theo định nghĩa bài toán
    public double calculateRadarSignal(int n) {
        if (n >= 0 && n <= 15) {
            return 1 - (double) n / 15;
        } else {
            return 0;
        }
    }
    
    // In tín hiệu cho n từ 0 đến 4
    public void printSignalForN() {
        for (int n = 0; n <= 4; n++) {
            System.out.println("X(" + n + ") = " + calculateRadarSignal(n));
        }
    }
}

// Lớp chính để chạy chương trình
public class Main {
    public static void main(String[] args) {
        // Tạo tín hiệu rời rạc với các giá trị
        DiscreteSignal discreteSignal = new DiscreteSignal(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0));
        System.out.println("Tín hiệu rời rạc tại n = 2: " + discreteSignal.calculateDiscreteSignal(2));
        
        // Tạo đối tượng Radar và in tín hiệu cho n = 0 đến 4
        Radar radar = new Radar();
        radar.printSignalForN();
    }
}
