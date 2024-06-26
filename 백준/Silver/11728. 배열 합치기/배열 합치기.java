import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        int[] B = new int[M];
        int aPointer = 0;
        int bPointer = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }


        while(aPointer < N && bPointer < M){
            if(A[aPointer] < B[bPointer]){
                sb.append(A[aPointer] + " ");
                aPointer++;
            } else{
                sb.append(B[bPointer] + " ");
                bPointer++;
            }
        }

        if(aPointer == N){
            for (int i = bPointer; i < M; i++) {
                sb.append(B[i] + " ");
            }
        } else{
            for (int i = aPointer; i < N; i++) {
                sb.append(A[i] + " ");
            }
        }

        System.out.println(sb.toString());

    }
}