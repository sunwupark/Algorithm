import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static boolean[] visited;

    static int[][] arr;

    static int min = 1000000000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        arr = new int[N][2];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= N; i++) {
            combination(new int[N], new boolean[N], 0, N, i, 1, 0);
        }

        System.out.println(min);

    }

    static void combination(int[] arr2, boolean[] visited, int start, int n, int r, int S, int B) {
        if(r == 0) {
            if(Math.abs(S-B) < min){
                min = Math.abs(S-B);
            }
            return;
        }

        for(int i=start; i<n; i++) {
            visited[i] = true;
            combination(arr2, visited, i + 1, n, r - 1, S*arr[i][0], B+arr[i][1]);
            visited[i] = false;
        }
    }
}