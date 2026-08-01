class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for info in details:
            phone = info[0:10]
            gender = info[10:11]
            age = info[11:13]
            seat = info[13:]
            if int(age) > 60:
                count += 1
        return count

        