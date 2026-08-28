class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        currSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1]
            if (currSum / k) >= threshold:
                result += 1
            currSum -= arr[L]

        return result