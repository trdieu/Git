package polymorphism.music3;

import java.util.Random;

public class Music3 {

    public static void main(String[] args) {
        Instrument[] orchestra = {
            new Wind(),
            new Percussion(),
            new Stringed(),
            new Brass(),
            new Woodwind()
        };

        for (Instrument instrument : orchestra) {
            System.out.println(instrument); // Calls toString() method
        }

        tuneAll(orchestra);
    }

    public static void tune(Instrument i) {
        i.play(Note.MIDDLE_C);
    }

    public static void tuneAll(Instrument[] e) {
        for (Instrument i : e) {
            tune(i);
        }
    }

    // Note Enum
    public enum Note {
        MIDDLE_C
    }

    // Instrument Base Class
    static class Instrument {
        void play(Note n) {
            System.out.println("Instrument.play() " + n);
        }

        @Override
        public String toString() {
            return "Instrument";
        }

        void adjust() {
            System.out.println("Adjusting Instrument");
        }
    }

    // Wind Class
    static class Wind extends Instrument {
        @Override
        void play(Note n) {
            System.out.println("Wind.play() " + n);
        }

        @Override
        public String toString() {
            return "Wind";
        }

        @Override
        void adjust() {
            System.out.println("Adjusting Wind");
        }
    }

    // Percussion Class
    static class Percussion extends Instrument {
        @Override
        void play(Note n) {
            System.out.println("Percussion.play() " + n);
        }

        @Override
        public String toString() {
            return "Percussion";
        }

        @Override
        void adjust() {
            System.out.println("Adjusting Percussion");
        }
    }

    // Stringed Class
    static class Stringed extends Instrument {
        @Override
        void play(Note n) {
            System.out.println("Stringed.play() " + n);
        }

        @Override
        public String toString() {
            return "Stringed";
        }

        @Override
        void adjust() {
            System.out.println("Adjusting Stringed");
        }
    }

    // Brass Class
    static class Brass extends Wind {
        @Override
        void play(Note n) {
            System.out.println("Brass.play() " + n);
        }

        @Override
        public String toString() {
            return "Brass";
        }

        @Override
        void adjust() {
            System.out.println("Adjusting Brass");
        }
    }

    // Woodwind Class
    static class Woodwind extends Wind {
        @Override
        void play(Note n) {
            System.out.println("Woodwind.play() " + n);
        }

        @Override
        public String toString() {
            return "Woodwind";
        }
    }
}