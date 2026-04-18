class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[][] Array = new int[nums.length][2];
        for(int i = 0; i< nums.length;i++){
            Array[i][0] = nums[i];
            Array[i][1] = i;
        }
        Arrays.sort(Array, Comparator.comparingInt(a -> a[0]));
        int i = 0, j = nums.length - 1;
        while(i<j){
            int cur = Array[i][0] + Array[j][0];
            if(cur == target){
                return new int[]{Math.min(Array[i][1],Array[j][1]),Math.max(Array[i][1],Array[j][1])};
            }else if (cur < target){
                i++;
            }else{
                j--;
            }
        }
        return new int[0];
    }
}
