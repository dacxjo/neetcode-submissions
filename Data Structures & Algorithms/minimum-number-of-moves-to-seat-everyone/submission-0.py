class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sorted = sorted(seats)
        sorted_students = sorted(students)
        result = 0
        for i in range(len(seats_sorted)):
            result += abs(sorted_students[i] - seats_sorted[i])
        return result



        