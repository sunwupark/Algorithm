import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static boolean[] isVisit;
    static HashMap<Integer, List<Integer>> hashMap = new HashMap<>();
    static int[] parent;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        isVisit = new boolean[N+1];
        parent = new int[N+1];

        for(int i = 0; i < N-1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            List<Integer> listA = hashMap.getOrDefault(a, new ArrayList<>());
            listA.add(b);
            hashMap.put(a, listA);

            List<Integer> listB = hashMap.getOrDefault(b, new ArrayList<>());
            listB.add(a);
            hashMap.put(b, listB);
        }

        dfs(1);

        for(int i = 2; i < parent.length; i++){
            System.out.println(parent[i]);
        }
    }

    public static void dfs(int index){
        isVisit[index] = true;
        for(int i : hashMap.get(index)){
            if(!isVisit[i]){
                parent[i] = index;
                dfs(i);
            }
        }
    }
}
