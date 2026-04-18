class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i< nums.length ; i++){
            map.put(nums[i],i);
        }
        for(int i = 0 ; i< nums.length; i++){
            int objective = target - nums[i];
            if( map.containsKey(objective) && map.get(objective) != i ){
                return new int[]{i, map.get(objective)};
            }
        }
        return new int[0];
    }
}
