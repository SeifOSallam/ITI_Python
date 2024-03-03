class Solution(object):
    def fizzBuzz(self, n):
        resArr = []
        for i in range(1, n+1):
            res = ""
            if i % 3 == 0:
                res += "Fizz"
            if i % 5 == 0:
                res += "Buzz"
            if res == "":
                res = str(i)
            resArr.append(res)
        return resArr