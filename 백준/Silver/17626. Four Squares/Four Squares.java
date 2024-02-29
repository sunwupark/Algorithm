import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[50001];

        for(int i = 1; i <= N; i++){
            int num = (int) Math.sqrt(i);
            int subtract = i - num*num;
            if(subtract == 0){
                arr[i] = 1;
            } else{
                arr[i] = arr[i-1] + 1;
                for(int j = num; j >= 1; j--){
                    arr[i] = Math.min(arr[i], arr[i - j*j] + 1);
                }
            }
            //System.out.println("i: " + i + " num: " + num + " subtract = " + subtract + " arr: " + arr[i]);
        }

        System.out.println(arr[N]);
    }
}