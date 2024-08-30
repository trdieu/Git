public class book {
    String title;
    String author;
    int numPages;

    // Constructor mặc định
    book() {
        this("Unknown Title", "Unknown Author", 0);
    }

    // Constructor với một tham số
    public book(String t) {
        this(t, "Unknown Author", 0);
    }

    // Constructor với hai tham số
    public book(String t, String a) {
        this(t, a, 0);
    }

    // Constructor với ba tham số
    public book(String t, String a, int p) {
        title = t;
        author = a;
        numPages = p;
    }

    public static void main(String[] args) {
        // Tạo đối tượng book với các constructor khác nhau
        book book1 = new book();
        book book2 = new book("The TeXbook");
        book book3 = new book("The TeXbook", "Donald Knuth");
        book book4 = new book("The TeXbook", "Donald Knuth", 483);

        // In ra thông tin các đối tượng book
        System.out.println("book1 - Title: " + book1.title + ", Author: " + book1.author + ", Pages: " + book1.numPages);
        System.out.println("book2 - Title: " + book2.title + ", Author: " + book2.author + ", Pages: " + book2.numPages);
        System.out.println("book3 - Title: " + book3.title + ", Author: " + book3.author + ", Pages: " + book3.numPages);
        System.out.println("book4 - Title: " + book4.title + ", Author: " + book4.author + ", Pages: " + book4.numPages);
    }
}
