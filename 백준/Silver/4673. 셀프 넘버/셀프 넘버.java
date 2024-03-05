
public class Main {
    public static void main(String[] args) {
        int[] dp = new int[10001];

        for (int i = 1; i <= 10000; i++) {
            String temp = String.valueOf(i);
            int notself = i;
            for(int j = 0; j < temp.length(); j++){
                notself += temp.charAt(j) - '0';
            }
            if(notself < 10001)
            dp[notself] = -1;
        }

        for (int i = 1; i < 10000; i++) {
            if(dp[i] != -1){
                System.out.println(i);
            }
        }
    }
}