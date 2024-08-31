import java.util.Random;

// Lớp cơ sở Shape
class Shape {
    public void draw() {}
    public void erase() {}

    // Phương thức mới không ghi đè trong các lớp dẫn xuất
    public void message() {
        System.out.println("Message from Shape");
    }
}

// Lớp dẫn xuất Circle
class Circle extends Shape {
    @Override
    public void draw() {
        System.out.println("Circle.draw()");
    }

    @Override
    public void erase() {
        System.out.println("Circle.erase()");
    }

    @Override
    public void message() {
        System.out.println("Message from Circle");
    }
}

// Lớp dẫn xuất Square
class Square extends Shape {
    @Override
    public void draw() {
        System.out.println("Square.draw()");
    }

    @Override
    public void erase() {
        System.out.println("Square.erase()");
    }

    @Override
    public void message() {
        System.out.println("Message from Square");
    }
}

// Lớp dẫn xuất Triangle
class Triangle extends Shape {
    @Override
    public void draw() {
        System.out.println("Triangle.draw()");
    }

    @Override
    public void erase() {
        System.out.println("Triangle.erase()");
    }

    @Override
    public void message() {
        System.out.println("Message from Triangle");
    }
}

// Lớp dẫn xuất Hexagon (hình lục giác)
class Hexagon extends Shape {
    @Override
    public void draw() {
        System.out.println("Hexagon.draw()");
    }

    @Override
    public void erase() {
        System.out.println("Hexagon.erase()");
    }

    @Override
    public void message() {
        System.out.println("Message from Hexagon");
    }
}

// Lớp RandomShapeGenerator
class RandomShapeGenerator {
    private Random rand = new Random(47);

    public Shape next() {
        switch(rand.nextInt(4)) { // Cập nhật để bao gồm Hexagon
            default:
            case 0: return new Circle();
            case 1: return new Square();
            case 2: return new Triangle();
            case 3: return new Hexagon();
        }
    }
}

// Lớp chính ShapesDemo
public class ShapesDemo {
    private static RandomShapeGenerator gen = new RandomShapeGenerator();

    public static void main(String[] args) {
        Shape[] s = new Shape[9];
        // Fill up the array with shapes:
        for(int i = 0; i < s.length; i++)
            s[i] = gen.next();

        // Make polymorphic method calls:
        for(Shape shp : s) {
            shp.draw();
            shp.message(); // Gọi phương thức mới
        }
    }
}
	