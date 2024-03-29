import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        int sum = 64;
        int count = 6;
        int smallest = 64;
        int[] arr = new int[7];
        arr[6] = 1;

        while(sum >= X){
            if(sum == X){
                int total = 0;
                for (int i = 0; i < 7; i++) {
                    total += arr[i];
                }
                System.out.println(total);
                break;
            }
            if(count == 0){
                break;
            }
            smallest /= 2;
            arr[count] -= 1;
            if(sum - smallest >= X){
                sum = sum-smallest;
                arr[count-1] += 1;
            } else{
                arr[count-1] += 2;
            }
            count-=1;
        }
    }
}