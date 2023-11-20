import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException{
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    int s = Integer.parseInt(bufferedReader.readLine());
    for (int i =0; i < s; i++){
      String s1 = bufferedReader.readLine();
      int left = 0;
      for(int j = 0; j < s1.length(); j++){
        if(s1.charAt(j) == '('){
          left+=1;
        } else {
          left-=1;
        }
        if(left < 0){
          System.out.println("NO");
          break;
        }
      }
      if(left > 0)
        System.out.println("NO");
      else if(left == 0){
        System.out.println("YES");
      }
    }

  }
}
