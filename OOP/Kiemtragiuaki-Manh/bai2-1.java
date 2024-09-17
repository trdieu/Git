class DiscreteSignal {
    // Thuộc tính
    private double[] coefficients; // Mảng chứa các hệ số a_k
    private int[] indices;         // Mảng chứa các chỉ số k tương ứng với mỗi a_k

    // Constructor để khởi tạo tín hiệu
    public DiscreteSignal(double[] coefficients, int[] indices) {
        this.coefficients = coefficients;
        this.indices = indices;
    }

    // Phương thức tính tín hiệu x(n)
    public double x(int n) {
        double result = 0;
        for (int i = 0; i < coefficients.length; i++) {
            result += coefficients[i] * delta(n - indices[i]);
        }
        return result;
    }

    // Hàm xung đơn vị delta(n)
    private int delta(int n) {
        if (n == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    // Phương thức hiển thị tín hiệu trong khoảng cho trước
    public void displaySignal(int start, int end) {
        for (int n = start; n <= end; n++) {
            System.out.println("x(" + n + ") = " + x(n));
        }
    }
}
