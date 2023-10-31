class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [pref[0]]
        for i, num in enumerate(pref[1:]):
            result.append(pref[i]^num)
        return result