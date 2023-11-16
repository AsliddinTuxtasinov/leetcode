from typing import List
    
def containsDuplicate(nums: List[int]) -> bool:
    if len(set(nums)) != len(nums):
        return True
    return False


nums: List[int] = [1,1,1,3,3,4,3,2,4,2]
print(f"Solution: {containsDuplicate(nums=nums)}")