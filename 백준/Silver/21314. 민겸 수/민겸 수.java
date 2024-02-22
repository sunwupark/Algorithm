import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        String max_value = "";
        String min_value = "";
        int k =0;
        int length = line.length();

        for(int i =0;i < length; i++){
            if(line.charAt(i) == 'M'){
                k+=1;
                if(i+1 >= length){
                    for(int j = 0; j < k; j++){
                        max_value += "1";
                        if(j == 0){
                            min_value += "1";
                        } else{
                            min_value += "0";
                        }
                    }
                }
            } else{
                max_value += "5";
                for(int j = 0; j < k; j++){
                    max_value += "0";
                    if(j == 0){
                        min_value += "1";
                    } else{
                        min_value += "0";
                    }
                }
                min_value += "5";
                k = 0;
            }
        }
        System.out.println(max_value);
        System.out.println(min_value);
    }
}