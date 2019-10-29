class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {"(" : ")", "{" : "}" , "[" : "]"}
        for(i in range(0,s.length)):
            if(len(s)%2 != 0):
                return false
            if()