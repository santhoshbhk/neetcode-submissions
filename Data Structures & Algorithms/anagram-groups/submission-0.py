class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = dict()
        for word in strs:
            toKey = ''.join(sorted(word))
            if toKey in anagram:
                anagram[toKey].append(word)
            else:
                anagram[toKey] = []
                anagram[toKey].append(word)
                
        res = []
        for key in anagram:
            res.append(anagram[key])
        
        return res