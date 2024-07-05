def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None
    
    def recursive_find_peak(nums, left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            return recursive_find_peak(nums, mid + 1, right)
        elif nums[mid] < nums[mid - 1]:
            return recursive_find_peak(nums, left, mid - 1)
        else:
            return nums[mid]
    
    return recursive_find_peak(list_of_integers, 0, len(list_of_integers) - 1)
