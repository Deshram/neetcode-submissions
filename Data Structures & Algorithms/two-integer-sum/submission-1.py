class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        get_indices = {}
        for i,num in enumerate(nums):
            if get_indices.get(num):
                get_indices[num].append(i)
            else:
                get_indices[num] = [i]
        # print(get_indices)
        for num in nums:
            if get_indices.get(target - num):
                
                for num_idx in get_indices[num]: 
                    for comp_idx in get_indices[target - num]:
                        if num_idx != comp_idx:
                            return [num_idx, comp_idx]        
 
        