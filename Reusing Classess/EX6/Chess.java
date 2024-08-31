// Lớp Game với constructor có tham số
class Game {
    Game(int i) {
        System.out.println("Constructor cua Game duoc goi");
    }
}

// Lớp BoardGame kế thừa từ Game, gọi constructor của Game
class BoardGame extends Game {
    BoardGame(int i) {
        super(i);  // Gọi constructor của lớp Game với tham số
        System.out.println("Constructor cua BoardGame duoc goi");
    }
}

// Lớp Chess kế thừa từ BoardGame, gọi constructor của BoardGame
public class Chess extends BoardGame {
    Chess() {
        super(11);  // Gọi constructor của BoardGame với tham số 11
        System.out.println("Constructor cua Chess duoc goi");
    }

    public static void main(String[] args) {
        // Tạo đối tượng của lớp Chess và quan sát thứ tự gọi constructor
        Chess x = new Chess();
    }
}
	