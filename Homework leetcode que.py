#Link : https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/submissions/

#Code:

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <=  endTime[i]:
                c += 1
        return c  
