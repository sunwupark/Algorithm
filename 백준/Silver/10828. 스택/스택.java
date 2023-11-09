import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    Stack<Integer> stack = new Stack<Integer>();
    int count = 0;

    for(int i = 0; i < n; i++){
      String input = br.readLine();
      String[] strings = input.split(" ");
      //System.out.println("strings[0] = " + strings[0]);
      switch (strings[0]){
        case "push":
          stack.push(Integer.parseInt(strings[1]));
          count++;
          break;
        case "top":
          if(count == 0){
            System.out.println(-1);
          } else{
            System.out.println(stack.lastElement());
          }
          break;
        case "size":
          System.out.println(count);
          break;
        case "empty":
          if(count == 0){
            System.out.println(1);
          } else{
            System.out.println(0);
          }
          break;
        case "pop":
          if(stack.isEmpty()) {
            System.out.println(-1);
          } else{
            System.out.println(stack.pop());
            count--;          }
          break;
      }
    }
  }
}