class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        
        // Step 1 is to create adjacency list using map and priority queue
        Map<String , PriorityQueue<String>> AL = new HashMap<>();
        // step 2 fill the adjacency list
        for(List<String> list : tickets){
            String from = list.get(0);
            String to = list.get(1);
            AL.computeIfAbsent(from ,temp->new PriorityQueue<>()).add(to);

        }
        // now use a stack and do DFS
        LinkedList<String> stack = new LinkedList<>();
        LinkedList<String> result = new LinkedList<>();
        stack.add("JFK"); // starting city is JFK
        while(!stack.isEmpty()){
           
            while(AL.containsKey(stack.peekLast())&& !AL.get(stack.peekLast()).isEmpty()){ 
                // check the adjacency list of string picked if it is not empty
                // Go deeper into lexographicall smallest destination
               
                stack.add(AL.get(stack.peekLast()).poll());
                

            }
            // add the city in the result list
                result.addFirst(stack.pollLast());

        }

    return result;
        
    }
}
