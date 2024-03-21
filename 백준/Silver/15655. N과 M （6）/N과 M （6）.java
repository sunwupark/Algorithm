import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int[] arr;
    static boolean[] visited;
    static int[] dp;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N];
        visited = new boolean[N];
        dp = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        for (int i = 0; i < N; i++) {
            dp[0] = arr[i];
            dfs(1);
        }
       // dfs(0);

        System.out.println(sb.toString());
    }

    static void dfs(int count){
        if(count == M){
            for (int i = 0; i < M; i++) {
                //System.out.println("Adding tpo sb " + dp[i] + "  " + i);
                sb.append(dp[i] + " ");
            }
            sb.append("\n");
        } else {
            for (int i = 1; i < N; i++) {
                //System.out.println("i = " + i + " visited " + visited[i] + " dp " + dp[i] + " arr " + arr[i]);
                if (!visited[i] && dp[count - 1] < arr[i]) {
                    visited[i] = true;
                    dp[count] = arr[i];
                    dfs(count + 1);
                    visited[i] = false;
                }
            }
        }
    }
}