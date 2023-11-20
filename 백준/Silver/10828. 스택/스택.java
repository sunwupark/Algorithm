import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
  public static void main(String[] args) throws IOException {
    Stack stack = new Stack();

    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    Integer N = Integer.parseInt(bufferedReader.readLine());

    for(int i = 0; i < N; i++){
      String[] strings = bufferedReader.readLine().split(" ");
      switch(strings[0]){
        case "push":
          stack.push(strings[1]);
          break;
        case "top":
          if(stack.isEmpty()){
            System.out.println(-1);
          } else {
            System.out.println(stack.lastElement());
          }
          break;
        case "size":
          System.out.println(stack.size());
          break;
        case "empty":
          if(stack.isEmpty()){
            System.out.println(1);
          } else{
            System.out.println(0);
          }
          break;
        case "pop":
          if(stack.isEmpty()){
            System.out.println(-1);
          } else{
            System.out.println(stack.pop());
          }
          break;
      }
    }

  }
}
