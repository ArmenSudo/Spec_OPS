# 1
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        new_arr = []
        if target[-1] < n:
            n = target[-1]
        for x in range(1, n+1):
            if x in target:
                new_arr.append("Push")
            else:
                new_arr.append("Push")
                new_arr.append("Pop")
        return new_arr

# 2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1 & nums2

# 3
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_set = set(nums)
        dic = {x:nums.count(x) for x in nums_set}
        # dic = {}
        # for x in nums_set:
            # dic[x] = nums.count(x)
        sizes = []
        max_numb = max(dic.values())
        for key, val in dic.items():
            if val == max_numb:
                sizes.append(len(nums) - nums[::-1].index(key) - nums.index(key))
        return min(sizes)
    
    
class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

    
# 4
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index = 0
        for ind, val in enumerate(nums):
            if val % 2 == 0:
                nums[index], nums[ind] = nums[ind], nums[index]
                index += 1
        return nums
    
 

# 5
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sumar = 0
        for x in nums_set:
            if nums.count(x) == 1:
                sumar += x
        return sumar

# 6
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0
        else:
            try:
                return haystack.index(needle)
            except:
                return -1

# 7
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

# 8
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for x in s:
            if x.isalnum():
                new_s += x.lower()

        return new_s[::] == new_s[::-1]

# 9
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()
        for x in emails:
            if '+' in x:
                unique_email.add(''.join([i for i in x[:x.index('+')]if i != '.'])+x[x.index("@"):])
            else:
                unique_email.add(''.join([i for i in x[:x.index('@')] if i != '.']) + x[x.index("@"):])

        return len(unique_email)

# 10
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), len(nums) - nums[::-1].index(target)-1]
        except:
            return [-1, -1]
