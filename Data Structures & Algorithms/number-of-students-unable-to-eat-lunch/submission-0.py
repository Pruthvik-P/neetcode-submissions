class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n

        for sw in sandwiches:
            count = 0
            while count < n and q[0] != sw:
                curr = q.popleft()
                q.append(curr)
                count += 1

            if q[0] == sw:
                q.popleft()
                res -= 1
            else:
                break

        return res