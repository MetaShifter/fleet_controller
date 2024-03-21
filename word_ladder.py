# Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest
# transformation sequence from beginWord to endWord, such that:
# 1. Only one letter can be changed at a time.
# 2. Each transformed word must exist in the word list.
# Note:
# - Return 0 if there is no such transformation sequence.
# - All words have the same length.
# - All words contain only lowercase alphabetic characters.
# - You may assume no duplicates in the word list.
# - You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
# Input:
# beginWord = 'hit'
# endWord = 'cog'
# wordList = ['hit','hot','dot','dog','lot','log','cog']
# Output: 5
# Explanation: As one shortest transformation is 'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog',
# return its length 5.
# Example 2:
# Input:
# beginWord = 'hit'
# endWord = 'cog'
# wordList = ['hit', 'hot','dot','dog','lot','log']
# Output: 0
# Explanation: The endWord 'cog' is not in wordList, therefore no possible transformation.

# Extra tests

# endWord = 'bag'
# ['hit','hot','dot','dog','lot','log','cog','lag','bat','bag','rot']
# ['hit','hot','dot','dog','lot','log','cog','lag','bat','bag','rot','bot']



def create_word_dict(word_list):
    word_dict = {}  
    for word in word_list:
        for index in range(len(word)):
            match_pattern = word[:index] + '_' + word[index + 1:]

            if match_pattern not in word_dict:
                word_dict[match_pattern] = set()  

            word_dict[match_pattern].add(word)
    return word_dict

def generate_match_template(word, index):
    return word[:index] + '_' + word[index + 1:]

def find_transformation(beginWord, endWord, wordList):
    if endWord not in wordList:  
        return 0

    word_dict = create_word_dict(wordList)

    bfs_queue = [[beginWord, 1]]  
    visited_words = {beginWord}  

    while bfs_queue:
        current_word, level = bfs_queue.pop(0)  
        if current_word == endWord:
            return level

        for index in range(len(current_word)):
            wildcard = generate_match_template(current_word, index)
            for neighbor in word_dict[wildcard]:
                if neighbor not in visited_words:
                    visited_words.add(neighbor)
                    bfs_queue.append((neighbor, level + 1))

    return 0

def main():
    # beginWord = "hit"
    # endWord = "cog"
    # word_list = ['hit','hot', 'klo', 'dot','dog','lot','log','cog']

    beginWord = "hit"
    endWord = "bag"
    word_list = ['hit','hot','dot','dog','lot','log','cog','lag','bat','bag','rot','bot']
    
    print(find_transformation(beginWord, endWord, word_list))

if __name__ == "__main__":
    main()
