import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.HashMap;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    HashMap<String, Integer> hashMap = new HashMap<>();
    int count = 0;
    while(true){
      String line = bufferedReader.readLine();
      if(line == null || line.isEmpty()){
        break;
      }
      hashMap.put(line, hashMap.getOrDefault(line, 0) + 1);
      count++;
    }
    StringBuilder stringBuilder = new StringBuilder();
    int finalCount = count;
    hashMap.keySet().stream().sorted().forEach(key -> {
      stringBuilder.append(key).append(" ").append(String.format("%.4f", (double) hashMap.get(key) / finalCount * 100)).append("\n");
    });
    System.out.println(stringBuilder.toString());

  }
}
