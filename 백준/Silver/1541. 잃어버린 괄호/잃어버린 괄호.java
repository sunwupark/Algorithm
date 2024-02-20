import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split("-");
        int total = 0;
        for(int i = 0; i < arr.length; i++){
            String[] split = arr[i].split("\\+");
            int sum =0 ;
            for(int j = 0; j < split.length; j++){
                sum += Integer.parseInt(split[j]);
            }
            if(i == 0){
                total = sum;
            } else{
                total -= sum;
            }
        }
        System.out.println(total);

    }
}
