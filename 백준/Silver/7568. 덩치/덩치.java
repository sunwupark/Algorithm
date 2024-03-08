import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][3];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int[] result = new int[N];
        for(int i = 0; i < N; i++){
            int higher = 0;
            for(int j=0; j < N; j++){
                if(arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]){
                    higher++;
                }
            }
            result[i] = higher+1;
        }

        for (int i = 0; i < N; i++) {
            if(i < N-1){
                System.out.print(result[i] + " ");
            } else{
                System.out.println(result[i]);
            }
        }
    }
}