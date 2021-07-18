class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        String s[] = text.split(" ");
        char ch[] = brokenLetters.toCharArray();
        boolean flag = true;
        int count = 0;
        for(String str : s)
        {
            flag = true;
            for(char c : ch)
            {
                if(str.indexOf(c)!=-1)
                {
                    flag = false;
                    break;
                }
            }
            if(flag == true)
                count++;
        }
        
        return count;
    }
}