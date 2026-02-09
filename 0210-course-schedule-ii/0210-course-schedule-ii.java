class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
    
    int n =  numCourses;
        int e = prerequisites.length;
        ArrayList AL[] = new ArrayList[n];
        for(int i = 0 ; i< n ; i++){
            AL[i] = new ArrayList();
        }
        Queue q = new LinkedList();
        int inDeg[] = new int[n];
        for(int i = 0 ; i< e ; i++){ // [[0 , 1], [1 , 0]]
            // update the indegree array
            inDeg[prerequisites[i][0]]++;
            AL[prerequisites[i][1]].add(prerequisites[i][0]);// AL[1].asdd(0)
        }
        int counter = 0;
        for(int i = 0 ; i< n ; i++){
            if(inDeg[i] == 0){
                q.add(i);
                counter++;
            }
        }
        // BFS
        int result[] = new int[n];
        int k = 0;
        while(q.size() != 0 ){
            int sv = (int)q.poll(); // sv 5
            result[k++] = sv;
            for(int i = 0 ; i < AL[sv].size() ; i++){ // 0 ----
                int av = (int)AL[sv].get(i);
                inDeg[av]--;
                if(inDeg[av]== 0 ){
                    q.add(av);
                    counter++;
                }
            }
        }

        if(counter == n){
            return result;
        }
        else {
            return new int[0] ;
        }



    }
        
}
