class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        students = deque(students)
        sandwiches.reverse()
        cnt = 0
        
        while students and cnt <= len(students):
            
            student = students.popleft()
            
            if student == sandwiches[-1]:
                sandwiches.pop()
                cnt = 0
            else:
                students.append(student)
                cnt += 1
        
        return len(students)