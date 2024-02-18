import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        String arr = br.readLine();

        int total = 0;

        int B = 0;
        int R = 0;

        char previous = 'n';
        for(int i = 0; i < N; i++){
            char curr = arr.charAt(i);
            if((previous == 'R' && curr == 'B') || ((curr == 'R') && (i+1 == N))){
                R+=1;
            }
            if((previous == 'B' && curr == 'R') || ((curr == 'B') && (i+1 == N))){
                B+=1;
            }
            previous = curr;
        }

        if(R>B){
            total = B+1;
        } else{
            total = R+1;
        }

        System.out.println(total);
    }
}