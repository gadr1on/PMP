# two sum 
# gadrion - 03/04/2022

def twoSum(nums, target):
    track = {}
    for i in range(len(nums)):
        diff = target - nums[i] 
        if diff in track:
            return [track[diff], i]
        track[nums[i]] = i
    return
