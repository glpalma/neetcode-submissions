class Solution {
    public int lengthOfLastWord(String s) {
        int right = -1;
        char curr;

        for (int i = s.length() - 1; i >= 0; i--) {
            curr = s.charAt(i);

            if (right == -1 && curr != ' ') {
                right = i;
            }
            if (right != -1) { // chegou na esquerda
                if (curr == ' ') {
                    return right - i;
                } else if (i == 0) {
                    return right - i + 1;
                }
            }
        }
        return -1;
    }
}