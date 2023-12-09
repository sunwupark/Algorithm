import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    String[] s = bufferedReader.readLine().split(" ");
    List<String> list = new ArrayList<>();
    int N = Integer.parseInt(s[0]);
    int M = Integer.parseInt(s[1]);
    int count = 0;
    for(int i =0; i< N; i++){
        list.add(bufferedReader.readLine());
    }
    for(int j = 0; j < M; j++){
      String s1 = bufferedReader.readLine();
      if(list.contains(s1)){
        count++;
      }
    }
    System.out.println(count);
  }
}
