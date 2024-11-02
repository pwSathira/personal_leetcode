class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int sLength = s.length();
        
        //Only have to check till middle, therefore n/2
        for (int i = 0; i < sLength/2; i++){
            if (s.charAt(i) != s.charAt(sLength-i-1)){
                return false;
            }
        }
        return true;
    }
}