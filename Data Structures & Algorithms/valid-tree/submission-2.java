class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length > n){
            return false;
        }

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }

        for (int []edge : edges){
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visit = new HashSet<>();

        if (!dfs(0, -1, visit, adj)){
            return false;
        }

        return visit.size() == n;
    }


    private boolean dfs(int currentNode, int parentNode, Set<Integer> visit, List<List<Integer>> adj){
        if (visit.contains(currentNode)){
            return false;
        }

        visit.add(currentNode);
        for(int nei: adj.get(currentNode)){
            if (nei == parentNode){
                continue;
            }

            if (!dfs(nei, currentNode, visit, adj)){
                return false;
            }
        }
        return true;
    }
}
