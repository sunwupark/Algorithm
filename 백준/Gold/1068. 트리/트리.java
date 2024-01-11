import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int D;
    static ArrayList<Integer>[] graph;
    static boolean visited[];
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer stk;
        graph = new ArrayList[N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < N; i++)
            graph[i] = new ArrayList<>();
        int root = -1;

        stk = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int p = Integer.parseInt(stk.nextToken());
            if (p == -1) {
                // i 노드가 바로 루트 노드
                root = i; // 루트 노드 정보를 저장함
            } else {
                // p 가 i 노드의 부모 노드임
                graph[i].add(p);
                graph[p].add(i); // 서로 연결
            }
        }

        D = Integer.parseInt(br.readLine());

        if(D == root){
            System.out.println(0);
            return;
        } else
            gothrough(root);

        System.out.println(ans);
    }

    static void gothrough(int num) {
        visited[num] = true;
        int nodes = 0;
        for(int cur : graph[num]){
            if(cur != D && !visited[cur]){
                nodes++;
                gothrough(cur);
            }
        }
        if(nodes == 0){
            ans++;
        }
    }
}
