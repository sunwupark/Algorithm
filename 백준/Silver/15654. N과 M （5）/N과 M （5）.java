import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int[] arr;
    static int[] dp;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        
        arr = new int[N];
        visited = new boolean[N];
        dp = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        dfs(0);

        System.out.println(sb.toString());

    }

    static void dfs(int count){
        if(count == M){
            for (int i = 0; i < M; i++) {
                sb.append(dp[i]).append(" ");
            }
            sb.append("\n");
            return;
        } else {
            for (int i = 0; i < N; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    dp[count] = arr[i];
                    dfs(count + 1);
                    visited[i] = false;
                }
            }
        }
    }
}