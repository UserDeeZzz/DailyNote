# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换
# 需遵循如下规则： 
# 
#  
#  每次转换只能改变一个字母。 
#  转换后得到的单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回一个空列表。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。 
#  Related Topics 广度优先搜索 数组 字符串 回溯算法 
#  👍 338 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        visited = {beginWord}
        queue = [(beginWord, [beginWord])]
        res = []
        minimum = float('inf')
        while queue:
            new_visited = set()

            word, path = queue.pop(0)
            if len(path) > minimum:
                break

            for i in range(len(word)):
                for alpha in 'abcdefghijklmnopqrstuvwxyz':
                    if alpha != word[i]:
                        new_word = word[:i] + alpha + word[i + 1:]
                        if new_word == endWord and new_word in wordList:
                            minimum = len(path)
                            res.append([*path, new_word])

                        if new_word in wordList and new_word not in visited:
                            new_visited.add(new_word)
                            queue.append((new_word, [*path, new_word]))

            visited |= new_visited

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    o = Solution()
    res = o.findLadders(beginWord, endWord, wordList)
    print(res)
