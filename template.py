# Main
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
    

    # Iterate through a file .
    for line in Lines: 
        print("Line{}: {}".format(count, line.strip()))
    
        # Split lines based on , 
        print(word.split(',')) 
        

    # while loop
    while true:
        print("do stuff");

    
    print(f'Completed all paths after {i} iterations.')
