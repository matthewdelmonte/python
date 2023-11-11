submission = input("Enter a word: ")

def get_count(sentence):
    count = 0
    vowels = {"a", "e", "i", "o", "u"}
    
    for char in sentence:
        if char in vowels:
            count += 1
    return count

solution = get_count(submission)
print("The vowel count is: ", solution)