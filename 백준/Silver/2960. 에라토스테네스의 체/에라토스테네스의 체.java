import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        List<Integer> chae = new ArrayList<>();

        st = new StringTokenizer(br.readLine());

        Integer N = Integer.valueOf(st.nextToken());
        Integer K = Integer.valueOf(st.nextToken());

        for (int i = 2; i <= N; i++) {
            chae.add(i);
        }

        int count = 0;

        while (count < K) {
            Integer i1 = chae.get(0);
            for (int i = 0; i < chae.size(); i++) {
                int num = chae.get(i);
                if (num % i1 == 0) {
                    chae.remove(i);
                    count += 1;
                    if (count == K) {
                        System.out.println(num);
                        return;
                    }

                }
            }
        }
    }
}