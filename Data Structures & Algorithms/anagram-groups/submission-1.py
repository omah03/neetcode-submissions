class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = {}

        # for word in strs:
        #     key = "".join(sorted(word))
        #     if key not in groups:
        #         groups[key] = []
        #     groups[key].append(word)
        # return list(groups.values())

        groups = {}

        for word in strs:
            counts = [0] * 26
                # Count the letters here
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            # Convert counts into a tuple
            count_tuple = tuple(counts)
            if count_tuple not in groups:
                groups[count_tuple] = []
            groups[count_tuple].append(word)
        return list(groups.values())
 



                                    
        