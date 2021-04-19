from typing import List

#class Solution:
#    def removeElement(self, nums: List[int], val: int) -> int:
#        for i in range(len(nums) - 1, -1, -1):
#            if (nums[i] == val):
#                del nums[i]
#        return len(nums)
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0

        while i <= j:
            if (nums[i] == val):
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
            else:
                i+=1
        return j+1
        

    
            
        
test1 = [1,2,3,4,5,6,7,8]
test2 = [1,1,2,2,3,3,4,4]
test3 = [0,0,0,0,0,0,0,0]

if __name__ == "__main__":
    testArray = test3
    testNum = 0
    
    testClass = Solution()
    res = testClass.removeElement(testArray,testNum)
    print(testArray)
    print(res)
