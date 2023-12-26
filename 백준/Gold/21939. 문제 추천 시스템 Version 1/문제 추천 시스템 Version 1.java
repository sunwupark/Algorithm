import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Collections;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Vector;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        PriorityQueue<value> maxQueue = new PriorityQueue<>();
        PriorityQueue<value> minQueue = new PriorityQueue<>(Collections.reverseOrder());
        int N = Integer.parseInt(br.readLine());
        for(int p = 0; p < N; p++){
            String[] s = br.readLine().split(" ");
            int P = Integer.parseInt(s[0]);
            int L = Integer.parseInt(s[1]);
            hashMap.put(P, L);
            maxQueue.add(new value(P,L));
            minQueue.add(new value(P,L));
        }
        int M = Integer.parseInt(br.readLine());
        for(int i = 0; i< M; i++){
            String[] s = br.readLine().split(" ");
//            System.out.println("s = " + s[0]);
//            System.out.println("hashMap = " + hashMap);
//            System.out.println("minQueue = " + minQueue.peek().P);
//            System.out.println("maxQueue = " +maxQueue.peek().P);
            switch (s[0]){
                case "add":
                    int i1 = Integer.parseInt(s[1]);
                    int i2 = Integer.parseInt(s[2]);
                    Integer orDefault = hashMap.getOrDefault(i1, 0);
                    if(orDefault > 0){
                        if(orDefault == i2){
                            break;
                        }
                    }
                    hashMap.put(i1, i2);
                    maxQueue.add(new value(i1, i2));
                    minQueue.add(new value(i1, i2));
                    break;
                case "recommend":
                    PriorityQueue<value> values = Integer.parseInt(s[1]) == 1 ? maxQueue : minQueue;
                    System.out.println(values.peek().P);
                    break;
                case "solved":
                    removeElement(maxQueue, hashMap, Integer.parseInt(s[1]));
                    removeElement(minQueue, hashMap, Integer.parseInt(s[1]));
                    break;
            }
        }
    }

    public static int removeElement(PriorityQueue<value> queue, HashMap<Integer, Integer> hashMap, int element){
        int n;
        while(true){
            value value = queue.poll();
            n = hashMap.getOrDefault(value.P, 0);
            if(n == 0){
                continue;
            }
            if(n >= 1){
                if(element == value.P){
                    hashMap.remove(value.P);
                }
                else {
                    queue.add(value);
                }
            }
            break;
        }
        return n;
    }

    public static int removeMap(PriorityQueue<value> queue, HashMap<Integer, Integer> hashMap){
        int n;
        while(true){
            value value = queue.poll();
            n = hashMap.getOrDefault(value.P, 0);
            System.out.println("n = " + n);
            if(n == 0){
                continue;
            }
            if(n >= 1){
                hashMap.remove(value.P);
            }
            break;
        }
        return n;
    }
}

class value implements Comparable<value> {
    int P;
    int L;

    public value(int P, int L) {
        this.P = P;
        this.L = L;
    }
    @Override
    public int compareTo(value o) {
        return this.L == o.L ? (this.P < o.P ? 1 : -1) : (this.L < o.L ? 1: -1);
    }
}