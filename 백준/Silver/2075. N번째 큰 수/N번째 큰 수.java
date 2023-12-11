import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    Integer N = Integer.parseInt(bufferedReader.readLine());
    PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Comparator.reverseOrder());
    for(int i =0; i < N; i++){
        String[] split = bufferedReader.readLine().split(" ");
        for(int j = 0; j < N; j++){
            priorityQueue.add(Integer.parseInt(split[j]));
        }
    }

    for(int i = 0; i < N - 1; i++){
        priorityQueue.poll();
    }
    System.out.println(priorityQueue.poll());
  }
}