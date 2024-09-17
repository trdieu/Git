// DisruptLecture.java

class Tune {
    public void play() {
        System.out.println("Playing a regular tune.");
    }
}

class ObnoxiousTune extends Tune {
    @Override
    public void play() {
        System.out.println("Playing an obnoxious tune.");
    }
}

class CellPhone {
    public void ring(Tune t) {
        t.play();
    }
}

public class DisruptLecture {
    public static void main(String[] args) {
        CellPhone noiseMaker = new CellPhone();
        Tune t1 = new Tune();
        Tune t2 = new ObnoxiousTune();

        // Calling the ring method with different Tune objects
        noiseMaker.ring(t1);  // Calls Tune's play method
        noiseMaker.ring(t2);  // Calls ObnoxiousTune's play method

        // Downcasting Tune to ObnoxiousTune, may cause a ClassCastException
        try {
            noiseMaker.ring((ObnoxiousTune) t1);  // This will throw a ClassCastException
        } catch (ClassCastException e) {
            System.out.println("Caught a ClassCastException!");
        }
        
        // Ringing with a properly casted ObnoxiousTune
        noiseMaker.ring(t2);  // Calls ObnoxiousTune's play method
    }
}
