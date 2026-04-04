class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() == 0 || t.length() == 0 || s.length()!=t.length()) return false;
        char[] sa = s.toCharArray();
        char[] ta = t.toCharArray();

        HashMap<Character,Integer> map1 = new HashMap<>();
        HashMap<Character,Integer> map2 = new HashMap<>();
        for(int i = 0;i<s.length();i++){
            if(!map1.containsKey(sa[i])){
                map1.put(sa[i],1);
            }else{
                map1.put(sa[i],map1.get(sa[i])+1);
            }
            
            if(!map2.containsKey(ta[i])){
                map2.put(ta[i],1);
            }else{
                map2.put(ta[i],map2.get(ta[i])+1);
            }
        }
        if(map1.equals(map2)){
            return true;
        }else{
            return false;
        }

    }
}
