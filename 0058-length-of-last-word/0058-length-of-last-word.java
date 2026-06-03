class Solution {

    public int lengthOfLastWord(String s) {

        int i = s.length() - 1;

        // Skip spaces at end
        while(i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        int length = 0;

        // Count last word
        while(i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }

        return length;
    }
}