solution = 0

with open('input.txt', 'r') as file:
    calibrations = file.readlines()

    for line in calibrations:
        start = None
        end = None

        for i in range(0, len(line)):
            if line[i].isnumeric():
                start = line[i]
                break

        for i in range(-1, (len(line)+1)*-1, -1):
            if line[i].isnumeric():
                end = line[i]
                break

        solution += int((start+end))

print(solution)
