class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue # Skipping Duplicate for 1st number
            
            l = i+1
            r = len(nums)-1

            while l<r: # It is not equal because it is supposed to be UNIQUE Num
                threeSum = nums[i]+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]: #Skipping 2nd Duplicate
                        l+=1
                    while l<r and nums[r]==nums[r+1]: #Skipping 3rd Duplicate
                        r-=1 
        return res
