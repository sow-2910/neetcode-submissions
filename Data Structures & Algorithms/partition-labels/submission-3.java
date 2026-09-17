class Solution {
    public List<Integer> partitionLabels(String s) {
        Map <Character, Integer> frequencies = new HashMap<>();
        for (char c : s.toCharArray()){
            frequencies.put(c, 1 + frequencies.getOrDefault(c, 0));
        }

        List<Integer> result = new ArrayList<>();
        int currentSize = 0;
        HashSet<Character> activeSet = new HashSet<>();

        for (char c : s.toCharArray()){
            activeSet.add(c);
            frequencies.put(c, frequencies.get(c) - 1);
            currentSize += 1;

            if (frequencies.get(c) == 0){
                activeSet.remove(c);
            }

            if (activeSet.isEmpty()){
                result.add(currentSize);
                currentSize =0;
            }
        }
        return result;
    }
}
