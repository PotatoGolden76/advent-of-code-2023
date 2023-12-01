# Part 1
def part_1():
    sum = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            temp = 0
            for c in line:
                if c.isdigit():
                    temp += int(c)*10
                    break
            for c in line[::-1]:
                if c.isdigit():
                    temp += int(c)
                    break
            sum += temp
    return sum


# Part 2
def part_2():
    digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    sum = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            first = last = 0
            for i in range(len(line)):
                if line[i].isdigit():
                    first = i
                    break
            for i in range(len(line)-1, -1, -1):
                if line[i].isdigit():
                    last = i
                    break


            t_first = (first, -1)
            for d in digit_strings:
                t = line.find(d)
                if t == -1:
                    continue
                if t_first[0] >= t:
                    t_first = (t, digit_strings.index(d)+1)
                    
            t_last = (last, -1)
            for d in digit_strings:
                t = line.rfind(d)
                if t == -1:
                    continue
                if t_last[0] <= t:
                    t_last = (t, digit_strings.index(d)+1)

            # print(f"{t_first}, {t_last}")

            if t_first[1] == -1 :
                sum += int(line[t_first[0]])*10
            else:
                sum += t_first[1]*10
                
            if t_last[1] == -1 :
                sum += int(line[t_last[0]])
            else:
                sum += t_last[1]
                
    return sum

if __name__ == "__main__":
    print("part 1: ", part_1())
    print("part 2: ", part_2())