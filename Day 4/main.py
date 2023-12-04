# Part 1
def part_1():
    sum = 0
    with open("input.txt", "r") as f:
        cards = f.readlines()
        for card in cards:
            count = 0
            numbers = [x.strip().split() for x in card[card.find(": ")+1:].strip().split("|")]
            for winning in numbers[0]:
                if winning in numbers[1]:
                    count += 1
            sum += pow(2, count-1) if count else 0 # Why pow(x, 0) = 0.5??
    return sum

# Part 2
def part_2():
    sum = 0
    stack = []
    with open("input.txt", "r") as f:
        cards = f.readlines()

        for card in cards:
            count = 0
            numbers = [x.strip().split() for x in card[card.find(": ")+1:].strip().split("|")]
            for winning in numbers[0]:
                if winning in numbers[1]:
                    count += 1
            stack.append((1, count))
        for i in range(len(stack)):
            current = stack[i]
            stack[i] = (current[0], 0)
            for k in range(current[1]):
                stack[i+k+1] = (stack[i+k+1][0] + current[0], stack[i+k+1][1])
    for c in stack:
        sum += c[0]
    return sum

if __name__ == "__main__":
    print("part 1: ", part_1())
    print("part 2: ", part_2())