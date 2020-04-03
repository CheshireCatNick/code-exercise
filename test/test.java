import java.util.*;

class Rect {
    static String p = "R";
    static public int w = 5;
    public int h = 12;
    public String getP() {
        return p;
    }
    private int priv = 99;
    public int getPriv() {
        return this.priv;
    }
    static public int getW() {
        System.out.println("This is a Rect");
        return w;
    }
}

class Square extends Rect {
    static String p = "S";
    static public int w = 10;
    public int h = 10;
    public String getP() {
        return p;
    }
    static public int getW() {
        return w;
    }
}
class Test {

    private int value;

    public void set() {
        Scanner s = new Scanner(System.in);
        this.value = s.nextInt();
    }
    public void show() {
        System.out.println(this.value);
    }
    public Test(int v) {
        this.value = v;
    }
    public static void main(String args[]) {
        Square square = new Square();
        Rect rect = square;
        System.out.println(rect.p);
        System.out.println(rect.getP());
        System.out.println(rect.getW());
        System.out.println(rect.w);
        System.out.println(square.w);
        System.out.println(rect.getPriv());
        System.out.println(square.getPriv());
        


    }
    
}