import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    List<String> list = new ArrayList<>();
    Stack<Integer> stack = new Stack<>();
    int n = Integer.parseInt(br.readLine());
    int last_input = 0;
    for(int i =0; i < n; i++){
      int k = Integer.parseInt(br.readLine());
      if(k > last_input){
        for(int j =last_input+1; j <= k; j++){
          stack.push(j);
          list.add("+");
        }
        last_input = k;
        stack.pop();
        list.add("-");
      } else if(k < last_input){
        if(stack.isEmpty()){
          System.out.println("NO");
          return;
        }
        while(!stack.isEmpty()){
          int pop_element = stack.pop();
          list.add("-");
          if(pop_element == k){
            break;
          }
        }
      }
    }
    for (String s : list) {
      System.out.println(s);
    }
  }
}
