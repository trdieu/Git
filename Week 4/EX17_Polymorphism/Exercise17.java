// Base class Cycle
class Cycle {
    public void ride() {
        System.out.println("Riding a cycle");
    }
}

// Unicycle class extends Cycle and adds balance() method
class Unicycle extends Cycle {
    public void balance() {
        System.out.println("Balancing on a unicycle");
    }

    @Override
    public void ride() {
        System.out.println("Riding a unicycle");
    }
}

// Bicycle class extends Cycle and adds balance() method
class Bicycle extends Cycle {
    public void balance() {
        System.out.println("Balancing on a bicycle");
    }

    @Override
    public void ride() {
        System.out.println("Riding a bicycle");
    }
}

// Tricycle class extends Cycle but no balance() method
class Tricycle extends Cycle {
    @Override
    public void ride() {
        System.out.println("Riding a tricycle");
    }
}

public class Exercise17 {
    public static void main(String[] args) {
        // Create instances of all three types
        Cycle[] cycles = {
            new Unicycle(),
            new Bicycle(),
            new Tricycle()
        };

        // Try to call balance() on each element of the array (this will not work directly)
        for (Cycle cycle : cycles) {
            cycle.ride();  // Polymorphism at work
            // Compile-time error if we try to call balance() here:
            // cycle.balance();
        }

        // Downcast and call balance() where appropriate
        ((Unicycle) cycles[0]).balance(); // Successful downcast to Unicycle
        ((Bicycle) cycles[1]).balance();  // Successful downcast to Bicycle

        // The following line would throw a ClassCastException if uncommented
        // ((Unicycle) cycles[2]).balance(); // Unsuccessful downcast, Tricycle does not have balance()
    }
}
