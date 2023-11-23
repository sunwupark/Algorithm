import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] s = br.readLine().split(" ");
    int N = Integer.parseInt(s[0]);
    int K = Integer.parseInt(s[1]);

    List<Integer> list = new ArrayList<>();
    for (int i = 1; i <= N; i++) {
      list.add(i);
    }
    String result = "<";

    int iter = 0;
    int count = 0;

    while(!list.isEmpty()){
      if(iter == list.size()){
        iter = 0;
      }
      if(count == K-1){
        Integer num = list.get(iter);
        list.remove(iter);
        if(!list.isEmpty())
          result += num.toString() + ", ";
        else{
          result += num.toString() + ">";
        }
        count = 0;
        continue;
      }
      iter++;
      count++;
    }

    System.out.println(result);
  }
}