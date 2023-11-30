import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    String s = bufferedReader.readLine();

    int count = 0;
    int sum = 0;
    for(int i = 0; i < s.length(); i++){
      if(s.charAt(i) == '('){
        count++;
      } else if(s.charAt(i) ==')'){
        if(i-1 >= 0) {
          if (s.charAt(i - 1) == '(') {
            count-=1;
            sum += count;
          }
          else{
            count--;
            sum+=1;
          }
        }
      }
    }
    sum+= count;
    System.out.println(sum);
  }
}
