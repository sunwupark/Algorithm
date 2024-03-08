import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;
        long integer = 665;
        String temp = "";
        while(count < N){
            integer++;
            temp =String.valueOf(integer);
            if(temp.contains("666")){
                count++;
            }
        }
        System.out.println(temp);
    }
}
