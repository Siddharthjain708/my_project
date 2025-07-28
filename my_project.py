# Function to get marks of students from user input 
def get_marks(): 
    marks = [] 
    n = int(input("Enter number of students:")) 
    print("Enter marks for each students (Enter -1 for absent students):") 
    for i in range(n): 
        mark = int(input("student "+ str(i+1)+": ")) 
        marks.append(mark) 
    return marks 
 
# Function to calculate average marks, ignoring absent students (-1) 
def avg_score(marks): 
    count=0 
    total=0 
    for mark in marks: 
        if mark != -1:  # Skip absent students 
            count +=1 
            total += mark 
    if count == 0:  # Avoid division by zero 
        return 0 
    return total/count 
 
# Function to find highest and lowest marks (excluding absentees) 
def high_low(marks): 
    low = 101   # Assuming maximum marks are 100 
    high = -1 
    for mark in marks: 
        if mark != -1: 
            if mark > high: 
                high = mark 
            if mark < low: 
                low = mark 
    if high == -1:   # If all students are absent 
        return None, None 
    return high, low 
 
# Function to count number of absent students 
def absent(marks): 
    absent =0  
    for mark in marks: 
        if mark == -1: 
            absent += 1 
    return absent 
 
# Function to find the mark with highest frequency 
def frequency(marks): 
    max_freq=0 
    max_freq_mark=0 
    freq = {} 
    # Count occurrences of each mark 
    for mark in marks: 
        if mark != -1: 
            if mark in freq: 
                freq[mark] += 1 
            else: 
                freq[mark] =1 
    # Find the mark with the highest frequency 
    for mark in freq: 
        if freq[mark]>max_freq: 
            max_freq = freq[mark] 
            max_freq_mark = mark 
    return max_freq_mark, max_freq 
 
# Main program starts from here 
 
marks = get_marks() 
print("\nResults\n") 
 
# Display average score 
print("1.Average score of class:",avg_score(marks)) 
 
# Display number of absent students 
print("2.Count of students who were absent for the test:",absent(marks)) 
 
# Display lowest and highest scores 
high, low = high_low(marks) 
print("3.Lowest score:",low) 
print("  Highest score:",high) 
 
# Display most frequently occurring mark 
max_occured_mark, maximum_freq = frequency(marks) 
print("4.Most occured marks are:",max_occured_mark) 
print("  which occured" , maximum_freq , "time")