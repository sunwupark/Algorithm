import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] dp = new int[N];
        int count = 0;
        int max = -100000000;

        while(st.hasMoreElements()){
            int temp = Integer.parseInt(st.nextToken());
            if(count == 0){
                dp[count] = temp;
            } else{
                dp[count] = Math.max(dp[count-1] + temp, temp);
            }

            if(dp[count] > max){
                max = dp[count];
            }
            count++;
        }

        System.out.println(max);
    }
}