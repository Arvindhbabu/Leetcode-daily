class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        int n =  numCourses;
        int e = prerequisites.length;
        ArrayList AL[] = new ArrayList[n];
        for(int i = 0 ; i< n ; i++){
            AL[i] = new ArrayList();
        }
        Queue q = new LinkedList();
        int inDeg[] = new int[n];
        for(int i = 0 ; i< e ; i++){
            // update the indegree array
            inDeg[prerequisites[i][0]]++;
            AL[prerequisites[i][1]].add(prerequisites[i][0]);
        }
        int counter = 0;
        for(int i = 0 ; i< n ; i++){
            if(inDeg[i] == 0){
                q.add(i);
                counter++;
            }
        }
        // BFS
        while(q.size() != 0 ){
            int sv = (int)q.poll();
            for(int i = 0 ; i < AL[sv].size() ; i++){
                int av = (int)AL[sv].get(i);
                inDeg[av]--;
                if(inDeg[av]== 0 ){
                    q.add(av);
                    counter++;
                }
            }
        }

        if(counter == n){
            return true;
        }
        else {
            return false;
        }


    }
}
