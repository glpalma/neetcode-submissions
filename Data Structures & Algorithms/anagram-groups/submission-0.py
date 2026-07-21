class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sWord = str(sorted(word))

            if sWord not in groups.keys():
                groups[sWord] = []
            
            groups[sWord].append(word)
        
        return list(groups.values())
        