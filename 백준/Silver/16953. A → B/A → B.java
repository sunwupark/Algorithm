import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int A = Integer.parseInt(s[0]);
        String B = s[1];
        int temp = Integer.parseInt(B);
        int count =0;

        bfs(count, B, A);

    }
    static void bfs(int count, String B, int A){
        int temp = Integer.parseInt(B);
        int length = B.length();
        if(Integer.parseInt(B) == A){
            System.out.println(count+1);
        } else if(temp < A){
            System.out.println(-1);
        } else if(temp%2 == 0){
            bfs(count+1, String.valueOf(temp/2), A);
        } else if(B.charAt(length-1) == '1'){
            bfs(count+1, B.substring(0, length-1), A);
        } else{
            System.out.println(-1);
        }
    }
}