class Solution {
    public int solution(int num, int n) {
        int answer = 0;
        int number = num%n;
        answer = Integer.toString(number).equals("0") ? 1 : 0;
        return answer;
    }
}