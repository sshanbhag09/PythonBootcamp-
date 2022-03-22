# class Solution:
#     def countPoints(self, rings: str) -> int:
#         ringdict = {}
#         count=0
#         for i in range(10):
#             ringdict[i] = []
#         print(ringdict)
#         for i in range(0, len(rings), 2):
#             if int(rings[i + 1]) in ringdict:
#                 intkey = int(rings[i + 1])
#                 ringdict[intkey].append(rings[i])
#         print(ringdict)
#         for key in ringdict:
#             if 'R' in ringdict[key] and 'G' in ringdict[key] and "B" in ringdict[key]:
#                 count += 1
#
#         return count
#
# s=Solution()
# print(s.countPoints("B0B6G0R6R0R6G9"))

subset=[]
def subArrayRanges(nums) -> int:
    for i in range(0,len(nums)):
        totalarr=[nums[i]]
        print(totalarr)
        for j in range(i,len(nums)-i):
            if j==i:
                subset.append(totalarr)

            else:
                totalarr.append(nums[j])
                subset.append(totalarr)
subArrayRanges(nums=[4,-2,-3,4,1])

