class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> hashMap = new HashMap<>();

        hashMap.put(')', '(');
        hashMap.put(']', '[');
        hashMap.put('}', '{');

        for(char c : s.toCharArray()){
            if (hashMap.containsKey(c)){
                if(!stack.isEmpty() && stack.peek() == hashMap.get(c)){
                    stack.pop();
                }else{
                    return false;
                }
            }else{
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
