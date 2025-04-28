class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        import numpy as np
        groupSizes = np.array(groupSizes)
        groupIdx = np.arange(len(groupSizes))
        group = np.vstack((groupSizes, groupIdx)).T
        
        group = group[group[:,0].argsort()]     # (n, 2), orderred by groupSizes
        people = []
        i = 0
        while i < len(group):
            size, _ = group[i]
            people.append([idx for _, idx in group[i:i+size]])
            i += size
        return people