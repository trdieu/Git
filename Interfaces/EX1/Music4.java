//: interfaces/music4/Music4.java 
// Abstract classes and methods. 
package interfaces.music4;

// Thay thế import bằng các lệnh in chuẩn của Java
// import static net.mindview.util.Print.*; 

// Giả định rằng Note là một enum hoặc lớp đơn giản
enum Note {
    MIDDLE_C, C_SHARP, B_FLAT
}

// Lớp trừu tượng Instrument
abstract class Instrument { 
    public abstract void play(Note n); 
    public String what() { return "Instrument"; } 
    public abstract void adjust(); 
}

// Lớp cụ thể Wind
class Wind extends Instrument { 
    @Override
    public void play(Note n) { 
        System.out.println("Wind.play() " + n); 
    } 
    @Override
    public String what() { return "Wind"; } 
    @Override
    public void adjust() {} 
}

// Lớp cụ thể Percussion
class Percussion extends Instrument { 
    @Override
    public void play(Note n) { 
        System.out.println("Percussion.play() " + n); 
    } 
    @Override
    public String what() { return "Percussion"; } 
    @Override
    public void adjust() {} 
}

// Lớp cụ thể Stringed
class Stringed extends Instrument { 
    @Override
    public void play(Note n) { 
        System.out.println("Stringed.play() " + n); 
    } 
    @Override
    public String what() { return "Stringed"; } 
    @Override
    public void adjust() {} 
}

// Lớp cụ thể Brass
class Brass extends Wind { 
    @Override
    public void play(Note n) { 
        System.out.println("Brass.play() " + n); 
    } 
    @Override
    public void adjust() { 
        System.out.println("Brass.adjust()"); 
    } 
}

// Lớp cụ thể Woodwind
class Woodwind extends Wind { 
    @Override
    public void play(Note n) { 
        System.out.println("Woodwind.play() " + n); 
    } 
    @Override
    public String what() { return "Woodwind"; } 
}

public class Music4 { 
    // Không quan tâm đến loại, vì vậy các loại mới
    // thêm vào hệ thống vẫn hoạt động đúng: 
    static void tune(Instrument i) { 
        i.play(Note.MIDDLE_C); 
    } 
    static void tuneAll(Instrument[] e) { 
        for (Instrument i : e) 
            tune(i); 
    } 
    public static void main(String[] args) { 
        // Upcasting trong khi thêm vào mảng: 
        Instrument[] orchestra = { 
            new Wind(), 
            new Percussion(), 
            new Stringed(), 
            new Brass(), 
            new Woodwind() 
        }; 
        tuneAll(orchestra); 
    } 
} 
