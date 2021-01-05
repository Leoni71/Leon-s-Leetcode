class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0){
            return "";
        }
        int shortest_len = strs[0].length();
        String result = "";
        String shortest = strs[0];
        for(int i=1;i<strs.length;i++){
            if(strs[i].length() < shortest_len){
                shortest_len = strs[i].length();
                shortest = strs[i];
            }
        }
        
        for(int i=0;i<shortest_len;i++){
            for(int j=0;j<strs.length;j++){
                if(strs[j].charAt(i)!=shortest.charAt(i)){
                    return result;
                }
            }
            result += shortest.charAt(i);
        }
        return result;
        
    }
}

# Vertical Scanning
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        for (int i = 0; i < strs[0].length() ; i++){
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j ++) {
                if (i == strs[j].length() || strs[j].charAt(i) != c)
                    return strs[0].substring(0, i);             
            }
        }
        return strs[0];
        
    }
}
