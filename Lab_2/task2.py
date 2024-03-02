def readFile(file):
    f = open(file, "r")
    filelines = f.readlines()
    lines = []
    for line in filelines:
        lines.append(line[0:-1])
    grades = []
    for elem in lines:
        words = elem.split()
        grades.append(words[1])
        if (int(words[1]) < 60):
            print(" ".join([words[0], 'Failed']))

    sum = 0
    for grade in grades:
        sum += int(grade)
    
    print("Average = " + str(sum/len(grades)))

    f.close()
            
readFile('students.txt')
