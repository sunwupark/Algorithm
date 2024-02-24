import java.util.HashMap;
import java.util.Map;

class Solution {
    
    static Map<Integer, Integer> attackInfo = new HashMap<>();
    static int endTime = 0;
    static int curHealth = 0;
    static int successiveTime = 0;
    
    public int solution(int[] bandage, int health, int[][] attacks) {
        curHealth = health;                
        for (int[] attack : attacks) {
            attackInfo.put(attack[0], attack[1]);
            endTime = attack[0];
        }
        
        for(int i = 1; i <= endTime; i++){
            if(attackInfo.containsKey(i)){
                curHealth -= attackInfo.get(i);
                successiveTime = 0;
            
            } else {
                curHealth += bandage[1];
                successiveTime += 1;
                
                if (successiveTime == bandage[0]) {
                    curHealth += bandage[2];
                    successiveTime = 0;
                }
                if (curHealth > health) {
                    curHealth = health;
                }
            }
            
            if (curHealth <= 0) { // 이번 턴을 마치고 체력이 바닥났다면 종료
                return -1;
            }
            
        }
        
        return curHealth;
    }
}