class Solution {

    public static void RecursiveUtility(String str , int op , 
                              int cp , int n , List<String> result){
            if(op == n && cp == n){
                result.add(str);

            }
            if(op < n){
                    RecursiveUtility(str + "(" , op + 1 , cp , n , result);
            }
            if(cp < op){
                    RecursiveUtility(str + ")" , op , cp + 1 , n , result);
                
            }

    }
        
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        RecursiveUtility("" , 0 , 0 , n , result);
        return result;
        
    }
}