import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] dist = new int[N-1];
        int[] price= new int [N];
        String[] string_dist = br.readLine().split(" ");
        String[] string_price = br.readLine().split(" ");

        for(int i =0; i < N-1; i++){
            dist[i] = Integer.parseInt(string_dist[i]);
        }

        for(int i =0; i < N; i++){
            price[i] = Integer.parseInt(string_price[i]);
        }

        int curr = 0;
        int distance = 0;
        int sum =0;
        while(distance != N-1){
            sum += price[curr]*dist[distance];
            distance+=1;
            if(price[curr] > price[distance]){
                curr = distance;
            }
        }
        System.out.println(sum);
    }
}