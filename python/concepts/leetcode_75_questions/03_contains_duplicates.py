# contains duplicates
# gadrion - 03/04/2022

# Pythonic solution
def containsduplicate(nums):
    return len(nums) > len(set(nums))

# Youtube solution
def containsduplicate(nums):
    if len(nums) > len(set(nums)):
        return True
    return False
