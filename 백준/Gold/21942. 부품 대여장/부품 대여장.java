import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, LocalDateTime> hashMap = new HashMap<>();
        TreeMap<String, Long> result = new TreeMap<>();

        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        int D = Integer.parseInt(s[1].split("/")[0]);
        int h = Integer.parseInt(s[1].split("/")[1].split(":")[0]);
        int m = Integer.parseInt(s[1].split("/")[1].split(":")[1]);
        int F = Integer.parseInt(s[2]);

        while (N-- > 0) {
            String[] command = br.readLine().split(" ");
            if (command.length < 4) {
                continue; // 입력 형식 오류인 경우 다음 입력으로 넘어갑니다.
            }
            String name = command[2] + "_" + command[3];
            String[] date = command[0].split("-");
            String[] date2 = command[1].split(":");

            LocalDateTime todayDate;
            if (!hashMap.containsKey(name)) {
                todayDate = LocalDateTime.of(Integer.parseInt(date[0]), Integer.parseInt(date[1]), Integer.parseInt(date[2]), Integer.parseInt(date2[0]), Integer.parseInt(date2[1]));
                todayDate = todayDate.plusDays(D).plusHours(h).plusMinutes(m);
                hashMap.put(name, todayDate);
            } else {
                todayDate = LocalDateTime.of(Integer.parseInt(date[0]), Integer.parseInt(date[1]), Integer.parseInt(date[2]), Integer.parseInt(date2[0]), Integer.parseInt(date2[1]));
                LocalDateTime inputDate = hashMap.getOrDefault(name, LocalDateTime.now());
                if (todayDate.compareTo(inputDate) > 0) {
                    Duration duration = Duration.between(inputDate, todayDate);
                    long minutes = duration.toMinutes() * F;
                    long current = 0;
                    current = result.getOrDefault(command[3], current);
                    result.put(command[3], minutes + current);
                }
                hashMap.remove(name);
            }
        }

        if (result.isEmpty()) {
            System.out.println(-1);
        }
        for (String keys : result.keySet()) {
            System.out.println(keys + " " + result.getOrDefault(keys, 0L));
        }
        result.clear();
    }
}