import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    Integer N = Integer.parseInt(bufferedReader.readLine());
    PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
    for(int i = 0;  i < N; i++){
      int parseInt = Integer.parseInt(bufferedReader.readLine());
        if(parseInt == 0){
            if(priorityQueue.isEmpty()){
                System.out.println(0);
            } else {
                System.out.println(priorityQueue.poll());
            }
        } else {
            priorityQueue.add(parseInt);
        }
    }
  }
}
