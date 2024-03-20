import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);

        dfs("", 0, 0);


    }

    static void dfs(String str, int last, int count){
        if(count == M){
            System.out.println(str.substring(1));
            return;
        } else{
            for (int i = 1; i <= N; i++) {
                if(i >= last) {
                    dfs(str + " " + i, i, count + 1);
                }
            }
        }
    }
}