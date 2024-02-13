import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        String[] inputs = br.readLine().split(" ");

        for(int i =0; i < N; i++){
            arr[i] = Integer.parseInt(inputs[i]);
        }
        
        Arrays.sort(arr);
        int total = 0;

        for(int i =0; i < N; i++){
            if(i>=1) {
                arr[i] = arr[i - 1] + arr[i];
            }
            total += arr[i];
        }

        System.out.println(total);

    }
}
