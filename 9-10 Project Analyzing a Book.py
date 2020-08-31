words = []
word_count = 0
char_count = 0
sentence_count = 0
max_words = ['', '', '', '', '', '', '', '', '', '']

with open('some book.txt', 'r', encoding='utf-8') as book:
    
    for line in book:
        for word in line.split():
            
            for char in word:
                if char != ' ':
                    char_count += 1
                if char in ['?', '.', '!']:
                    sentence_count += 1
                    
            if word[-1] in '”':
                word = word[:-1]
                
            if word[-1] in [',', ';', '.', '?', '!']:
                word = word[:-1]   
                
            if '-' in word:
                words_with_hyphens = word.split('-')
                for word in words_with_hyphens:
                    words.append(word)
                
            elif '—' in word:
                words_with_hyphens = word.split('—')
                for word in words_with_hyphens:
                    words.append(word)
                
            else:
                words.append(word)
                
for word in words:    
    word_count += 1
    for i in range(10):
        if len(word) > len(max_words[i]):  
            max_words[i + 1:] = max_words[i:-1]
            max_words[i] = word
            break      
            
from collections import Counter
counts = Counter(words)

print(f'The total word count: {word_count:,}')                    
print(f'The total character count: {char_count:,}')        
print(f'The total sentence count: {sentence_count:,}')  
print(f'The average word length: {char_count / word_count:,}')  
print(f'The average sentence length: {word_count / sentence_count:,}')  
print(f'\nThe top 10 longest words:\n{max_words}')  
print(f'\nA word distribution containing frequency counts of all words:\n{counts}')
