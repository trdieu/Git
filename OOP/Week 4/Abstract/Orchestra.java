// Abstract class Instrument
abstract class Instrument {
    private int i; // Storage allocated for each instance

    // Abstract method play
    public abstract void play();

    // Concrete method what
    public String what() {
        return "Instrument";
    }

    // Abstract method adjust
    public abstract void adjust();
}

// Wind class extends Instrument
class Wind extends Instrument {
    @Override
    public void play() {
        System.out.println("Wind.play()");
    }

    @Override
    public String what() {
        return "Wind";
    }

    @Override
    public void adjust() {
        System.out.println("Wind.adjust()");
    }
}

// Percussion class extends Instrument
class Percussion extends Instrument {
    @Override
    public void play() {
        System.out.println("Percussion.play()");
    }

    @Override
    public String what() {
        return "Percussion";
    }

    @Override
    public void adjust() {
        System.out.println("Percussion.adjust()");
    }
}

// Stringed class extends Instrument
class Stringed extends Instrument {
    @Override
    public void play() {
        System.out.println("Stringed.play()");
    }

    @Override
    public String what() {
        return "Stringed";
    }

    @Override
    public void adjust() {
        System.out.println("Stringed.adjust()");
    }
}

// Brass class extends Wind
class Brass extends Wind {
    @Override
    public void play() {
        System.out.println("Brass.play()");
    }

    @Override
    public void adjust() {
        System.out.println("Brass.adjust()");
    }
}

// Woodwind class extends Wind
class Woodwind extends Wind {
    @Override
    public void play() {
        System.out.println("Woodwind.play()");
    }

    @Override
    public String what() {
        return "Woodwind";
    }
}

// Main class to test the orchestra
public class Orchestra {
    // Method to tune an instrument
    static void tune(Instrument i) {
        i.play();
    }

    // Method to tune all instruments in the array
    static void tuneAll(Instrument[] orchestra) {
        for (Instrument i : orchestra) {
            tune(i);
        }
    }

    public static void main(String[] args) {
        // Creating an array of instruments
        Instrument[] orchestra = {
            new Wind(),
            new Percussion(),
            new Stringed(),
            new Brass(),
            new Woodwind()
        };

        // Tuning all instruments
        tuneAll(orchestra);
    }
}
