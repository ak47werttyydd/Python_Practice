from collections import defaultdict
from typing import Dict
from typing import List


class SimilarSentence:
    def __init__(self,SimilarPairs: List[List[str]]):
        self.SimilarPairs = SimilarPairs
        self.SimilarGraph = self.buildGraph()

    def buildGraph(self):
        SimilarGraph = defaultdict(set)
        for sp_lst in self.SimilarPairs:
            for i in range(1,len(sp_lst),1):
                SimilarGraph[sp_lst[i-1]].add(sp_lst[i])
                SimilarGraph[sp_lst[i]].add(sp_lst[i-1])
        return SimilarGraph

    def similar(self,str1,str2) -> bool:
        # identical strings
        if (str1 == str2):
            return True
        str1_words = str1.split()
        str2_words = str2.split()
        # different numbers of words, must not similar
        if (len(str1_words) != len(str2_words)):
            return False

        # comparing each words
        size = len(str1_words)
        for i in range(size):
            visited = defaultdict(int)  # initialize and reset visited
            if self.dfs(str1_words[i], str2_words[i], visited) != 3:  # doesn't match
                return False
        # no return false,i.e. all matching
        return True

    # visited=0:unvisited,1:visiting,2:following nodes are not target, 3: following nodes have target
    def dfs(self, current: str, target: str, visited: Dict[str, int]) -> int:
        if visited[current] == 2:  # following nodes don't have target, skip and return
            return 2
        # elif visited[current]==3: #already found
        #	return 3
        # indeed redundant. Once the target is found, 3 propagates back up the call stack, so no future calls will reach
        if current == target:  # immediately find target
            # visited[current]=3
            # There is no scenario where a previously marked visited = 3 node would be re-explored because the DFS terminates immediately after finding the target. Thus, there’s no need to mark nodes as 3.
            return 3

        # set current node is visiting before traverse
        visited[current] = 1
        # traverse all following nodes
        for adjacent in self.SimilarGraph[current]:
            if visited[adjacent] != 1:  # don't revisit if there is a cycle
                if self.dfs(adjacent, target, visited) == 3:  # already found
                    # visited[current]=3
                    return 3

        # after traversal, i.e. search all the subsequent nodes but not target found(i.e. return 3)
        visited[current] = 2  # set following nodes don't have target
        return 2

#test1, similar sentences
#similar sentences
str1="I am a good student"
str2="I am a fine student"
str3="I am an excellent student"
str7="They are the best students"

similarPairs=[
        #a set, in a vector
        ["I","He","They"],
        #a set, in two vectors, same first element
        ["am","is"],
        ["am","are"],
        #a set, in two vectors, different first element
        ["a","an"],
        ["an","the"],
        #a set, in a vector
        ["good","fine","excellent","best"],
        #a set, in two vectors, same first element
        ["student","students"]
    ]

ss=SimilarSentence(similarPairs)
print("Is str1 and str2 similar? ",ss.similar(str1,str2)) #True
print("Is str2 and str3 similar? ",ss.similar(str2,str3)) #True
print("Is str3 and str7 similar? ",ss.similar(str3,str7)) #True
print("Is str1 and str7 similar? ",ss.similar(str1,str7)) #True
print()
#test2: not similar to the test1
str4="He is a good teacher" #teacher doesn't match student
str5="He is not a fine student" #more words
print("Is str1 and str4 similar? ",ss.similar(str1,str4)) #False
print("Is str1 and str5 similar? ",ss.similar(str1,str5)) #False