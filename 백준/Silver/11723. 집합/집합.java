import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static Set<Integer> arr = new HashSet<>();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        Set<Integer> set = new HashSet<>();

        for (int i = 1; i <= 20; i++) {
            arr.add(i);
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            switch (st.nextToken()){
                case "add":
                    int temp3 = Integer.parseInt(st.nextToken());
                    if(set.contains(temp3)){
                        break;
                    }
                    set.add(temp3);
                    break;
                case "check":
                    int temp = Integer.parseInt(st.nextToken());
                    int result = set.contains(temp) ? 1 : 0;
                    sb.append(result + "\n");
                    break;
                case "remove":
                    set.remove(Integer.parseInt(st.nextToken()));
                    break;
                case "toggle":
                    int temp2 = Integer.parseInt(st.nextToken());
                    if(set.contains(temp2)){
                        set.remove(temp2);
                    } else{
                        set.add(temp2);
                    }
                    break;
                case "all":
                    set.addAll(arr);
                    break;
                case "empty":
                    set.clear();
                    break;
            }
        }

        System.out.println(sb.toString());
    }
}