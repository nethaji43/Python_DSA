def lc217(nums):
    length_list = len(nums)
    Set = set(nums)
    convert_set = list(Set)
    Length_convered = len(convert_set)
    if length_list == Length_convered:
        return bool(0)
    else:
        return bool(1)

print(lc217([1,2,3,4,5,6,7,8,9,1,2,3]))