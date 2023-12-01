number_array = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

solution = 0
with open('input.txt', 'r') as file:
    calibrations = file.readlines()
    lineNo = 0
    for line in calibrations:
        start1idx = None
        start = None
        end = None
        endstring = None
        startstring = None
        length = len(line)

        for i in range(0, length):
            flag = False
            for j in range(0, 10):
                start1idx = line[: i].find(number_array[j])
                if start1idx != -1:
                    start = j
                    startstring = line[: i]
                    flag = True
                    break
            if flag:
                break

        if start != None:
            for i in range(0, length):
                if line[i].isnumeric() and i < start1idx:
                    start = int(line[i])
                    break
        else:
            for i in range(0, length):
                if line[i].isnumeric():
                    start = int(line[i])
                    break

        for i in range(-1, (length+1)*-1, -1):
            flag = False
            for j in range(0, 10):
                if line[i : -1].find(number_array[j]) != -1:
                    end = j
                    endstring = line[i: -1]
                    flag = True
                    break
            if(flag):
                break

        if end != None:
            for i in range(-1, -1*(len(endstring)+1), -1):
                if line[i].isnumeric():
                    end = int(line[i])
                    break
        else:
            for i in range(-1, (length+1)*-1, -1):
                if line[i].isnumeric():
                    end = int(line[i])
                    break

        solution += (start*10) + end

print(solution)
