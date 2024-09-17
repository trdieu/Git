class DiscreteSignal implements Signal {
    private double[] signalValues;

    public DiscreteSignal(int size) {
        signalValues = new double[size];
    }

    @Override
    public void generate() {
        for (int i = 0; i < signalValues.length; i++) {
            signalValues[i] = Math.random(); // Tạo tín hiệu ngẫu nhiên
        }
    }

    @Override
    public double getSignalValue(double time) {
        int index = (int) time;
        return (index >= 0 && index < signalValues.length) ? signalValues[index] : 0;
    }

    @Override
    public void displayInfo() {
        System.out.println("Discrete signal with " + signalValues.length + " samples.");
    }
}
