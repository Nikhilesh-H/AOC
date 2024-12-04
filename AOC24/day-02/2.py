# path = r"AOC24\day-02\test.txt"
path = r"AOC24\day-02\input.txt" 

with open(path) as f:
    l = f.readlines()

safe = 0

for i in l:
    report = [int(i) for i in i.split()]
    flag = 1
    
    # Check if report is supposed to be descending or ascending
    if (report[0] > report[1]): 
        for level in range(len(report)-1):
            if (report[level] <= report[level+1]) or (abs(report[level] - report[level+1]) > 3): # Check if rules are violated
                flag = 0
    else:
        for level in range(len(report)-1):
            if (report[level] >= report[level+1]) or (abs(report[level] - report[level+1]) > 3): # Check if rules are violated
                flag = 0

    # Iteratively remove each level from the list and check again
    if (flag == 0):
        for i in range(len(report)):
            flag = 1
            new_report = report[:]
            new_report.pop(i)

            if (new_report[0] > new_report[1]):
                for level in range(len(new_report)-1):
                    if (new_report[level] <= new_report[level+1]) or (abs(new_report[level] - new_report[level+1]) > 3):
                        flag = 0
            else:
                for level in range(len(new_report)-1):
                    if (new_report[level] >= new_report[level+1]) or (abs(new_report[level] - new_report[level+1]) > 3):
                        flag = 0
            # Stop iterating if a new report is safe
            if (flag):
                break
    
    if (flag):
        safe += 1
        
print(safe)