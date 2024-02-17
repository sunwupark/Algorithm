import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        Integer[] arr = new Integer[N];
        String[] arr2 = br.readLine().split(" ");
        int max_value = 0;

        for(int i =0; i < N; i++){
            arr[i] = Integer.parseInt(arr2[i]);
            if(arr[i] >  max_value){
                max_value = arr[i];
            }
        }

        double total = max_value;

        for(int i =0; i < N; i++){
            if(arr[i] != max_value){
                total += (double) arr[i]/2;
            }
        }

        System.out.println(total);
    }
}
