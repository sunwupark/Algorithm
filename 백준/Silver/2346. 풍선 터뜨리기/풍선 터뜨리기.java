import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int i = Integer.parseInt(br.readLine());
    String[] inputArray = br.readLine().split(" ");
    List<String> inputs = new ArrayList<>(Arrays.asList(inputArray));
    List<Integer> mem = new ArrayList<>();
    List<Integer> result = new ArrayList<>();
    for (int j = 0; j < i; j++) {
      mem.add(j);
    }

    int iter = 0;
    int input = 0;
    for(int j = 0; j< i; j++){
      input = Integer.parseInt(inputs.get(iter));
      result.add(mem.get(iter)+1);
      if(result.size() == i){
        for (int l = 0; l < result.size(); l++) {
          if(l == result.size()-1){
            System.out.println(result.get(l));
            return;
          }
          System.out.print(result.get(l) + " ");
        }
        return;
      }
      inputs.remove(iter);
      mem.remove(iter);
      if(input > 0){
        iter = iter+input-1;
      } else {
        iter += input;
      }

      while(iter < 0 || iter >= inputs.size()){
        if(iter < 0){
          iter = inputs.size() + iter;
        } else if(iter >= inputs.size()){
          iter = iter -  inputs.size();
        }
      }
    }
  }
}
