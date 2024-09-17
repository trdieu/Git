// Actor.java
abstract class Actor {
    abstract void act();
}

// HappyActor.java
class HappyActor extends Actor {
    @Override
    public void act() {
        System.out.println("HappyActor is acting.");
    }
}

// SadActor.java
class SadActor extends Actor {
    @Override
    public void act() {
        System.out.println("SadActor is acting.");
    }
}

// Stage.java
class Stage {
    private Actor actor = new HappyActor(); // mặc định là HappyActor

    void change() {
        actor = new SadActor(); // đổi sang SadActor
    }

    void go() {
        actor.act(); // gọi phương thức act() của Actor hiện tại
    }
}

// Transmogrify.java
public class Transmogrify {
    public static void main(String[] args) {
        Stage stage = new Stage();
        stage.go(); // HappyActor is acting
        stage.change(); // đổi sang SadActor
        stage.go(); // SadActor is acting
    }
}
