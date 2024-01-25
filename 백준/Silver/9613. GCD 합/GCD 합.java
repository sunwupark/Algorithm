import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Integer t = Integer.valueOf(br.readLine());

        for(int i =0; i < t; i++){
            st = new StringTokenizer(br.readLine());
            Integer n = Integer.valueOf(st.nextToken());
            int[] arr = new int[n];
            for(int j = 0; j < n; j++){
                Integer temp = Integer.valueOf(st.nextToken());
                arr[j] = temp;
            }

            long sum =0;
            for(int k = 0; k < n; k++){
                for(int p = k+1; p < n; p++){
                    if(arr[k] > arr[p]){
                        sum += gcd(arr[k], arr[p]);
                    } else{
                        sum += gcd(arr[p], arr[k]);
                    }
                }
            }
            System.out.println(sum);
        }
    }

    static long gcd(Integer a, Integer b){
        if(b == 0){
            return a;
        }
        return gcd(b,a%b);
    }
}
