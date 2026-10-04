class Solution {
    private Map<Integer, List<Integer>> preqMap = new HashMap<>(); 

    private Set<Integer> visiting = new HashSet<>();
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++){
            preqMap.put(i, new ArrayList<>());
        }

        for (int[] preq: prerequisites){
            preqMap.get(preq[0]).add(preq[1]);
        }

        for (int c = 0; c < numCourses; c++){
            if(!dfs(c)){
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int c){
        if (visiting.contains(c)){
            return false;
        }

        if (preqMap.get(c).isEmpty()){
            return true;
        }

        visiting.add(c);
        for(int pre : preqMap.get(c)){
            if (!dfs(pre)){
                return false;
            }
        }
        visiting.remove(c);
        preqMap.put(c, new ArrayList<>());
        return true;
    }
}
