class Solution:
    def valIncrement(self, idx: int, pair: List[int], interval: List[List[int]]) -> int:
        idx += 1
        if idx < len(interval):
            pair.pop()
            pair.pop()
            pair.append(interval[idx][0])
            pair.append(interval[idx][1])
            return idx
        else:
            return idx
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        if len(firstList) == 0 or len(secondList) == 0:
            return output
        else:
            idx1 = idx2 = 0
            firstPair, secondPair = firstList[idx1], secondList[idx2]
            while idx1 < len(firstList) and idx2 < len(secondList):
                """
                * 1이 먼저 시작
                1이포함: [1,5], [2,3]
                1이먼저: [1,3], [2,5]
                * 2가 먼저 시작
                2가포함: [2,3], [1,5]
                2가먼저: [2,5], [1,3]
                """
                # 1이 먼저 시작
                if firstPair[0] <= secondPair[0] <= firstPair[1]:
                    if firstPair[1] <= secondPair[1]:
                        output.append([secondPair[0],firstPair[1]])
                        idx1 = self.valIncrement(idx1, firstPair, firstList)
                    else:
                        output.append([secondPair[0],secondPair[1]])
                        idx2 = self.valIncrement(idx2, secondPair, secondList)
                # 2가 먼저 시작
                elif secondPair[0] <= firstPair[0] <= secondPair[1]:
                    if secondPair[1] <= firstPair[1]:
                        output.append([firstPair[0],secondPair[1]])
                        idx2 = self.valIncrement(idx2, secondPair, secondList)
                    else:
                        output.append([firstPair[0],firstPair[1]])
                        idx1 = self.valIncrement(idx1, firstPair, firstList)
                else:
                    if firstPair[1] < secondPair[0]:
                        idx1 = self.valIncrement(idx1, firstPair, firstList)
                    elif secondPair[1] < firstPair[0]:
                        idx2 = self.valIncrement(idx2, secondPair, secondList)
            return output