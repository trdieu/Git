// Base class Cleanser
class Cleanser {
    private String s = "Cleanser";

    public void append(String a) { s += a; }
    public void dilute() { append(" dilute()"); }
    public void apply() { append(" apply()"); }
    public void scrub() { append(" scrub()"); }
    public String toString() { return s; }

    // Add main method in Cleanser
    public static void main(String[] args) {
        Cleanser cleanser = new Cleanser();
        cleanser.dilute();
        cleanser.apply();
        cleanser.scrub();
        System.out.println(cleanser);
    }
}

// Derived class Detergent
public class Detergent extends Cleanser {
    // Override the scrub method
    public void scrub() {
        append(" Detergent.scrub()");
        super.scrub(); // Call the base class's scrub method
    }

    // Add a new method to Detergent
    public void foam() {
        append(" foam()");
    }

    public static void main(String[] args) {
        Detergent x = new Detergent();
        x.dilute();
        x.apply();
        x.scrub();
        x.foam();
        System.out.println(x);
        System.out.println("Testing base class:");
        Cleanser.main(args);
    }
}
