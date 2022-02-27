from itertools import groupby

class Solution:
       def groupAnagrams(self, strs):
        result = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())
        # return [list(value_) for k, value_ in groupby(sorted(strs, key=sorted), sorted)]
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# if __name__ == "__main__":
#     from timeit import timeit
#     print(timeit(
#         "ob1.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])",
#         setup="from __main__ import ob1", number=100000
#     ))