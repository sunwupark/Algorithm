import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] strings = br.readLine().split(" ");
    HashMap<String, String> hashMap = new HashMap<>();
    int N = Integer.parseInt(strings[0]);
    int M = Integer.parseInt(strings[1]);
    for(int i = 0; i < N; i++){
      String s = br.readLine();
      hashMap.put(s, String.valueOf(i+1));
      hashMap.put(String.valueOf(i+1), s);
    }

    for(int j = 0; j < M; j++){
      String s = br.readLine();
      String s1 = hashMap.get(s);
      System.out.println(s1);
    }
  }
}
