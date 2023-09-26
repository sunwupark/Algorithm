class Solution {
    public int solution(int number, int n, int m) {
        int answer = 0;
        int number1 = number%n;
        int number2 = number%m;
        if(number1==0 && number2==0){
            answer = 1;
        }
        else{
            answer = 0;
        }
        return answer;
    }
}