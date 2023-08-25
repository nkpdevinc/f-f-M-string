
'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.


'''

import random

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        
        while True:
            random.shuffle(chars)
            
            for i in range(len(chars) - 1):
                if chars[i] == chars[i + 1]:
                    break
            else:
                break
        
        rearranged_string = ''.join(chars)
        return rearranged_string



if __name__ == "__main__":
    s = "aсab"
    sol= Solution()
    result = sol.reorganizeString(s)
    print(result)
