/* https://school.programmers.co.kr/learn/courses/30/lessons/42885 */

import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        List<Integer> waitingBoats = new ArrayList(people.length);

        int leftBoats = 0;
        
        for (int i = people.length - 1; i >= 0; i--) {
            Integer w = Integer.valueOf(people[i]);

            if (waitingBoats.isEmpty() || waitingBoats.get(waitingBoats.size() - 1) < w) {
                waitingBoats.add(Integer.valueOf(limit) - w);
            } else {
                waitingBoats.remove(waitingBoats.size() - 1);
                leftBoats += 1;
            }
        }
        
        return leftBoats + waitingBoats.size();
    }
}