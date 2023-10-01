def sort_words(input_string):
    words = input_string.split('-')
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
    
    
    sorted_string = '-'.join(words)
    
    return sorted_string
input_string = "green-red-yellow-black-white"
sorted_result = sort_words(input_string)
print("Sorted Result:", sorted_result)