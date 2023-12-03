# Part 1
def part_1():
    RED = 12
    GREEN = 13
    BLUE = 14

    sum = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        n = len(lines)
        sum = (n*(n+1))//2
        i = 1
        for game in lines:
            sets = game[game.find(": ")+1:].strip().split(";")
            
            for rd in sets:
                ok = True
                colours = rd.split(",")
                for c in colours:
                    if c.find("red") != -1:
                        if int(c.replace("red", "")) > RED:
                            sum-=i
                            ok = False
                            break
                    if c.find("green") != -1:
                        if int(c.replace("green", "")) > GREEN:
                            sum-=i
                            ok = False
                            break
                    if c.find("blue") != -1:
                        if int(c.replace("blue", "")) > BLUE:
                            sum-=i
                            ok = False
                            break
                if not ok:
                    break
            i += 1
    return sum

# Part 2
def part_2():
    sum = 0
    with open("input.txt", "r") as f:
        for game in f.readlines():
            m_red = m_green = m_blue = -1
            sets = game[game.find(": ")+1:].strip().split(";")
            
            for rd in sets:
                colours = rd.split(",")
                for c in colours:
                    if c.find("red") != -1:
                        if int(c.replace("red", "")) > m_red or m_red == -1:
                            m_red = int(c.replace("red", ""))
                    if c.find("green") != -1:
                        if int(c.replace("green", "")) > m_green or m_green == -1:
                            m_green = int(c.replace("green", ""))
                    if c.find("blue") != -1:
                        if int(c.replace("blue", "")) > m_blue or m_blue == -1:
                            m_blue = int(c.replace("blue", ""))
            sum += m_red*m_green*m_blue
    return sum

if __name__ == "__main__":
    print("part 1: ", part_1())
    print("part 2: ", part_2())