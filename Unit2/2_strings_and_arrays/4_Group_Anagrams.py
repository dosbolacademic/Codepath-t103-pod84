from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            group[key].append(i)
        return group.values()
