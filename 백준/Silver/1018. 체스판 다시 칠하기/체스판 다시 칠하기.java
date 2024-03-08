import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int M;
    static boolean[][] arr;
    static List<Integer> result = new ArrayList<>();

    public static  int min = 64;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String inputs = br.readLine();
            for(int j = 0; j < M; j++){
                if(inputs.charAt(j) == 'B'){
                    arr[i][j] = true;
                } else{
                    arr[i][j] = false;
                }
            }
        }


        for(int i = 0; i < N-7; i++){
            for(int j = 0; j < M-7; j++){
                find(i, j);
            }
        }

        System.out.println(min);
    }

    static void find(int i, int j) {
        int count = 0;
        boolean start = arr[i][j];
        for (int k = i; k < i + 8; k++) {
            for (int l = j; l < j + 8; l++) {

                if (start != arr[k][l]) {
                    count++;
                }
                start = !start;

            }
            start = !start;
        }

        count = Math.min(count, 64 - count);

        /*
         * 이전까지의 경우 중 최솟값보다 현재 count 값이
         * 더 작을 경우 최솟값을 갱신
         */
        min = Math.min(min, count);
    }
}
