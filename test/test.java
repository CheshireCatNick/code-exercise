import java.util.*;

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
        Test t = new Test(5);
        t.show();
        t.set();
        t.show();
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        m.put(1, 2);
        m.put(2, 3);
        System.out.println(m.get(1));
        System.out.println(m.get(2));
        m.put(2, m.get(2) + 1);
        System.out.println(m.get(2));
        System.out.println(m.get(10) == null);
        System.out.println(m.get(2) == 4);
    }
}