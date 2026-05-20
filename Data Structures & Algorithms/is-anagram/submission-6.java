class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> CountT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (int i = 0; i < t.length(); i++) {
            CountT.put(t.charAt(i), CountT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return countS.equals(CountT);
    }
}
