class ContinuousSignal implements Signal {
    private double frequency; // Tần số của tín hiệu

    public ContinuousSignal(double frequency) {
        this.frequency = frequency;
    }

    @Override
    public void generate() {
        // Trong trường hợp tín hiệu liên tục, phương thức generate() có thể chỉ thông báo về tần số
        System.out.println("Generating continuous signal with frequency: " + frequency + " Hz");
    }

    @Override
    public double getSignalValue(double time) {
        // Tín hiệu liên tục đơn giản sử dụng sóng sin
        return Math.sin(2 * Math.PI * frequency * time);
    }

    @Override
    public void displayInfo() {
        System.out.println("Continuous signal with frequency: " + frequency + " Hz.");
    }
}
