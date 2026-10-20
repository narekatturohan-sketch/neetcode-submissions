class Solution {
    public int longestConsecutive(int[] nums) {
        
        if (nums.length == 0 || nums == null) {
            return 0;
        }

        Set<Integer> numSet = new HashSet<>();

        for (int num : nums) {
            numSet.add(num);
        }

        int longStreak = 0;

        for (int num : numSet) {

            if (!numSet.contains(num - 1)) {

                int currentSum = num;
                int currentStreak = 1;

                while (numSet.contains(currentSum + 1)) {

                    currentSum += 1;
                    currentStreak += 1;
                }

                longStreak = Math.max(longStreak, currentStreak);
            }
        }
        return longStreak;
    }
}
