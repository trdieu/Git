// Node.java
class Node {
    public Node() {}
    
    public double eval() {
        System.out.println("Error: eval Node");
        return 0;
    }
}

// Binop.java
class Binop extends Node {
    protected Node lChild, rChild;
    
    public Binop(Node l, Node r) {
        lChild = l;
        rChild = r;
    }
}

// Plus.java
class Plus extends Binop {
    public Plus(Node l, Node r) {
        super(l, r); // gọi constructor của lớp Binop
    }
    
    public double eval() {
        return lChild.eval() + rChild.eval();
    }
}

// Const.java
class Const extends Node {
    private double value;
    
    public Const(double d) {
        value = d;
    }
    
    public double eval() {
        return value;
    }
}

// TestArithmetic.java
public class TestArithmetic {
    // evaluate 1.1 + 2.2 + 3.3
    public static void main(String[] args) {
        Node n = new Plus(
            new Plus(
                new Const(1.1), new Const(2.2)),
            new Const(3.3)
        );
        
        System.out.println("Result: " + n.eval());
        
        // Another example with node representation
        Node n1 = new Const(1.1);
        Node n2 = new Const(2.2);
        Node n3 = new Plus(n1, n2);
        Node n4 = new Const(3.3);
        Node n5 = new Plus(n3, n4);
        
        System.out.println("Result with individual nodes: " + n5.eval());
    }
}
