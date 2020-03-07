import java.util.*;

public class DSU {
    private Map<Integer, Integer> parent;
    private Map<Integer, Integer> size;

    public void makeSet(Integer a) {
        // make set only if a does not exist
        if (parent.containsKey(a)) return;
        parent.put(a, a);
        size.put(a, 1);
    }

    public void union(Integer a, Integer b) {
        Integer pa = find(a);
        Integer pb = find(b);
        if (pa == pb) return;
        // make pb pa's parent
        parent.put(pa, pb);
        Integer bSize = getSize(pb);
        Integer aSize = getSize(pa);
        size.put(pb, bSize + aSize);
    }

    public Integer find(Integer i) {
        if (parent.get(i) == i) return i;
        else {
            Integer p = find(parent.get(i));
            parent.put(i, p);
            return p;
        }
    }

    public Integer getSize(Integer a) {
        System.out.println(a);
        System.out.println(find(a));
        return size.get(find(a));
    }

    public DSU() {
        parent = new HashMap<Integer, Integer>();
        size = new HashMap<Integer, Integer>();
    }

    public static void main(String[] args) {
        DSU dsu = new DSU();

        dsu.makeSet(1);
        dsu.makeSet(2);
        dsu.union(1, 2);
        Integer tSize = dsu.getSize(2);
        System.out.println(tSize);
        
        dsu.makeSet(1);
        dsu.makeSet(3);
        dsu.union(1, 3);
        tSize = dsu.getSize(3);
        System.out.println(tSize);
    }
}