# Part 1
def part_1():
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    sum = 0
    with open("input.txt", "r") as f:
        engine = f.readlines()
        for line in range(len(engine)):
            is_adjacent = False
            current_nr = ""
            for col in range(len(engine[0].strip())):
                current = engine[line][col]
                if current.isdigit():
                    current_nr += current
                    if not is_adjacent:
                        for d in directions:
                            d_line = max(0, min(line + d[0], len(engine)-1))
                            d_col = max(0, min(col + d[1], len(engine[0].strip())-1))
                            if d_line != line or d_col != col:
                               if (not engine[d_line][d_col].isdigit()) and engine[d_line][d_col] != '.':
                                    is_adjacent = True
                                    break
                elif current_nr != "":
                        sum += int(current_nr) if is_adjacent else 0
                        current_nr = ""
                        is_adjacent = False
            if current_nr != "":
                sum += int(current_nr) if is_adjacent else 0
            
    return sum

# Part 2
def part_2():
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    sum = 0
    with open("input.txt", "r") as f:
        engine = f.readlines()
        for line in range(len(engine)):
            for col in range(len(engine[0].strip())):
                current = engine[line][col]
                if current == '*':
                    numbers = []
                    for d in directions:
                        d_line = max(0, min(line + d[0], len(engine)-1))
                        d_col = max(0, min(col + d[1], len(engine[0].strip())-1))
                        if d_line != line or d_col != col:
                            if engine[d_line][d_col].isdigit():
                                numbers.append((d_line, d_col))
                    count = 0
                    for n in numbers:
                        count += 1 if not (n[0], n[1]+1) in numbers else 0
                    
                    if count == 2:
                        prod = 1
                        while numbers != []:
                            temp_nr = f"{engine[numbers[0][0]][numbers[0][1]]}"

                            current = numbers[0]
                            while engine[current[0]][current[1]+1].isdigit():
                                temp_nr += engine[current[0]][current[1]+1]
                                numbers.remove((current[0], current[1]+1)) if (current[0], current[1]+1) in numbers else None
                                current = (current[0], current[1]+1)
                            
                            current = numbers[0]
                            while engine[current[0]][current[1]-1].isdigit():
                                temp_nr = engine[current[0]][current[1]-1] + temp_nr
                                numbers.remove((current[0], current[1]-1)) if (current[0], current[1]-1) in numbers else None
                                current = (current[0], current[1]-1)

                            numbers.pop(0)
                            prod *= int(temp_nr)

                        sum += prod
    return sum

if __name__ == "__main__":
    print("part 1: ", part_1())
    print("part 2: ", part_2())