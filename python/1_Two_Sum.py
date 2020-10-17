# 96%
# hashmap(dictionary) solution

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
      dic = {}
      for i, num in enumerate(nums):
         if num in dic:
            return [dic[num], i]
         dic[target-num] = i
         
# Note!!!!!!!!
# Using function "enumerate"(returns a generator) make it faster
