class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int [] count = new int[26];
        for(char sa : s.toCharArray()){
          count[sa - 'a']++;
        }

        for(char ta : t.toCharArray()){
          count[ta-'a']--;
        }

        for(int i = 0; i<count.length;i++){
          if(count[i] !=0) return false;
        }
        return true;
}
}