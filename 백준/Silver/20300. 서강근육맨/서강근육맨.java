import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] arr = new long [N];
        String[] input = br.readLine().split(" ");

        for(int i =0; i < N; i++){
            arr[i] = Long.parseLong(input[i]);
        }

        Arrays.sort(arr);

        long max = 0;
        if(N%2 == 1){
            max = arr[N-1];
            for(int i =0; i < N/2; i++){
                long temp =  arr[i] + arr[N-2-i];
                max = Math.max(temp, max);
            }
        } else{
            for(int i =0; i < N/2; i++){
//                System.out.println("arr[i] = " + arr[i] + " arr[N-1-i] " + arr[N-1-i]);
                long temp =  arr[i] + arr[N-1-i];
                max = Math.max(temp, max);
            }
        }

        System.out.println(max);
    }
}