from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalinDrome(w):
            return w == w[::-1]
        
        ## Hash Table Approach
        word2Idx = {}
        for i, w in enumerate(words):
            word2Idx[w] = i
        
        results = []
        for p in range(len(words)):
            curWord = words[p]
            
            ## Case 1: curWord is empty, add all existing palindromes to the list
            ## Example: aba + "" = aba, "" + aba = aba
            if curWord == "":
                for i, w in enumerate(words):
                    if isPalinDrome(w) and i != p:
                        results.append([i,p])
                        results.append([p,i])
            ## Case 2: curWord's reverse is already in the list, so we can create a palindrome
            ## Example: abcd + dcba => abcddcba => palindrome
            if curWord[::-1] in word2Idx and word2Idx[curWord[::-1]]!=p: # don't accidentally use the palindrome
                results.append([p, word2Idx[curWord[::-1]]])
                
            ## Case 3: Try to break the word into prefix and suffix and look for palindrome
            ## Skip matching the whole word as suffix/prefix as we have already covered it in Case 2
            for i in range(1, len(curWord)): # length of the prefix is atleast 1
                if isPalinDrome(curWord[:i]) and curWord[i:][::-1] in word2Idx:
                    results.append([word2Idx[curWord[i:][::-1]], p])
                if isPalinDrome(curWord[i:]) and curWord[:i][::-1] in word2Idx:
                    results.append([p, word2Idx[curWord[:i][::-1]]])
        
        return results

s = Solution()
print(s.palindromePairs(words = ["abcd","dcba","lls","s","sssll"])) 