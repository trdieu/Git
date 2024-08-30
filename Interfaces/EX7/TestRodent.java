// TestRodent.java
public class TestRodent {

    // Interface Rodent
    public interface Rodent {
        void eat();
        void sleep();
        void run();
    }

    // Class Mouse
    public static class Mouse implements Rodent {
        @Override
        public void eat() {
            System.out.println("Mouse eats.");
        }

        @Override
        public void sleep() {
            System.out.println("Mouse sleeps.");
        }

        @Override
        public void run() {
            System.out.println("Mouse runs.");
        }
    }

    // Class Gerbil
    public static class Gerbil implements Rodent {
        @Override
        public void eat() {
            System.out.println("Gerbil eats.");
        }

        @Override
        public void sleep() {
            System.out.println("Gerbil sleeps.");
        }

        @Override
        public void run() {
            System.out.println("Gerbil runs.");
        }
    }

    // Class Hamster
    public static class Hamster implements Rodent {
        @Override
        public void eat() {
            System.out.println("Hamster eats.");
        }

        @Override
        public void sleep() {
            System.out.println("Hamster sleeps.");
        }

        @Override
        public void run() {
            System.out.println("Hamster runs.");
        }
    }

    // Main method
    public static void main(String[] args) {
        Rodent[] rodents = {
            new Mouse(),
            new Gerbil(),
            new Hamster()
        };

        for (Rodent rodent : rodents) {
            rodent.eat();
            rodent.sleep();
            rodent.run();
            System.out.println();
        }
    }
}
