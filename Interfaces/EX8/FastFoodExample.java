// File: FastFoodExample.java
package polymorphism;

public class FastFoodExample {

    // Interface FastFood
    public interface FastFood {
        void order();
        void prepare();
        void serve();
    }

    // Class Sandwich implementing FastFood
    public static class Sandwich implements FastFood {
        @Override
        public void order() {
            System.out.println("Ordering a sandwich.");
        }

        @Override
        public void prepare() {
            System.out.println("Preparing a sandwich.");
        }

        @Override
        public void serve() {
            System.out.println("Serving a sandwich.");
        }

        public void make() {
            System.out.println("Making a sandwich.");
        }
    }

    // Class TestFastFood to test the FastFood implementation
    public static class TestFastFood {
        public static void main(String[] args) {
            FastFood myFood = new Sandwich();
            myFood.order();
            myFood.prepare();
            myFood.serve();

            // Optional: Demonstrate that Sandwich methods work too
            if (myFood instanceof Sandwich) {
                Sandwich sandwich = (Sandwich) myFood;
                sandwich.make();
            }
        }
    }
}