import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class SaveUserInfo {
    public static void main(String[] args) {
        // Tạo một ArrayList để lưu trữ thông tin người dùng
        ArrayList<User> userList = new ArrayList<>();
        userList.add(new User("john_doe", "password123", "John", "Doe"));
        userList.add(new User("jane_smith", "password456", "Jane", "Smith"));

        // Gọi hàm để ghi thông tin vào file
        saveUserInfoToFile(userList, "Data/Login.txt");
    }

    // Hàm để ghi thông tin người dùng vào file
    public static void saveUserInfoToFile(ArrayList<User> users, String filePath) {
        try (FileWriter writer = new FileWriter(filePath)) {
            for (User user : users) {
                writer.write(user.getUsername() + "," + user.getPassword() + "," + user.getFirstName() + "," + user.getLastName() + "\n");
            }
            System.out.println("Luu thong tin nguoi dung thanh cong!");
        } catch (IOException e) {
            System.out.println("Loi khi luu thong tin: " + e.getMessage());
        }
    }
}

// Lớp User chứa thông tin người dùng
class User {
    private String username;
    private String password;
    private String firstName;
    private String lastName;

    public User(String username, String password, String firstName, String lastName) {
        this.username = username;
        this.password = password;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }
}
