// Giao diện tín hiệu (Signal)
interface Signal {
    // Phương thức để lấy giá trị tín hiệu tại thời điểm t
    double getValue(double t);
}

// Lớp tín hiệu rời rạc (DiscreteSignal)
class DiscreteSignal implements Signal {
    private double[] values;
    private double timeStep;

    public DiscreteSignal(double[] values, double timeStep) {
        this.values = values;
        this.timeStep = timeStep;
    }

    // Lấy giá trị tín hiệu rời rạc tại thời điểm t
    @Override
    public double getValue(double t) {
        int index = (int) Math.round(t / timeStep);
        if (index >= 0 && index < values.length) {
            return values[index];
        } else {
            return 0; // Giá trị mặc định nếu t ngoài phạm vi
        }
    }
}

// Lớp tín hiệu liên tục (ContinuousSignal)
class ContinuousSignal implements Signal {
    private double amplitude;
    private double frequency;

    public ContinuousSignal(double amplitude, double frequency) {
        this.amplitude = amplitude;
        this.frequency = frequency;
    }

    // Lấy giá trị tín hiệu liên tục tại thời điểm t
    @Override
    public double getValue(double t) {
        return amplitude * Math.sin(2 * Math.PI * frequency * t);
    }
}

// Lớp chính để chạy chương trình
public class Main {
    public static void main(String[] args) {
        // Tạo tín hiệu rời rạc
        double[] discreteValues = {1.0, 2.0, 3.0, 4.0, 5.0};
        DiscreteSignal discreteSignal = new DiscreteSignal(discreteValues, 1.0);

        // Tạo tín hiệu liên tục
        ContinuousSignal continuousSignal = new ContinuousSignal(2.0, 1.0);

        // Hiển thị giá trị tín hiệu rời rạc tại t = 2
        System.out.println("Giá trị tín hiệu rời rạc tại t = 2: " + discreteSignal.getValue(2.0));

        // Hiển thị giá trị tín hiệu liên tục tại t = 2
        System.out.println("Giá trị tín hiệu liên tục tại t = 2: " + continuousSignal.getValue(2.0));

        // Hiển thị giá trị tín hiệu liên tục tại t = 0.5
        System.out.println("Giá trị tín hiệu liên tục tại t = 0.5: " + continuousSignal.getValue(0.5));
    }
}
