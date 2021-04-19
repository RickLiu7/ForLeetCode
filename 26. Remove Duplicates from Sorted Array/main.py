from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            for k in range(len(nums)-1,i,-1):
                if (nums[k] == nums[i]):
                    del nums[k]
            i+=1
        return len(nums)


test1 = [0,0,0,0,0,0,0,0,0,0]
test2 = [0,1,2,3,4,5,6,7,8,9]
test3 = [0,0,1,1,2,2,3,3,4,4]

if __name__ == "__main__":
    testArray = test1
    test = Solution()
    test.removeDuplicates(testArray)
    print(testArray)
