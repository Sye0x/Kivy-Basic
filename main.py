def majorityElement( nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if candidate == num:
            count += 1
        else:
            count -= 1

    return candidate
nums=[2,2,1,1,1,3,3]
print(majorityElement(nums))

