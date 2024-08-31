// Glyph.java
abstract class Glyph {
    abstract void draw();
    
    Glyph() {
        System.out.println("Glyph() before draw");
        draw(); // Gọi phương thức draw() của lớp con
        System.out.println("Glyph() after draw");
    }
}

// RoundGlyph.java
class RoundGlyph extends Glyph {
    int radius = 1;
    
    RoundGlyph(int r) {
        radius = r;
        System.out.println("RoundGlyph(), radius=" + radius);
    }
    
    @Override
    void draw() {
        System.out.println("RoundGlyph.draw(), radius=" + radius);
    }
}

// GlyphTest.java
public class GlyphTest {
    public static void main(String[] args) {
        new RoundGlyph(5); // Tạo một đối tượng RoundGlyph
    }
}
