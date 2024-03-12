import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int N;
    static int M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] arr= br.readLine().split(" ");
        N = Integer.parseInt(arr[0]);
        M = Integer.parseInt(arr[1]);

        dfs("", 0);


    }

    static void dfs(String arr, int count){
        if(count == M){
            System.out.println(arr.substring(1));
        } else{
            for (int i = 1; i <= N; i++) {
                if(!arr.contains(String.valueOf(i)))
                    dfs(arr + " " + i, count+1);
            }
        }
    }
}