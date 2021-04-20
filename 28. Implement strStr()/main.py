#from typing import str

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nedLen = len(needle)
        
        if needle == "":
            return 0
        
        for i in range(0, len(haystack)):
            k = i + nedLen
            if k > len(haystack): #超出长度
                return -1
            
            for j in range(i, k):
                if haystack[j] == needle[j-i]:
                    if j == k -1:
                        return i
                else:
                    break
                
        return -1


testA = "a"
testAA = "a"

if __name__ == "__main__":
    testClass = Solution()
    res = testClass.strStr(testA, testAA)
    print(res)
