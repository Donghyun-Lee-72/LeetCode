class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(num: int) -> bool:
            if num == 2:
                return True
            elif num % 2 == 0 or num == 1:
                return False
            
            for i in range(2, (num//2)+1):
                if (num % i) == 0:
                    return False
            return True
        
        def find_prime(diff: int, num: int) -> int:
        # find smallest prime number that is larger than diff and smaller than num
            prime = diff
            while prime < num:
                if is_prime(prime):
                    return prime
                else:
                    prime += 1
            return 0
        
        for i in range(len(nums)-1, 0, -1):
            diff = nums[i-1] - nums[i]
            print(nums[i], nums[i-1], diff)
            
            if diff < 0:
                continue
            else:
                prime = find_prime(diff+1, nums[i-1])
                if prime == 0:
                    return False
                nums[i-1] -= prime
                print(prime)
            print('*'*15)
            
        return True