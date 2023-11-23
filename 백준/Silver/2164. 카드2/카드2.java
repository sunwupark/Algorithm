import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
  public static void main(String[] args) throws IOException{
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(bufferedReader.readLine());
    Queue<Integer> num_list = new LinkedList<>();

    for(int i =1; i <= num; i++){
      num_list.add(i);
    }

    int iter = 0;
    while(num_list.size() > 1){
      if(iter % 2 == 0){
        num_list.poll();
      } else{
        num_list.add(num_list.poll());
      }
      iter++;
    }
    System.out.println(num_list.poll());
  }
}
