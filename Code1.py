#Finding the most frequent integer in the list 

def find_most_freq(int_list):
    #Checks if the list is empty
    if not int_list:
        return "Empty List"
    #Initialize the value and updates it when a higher occurence number is found
    max_count = 0
    freq_num = 0
    max_value = max(int_list)
    #Checks from value 1 all the way to the highest value 
    for i in range(1,max_value):
        if int_list.count(i) > max_count :
            max_count = int_list.count(i)
            freq_num = i
    return freq_num


int_list = [1,2,3,3,3,4,4,5]
print(find_most_freq(int_list))
