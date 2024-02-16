from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(f"{strs=}")
        output = []
        for text in strs:
            print(f"{text=}")
            output_part = [text]
            # strs.remove(text)
            strs = strs[1::]
            print(f"{strs=}")

            for text2 in strs:
                print(f"{text2=}")
                if sorted(list(text)) == sorted(list(text2)):
                    output_part.append(text2)
                    strs.remove(text2)
            #
            print(f"{output_part=}")
            output.append(output_part)

        return output


#
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"output={Solution().groupAnagrams(strs=strs)}")
