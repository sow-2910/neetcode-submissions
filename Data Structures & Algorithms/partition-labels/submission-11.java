class Solution {
    public List<Integer> partitionLabels(String s) {
        Map<Character, Integer> hashMap = new HashMap<>();

        for(char c: s.toCharArray()){
            hashMap.put(c, 1 + hashMap.getOrDefault(c, 0));
        }

        int currentSize = 0;
        List<Integer> result = new ArrayList<>();
        HashSet<Character> hashSet = new HashSet<>();

        for(char c: s.toCharArray()){
            hashSet.add(c);
            hashMap.put(c, hashMap.get(c) - 1);
            currentSize++;

            if (hashMap.get(c) == 0){
                hashSet.remove(c);
            }

            if(hashSet.isEmpty()){
                result.add(currentSize);
                currentSize = 0;
            }
        }
        return result;
    }
}
