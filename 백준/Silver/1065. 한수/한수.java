import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] dp = new int [10001];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int count = 0;

        if(N < 100){
            count = N;
        } else{
            count = 99;
            for (int i = 111; i <= N; i++) {
                String temp = String.valueOf(i);
                if((temp.charAt(1) - temp.charAt(0)) == (temp.charAt(2) - temp.charAt(1))){
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
