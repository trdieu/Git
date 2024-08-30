public class RecursionExample {
    // Hàm tính giai thừa của một số nguyên dương
    public static long factorial(long number) {
        if (number <= 1) { // Điều kiện dừng
            return 1;
        } else {
            return number * factorial(number - 1); // Gọi đệ quy
        }
    }

    public static void main(String[] args) {
        System.out.println("5! = " + factorial(5)); // In kết quả giai thừa của 5
    }
}
