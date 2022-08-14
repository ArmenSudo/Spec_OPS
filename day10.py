# 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            prev = nums[i]
            nums[index] = nums[i]
            index += 1
        return index
      
      
# 2      
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range(m, m+n):
            nums1[x] = nums2[x-m]
        return nums1.sort()
      
# 3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = 0
        dic = {}
        for i in nums:
            if dic.get(i):
                return True
            dic[i] = 1
        return False
      
# 4
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
                
        return seen.pop()
      
# or
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
      
# 5
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums)*(len(nums)+1))/2 - sum(nums))
      
# 6
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        new_arr = []
        string = ''
        for x in nums:
            if x == 1:
                string += "1"
            if x == 0:
                new_arr.append(len(string))
                string = ''
        new_arr.append(len(string))
        return max(new_arr)
      
# 7
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[x] for x in range(0, len(nums), 2)])
      
# 8
def primeFactors(n):
    c = 2
    while n > 1:
        if n % c == 0:
            n /= c
        else:
            c = c + 1
    return c


n = 600851475143
print(primeFactors(n))

# 9


# 10
def primeFactors(n):
    c = 2
    lst = []
    while n > 1:
        if n % c == 0:
            n /= c
            lst.append(c)
        else:
            c = c + 1
    return lst
def prime(num):
    prod = 1
    dic = {}
    while num:
        for i in primeFactors(num):
            dic[i] = max(primeFactors(num).count(i), dic.get(i, 0))
        num -= 1
    for i in dic.keys():
        prod  *= (int(i)**dic[i])
    return prod

print(prime(20))


# 11



# 12
import math


def is_prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


count = 1
i = 3
while True:
    if is_prime(i):
        count += 1
        if count == 10001:
            print(i)
            break
    i += 2
