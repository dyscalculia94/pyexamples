def __main__():
    grades = [5, 6, 7, 8, 9, 10]
    
    print ("Possible grades: ")
    for i in grades:
        print(str(i) + " ", end = "")
    print()

    print ("Possible grades: ")
    for i in range(len(grades)):
        print(str(grades[i]) + " ", end = "")
    print()

__main__()