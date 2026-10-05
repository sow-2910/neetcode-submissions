class Solution {
    private Map <Integer, List<Integer>> preMap = new HashMap<>();

    private Set<Integer> visited = new HashSet<>();

    private Set<Integer> visiting = new HashSet<>();

    private List<Integer> output = new ArrayList<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++) {
            preMap.put(i, new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            preMap.get(pre[0]).add(pre[1]);
        }

        for (int c = 0; c < numCourses; c++) {
            if (!dfs(c)) {
                return new int[0];
            }
        }

        int[] result = new int[numCourses];
        for(int i = 0; i < numCourses; i++){
            result[i] = output.get(i);
        }
        return result;
    }

    private boolean dfs(int c){
        if (visiting.contains(c)){
            return false;
        }

        if (visited.contains(c)){
            return true;
        }

        visiting.add(c);

        for (int pre: preMap.get(c)){
            if (!dfs(pre)){
                return false;
            }
        }
        visiting.remove(c);
        visited.add(c);
        output.add(c);
        return true;
    }
}
