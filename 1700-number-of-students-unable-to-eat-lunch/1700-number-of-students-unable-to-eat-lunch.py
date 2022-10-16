class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches:
            try:
                idx_students = students.index(sandwiches[0])
                students = students[idx_students+1:] + students[:idx_students]
                del sandwiches[0]
            except:
                return len(sandwiches)
        return 0