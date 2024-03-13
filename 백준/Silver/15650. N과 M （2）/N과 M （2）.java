import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int M;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        bfs("", 0, 0);


    }

    static void bfs(String str, int count, int last){
        if(count == M){
            System.out.println(str.substring(1));
        } else{
            for (int i = 1; i <= N; i++) {
                if(last < i){
                    bfs(str + " " + i, count+1, i);
                }
            }
        }
    }
}
