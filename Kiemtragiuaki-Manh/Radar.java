public class Radar {
    // Phương thức phân tích tín hiệu theo mẫu
    public static int[] analyzeSignal(int length) {
        int[] signal = new int[length];
        for (int i = 0; i < length; i++) {
            if (i >= 0 && i <= 15) {
                signal[i] = (int) (100 * (1 - (i / 15.0)));  // Tính giá trị tín hiệu từ 100 đến 0
            } else {
                signal[i] = 0;  // Giá trị tín hiệu là 0 nếu ngoài phạm vi từ 0 đến 15
            }
        }
        return signal;
    }

    // Phương thức hiển thị tín hiệu
    public static void displaySignal(int[] signal) {
        for (int value : signal) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int n = 16;  // Đặt số lượng mẫu cần phân tích
        int[] signal = analyzeSignal(n);  // Phân tích tín hiệu với n = 16

        // Hiển thị tín hiệu
        System.out.println("Discrete Signal Sample Output:");
        displaySignal(signal);
    }
}
