import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
  public static void main(String[] args) throws IOException {
    PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(
            new Comparator<Integer>() {
              @Override
              public int compare(Integer o1, Integer o2) {
                int absDiff = Integer.compare(Math.abs(o1), Math.abs(o2)); // Compare absolute values in descending order

                if (absDiff != 0) {
                  return absDiff;
                } else {
                  return Integer.compare(o1, o2); // Compare lucky numbers in descending order
                }
              }
            }
    );
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    for(int i =0; i< N; i++){
      Integer s = Integer.parseInt(br.readLine());
      if(s == 0){
        if(priorityQueue.isEmpty()){
          System.out.println(0);
        } else{
          System.out.println(priorityQueue.poll());
        }
      } else{
        priorityQueue.add(s);
      }
    }
  }
}