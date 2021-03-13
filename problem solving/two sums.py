class Solution:
    def two_sums(self, list, target):
        for i, a in enumerate(list):
            for j, b in enumerate(list):
                if a + b == target:
                    return i, j

        print("not here")


solution = Solution()
listt = [3, 2, 4, 9]
print(solution.two_sums(listt, 5))
