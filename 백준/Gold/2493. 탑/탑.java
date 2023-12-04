import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    String[] strings = br.readLine().split(" ");
    List<Integer> num_list = new ArrayList<>();
    Stack<Integer> stk = new Stack<>();

    for(int p = 0; p < N; p++){
      num_list.add(Integer.parseInt(strings[p]));
    }

    for(int i = 0; i < N; i++){
      while(!stk.isEmpty()){
        if(num_list.get(stk.peek()) < num_list.get(i)){
          stk.pop();
        } else{
          break;
        }
      }

      if(stk.isEmpty()){
        System.out.print("0 ");
      } else {
        System.out.print((stk.peek() + 1) + " ");
      }

      stk.push(i);
    }

  }
}