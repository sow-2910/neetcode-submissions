class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        Boolean found_first = false;
        Boolean found_second = false;
        Boolean found_last = false;

        for (int[] t: triplets){

            if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]){
                continue;
            }

            if (t[0] == target[0]){
                found_first = true;
            }

            if(t[1] == target[1]){
                found_second = true;
            }

            if(t[2] == target[2]){
                found_last = true;
            }
        }
        return found_first && found_second && found_last;
    }
}
