
public class NNCollection {
    private NNTree root;

    public NNCollection() {}

    public void insert(NameNumber n) {
        if (root != null) {
            root.insert(n);
        } else {
            root = new NNTree(n);
        }
    }

    public String findNumber(String lName) {
        if (root != null) {
            return root.findNumber(lName);
        } else {
            return "Name not found";
        }
    }

    // Phương thức main để kiểm tra lớp NNCollection
    public static void main(String[] args) {
        // Tạo một NNCollection mới
        NNCollection collection = new NNCollection();
        
        // Tạo các đối tượng NameNumber
        NameNumber nn1 = new NameNumber("Lewis", "268-1234");
        NameNumber nn2 = new NameNumber("Clay", "268-5678");
        NameNumber nn3 = new NameNumber("McCoy", "555-0000");
        NameNumber nn4 = new NameNumber("Day", "555-1234");

        // Chèn các đối tượng vào collection
        collection.insert(nn1);
        collection.insert(nn2);
        collection.insert(nn3);
        collection.insert(nn4);

        // Tìm số điện thoại theo tên
        System.out.println("Finding 'McCoy': " + collection.findNumber("McCoy"));
        System.out.println("Finding 'Day': " + collection.findNumber("Day"));
        System.out.println("Finding 'Clay': " + collection.findNumber("Clay"));
        System.out.println("Finding 'Lewis': " + collection.findNumber("Lewis"));
        System.out.println("Finding 'Smith': " + collection.findNumber("Smith")); // Không có
    }
}
