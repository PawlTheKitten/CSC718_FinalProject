

if __name__ == "__main__": 
    
    # Print using fstrings
    print (f"Hello, {name}. You are {age}.")
    
    
    # L = ["Geeks\n", "for\n", "Geeks\n"] 
    # writing to file 
    file1 = open('myfile.txt', 'w') 
    file1.writelines(L) 
    file1.close() 
    
    # Reading from file line by line 
    file1 = open('myfile.txt', 'r') 
    Lines = file1.readlines() 
    
    count = 0
    # Strips the newline character 
    for line in Lines: 
        print("Line{}: {}".format(count, line.strip()))
    
    # Split lines
    print(word.split(',')) 
