import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    int total = Integer.parseInt(bufferedReader.readLine());
    for(int i = 0; i< total; i++){
      String[] strings = bufferedReader.readLine().split(" ");
      int M = Integer.parseInt(strings[1]);

      String[] importance = bufferedReader.readLine().split(" ");
      Deque<Integer> queue = new ArrayDeque<>();
      Deque<Integer> queue2 = new ArrayDeque<>();
      for(int j = 0; j < importance.length; j++){
        queue.add(Integer.parseInt(importance[j]));
        queue2.add(j);
      }
      int count =0;
      while(!queue.isEmpty()){
        Integer max = queue.stream().max(Integer::compareTo).orElse(0);
        if(queue.getFirst() >= max){
          if(queue2.getFirst() == M){
            count +=1;
            System.out.println(count);
            break;
          }
          queue.removeFirst();
          queue2.removeFirst();
          count++;

        } else{
          Integer first = queue.getFirst();
          queue.addLast(first);
          queue.removeFirst();
          Integer second = queue2.getFirst();
          queue2.addLast(second);
          queue2.removeFirst();
        }
      }
    }
  }
}
