class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = sum(nums[1:])
        answer = []
        
        for leftNum, rightNum in zip(nums[:-1], nums[1:]):
            answer.append(abs(leftSum - rightSum))
            leftSum += leftNum
            rightSum -= rightNum
        
        answer.append(abs(leftSum - rightSum))
        return answer