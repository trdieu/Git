//: interfaces/rodent/Rodent.java
package interfaces.rodent;

// Lớp trừu tượng Rodent
abstract class Rodent {
    public abstract void eat();
    public abstract void sleep();
    public abstract void makeSound();
}

class Mouse extends Rodent {
    @Override
    public void eat() {
        System.out.println("Mouse eats.");
    }

    @Override
    public void sleep() {
        System.out.println("Mouse sleeps.");
    }

    @Override
    public void makeSound() {
        System.out.println("Mouse squeaks.");
    }
}

class Rat extends Rodent {
    @Override
    public void eat() {
        System.out.println("Rat eats.");
    }

    @Override
    public void sleep() {
        System.out.println("Rat sleeps.");
    }

    @Override
    public void makeSound() {
        System.out.println("Rat screeches.");
    }
}

public class RodentTest {
    public static void main(String[] args) {
        Rodent[] rodents = { new Mouse(), new Rat() };
        for (Rodent r : rodents) {
            r.eat();
            r.sleep();
            r.makeSound();
        }
    }
}
