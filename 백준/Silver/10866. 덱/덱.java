import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
  public static void main(String[] args) throws IOException {
    Deque<Integer> deque = new ArrayDeque<>();
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(bufferedReader.readLine());
    for(int i =0; i < num; i++){
      String[] s = bufferedReader.readLine().split(" ");
      switch(s[0]){
        case "push_back":
          deque.addLast(Integer.parseInt(s[1]));
          break;
        case "push_front":
          deque.addFirst(Integer.parseInt(s[1]));
          break;
        case "front":
          if(deque.isEmpty()){
            System.out.println(-1);
          } else {
            System.out.println(deque.peekFirst());
          }
          break;
        case "back":
          if(deque.isEmpty()){
            System.out.println(-1);
          } else {
            System.out.println(deque.peekLast());
          }
          break;
        case "size":
          System.out.println(deque.size());
          break;
        case "pop_front":
          if(deque.isEmpty()){
            System.out.println(-1);
          } else {
            System.out.println(deque.peekFirst());
            deque.removeFirst();
          }
          break;
        case "pop_back":
          if(deque.isEmpty()){
            System.out.println(-1);
          } else {
            System.out.println(deque.getLast());
            deque.removeLast();
          }
          break;
        case "empty":
          if(deque.isEmpty()){
            System.out.println(1);
          } else{
            System.out.println(0);
          }
          break;
      }
    }
  }
}
