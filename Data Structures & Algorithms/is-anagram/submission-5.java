class Solution {
    public boolean isAnagram(String s, String t) {
        char[] char_s = s.toCharArray();
        char[] char_t = t.toCharArray();
        Arrays.sort(char_s);
        Arrays.sort(char_t);
        if(char_s.length != char_t.length){
            return false;
        }
        for(int i = 0; i < char_s.length;i++){
            if(char_s[i] != char_t[i]){
                return false;
            }
        }
        return true;
    }
}
