# contains duplicates
# gadrion - 03/04/2022

# Pythonic solution
def containsduplicate(nums):
    if len(nums) > len(set(nums)):
        return True
    return False

# Youtube solution
def containsduplicate(nums):
    if len(nums) > len(set(nums)):
        return True
    return False
