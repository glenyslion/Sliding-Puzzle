import random

print("SLIDING PUZZLE 2020")
print("The objective of this game is to solve the puzzle by press the left, right, up, and down button and make all the numbers appear sequentially")
print("You can choose either 8 or 15 puzzle. And you move the tiles with the keyboard using 4 different letters.")


def main():
    while(True):
        choose = input("Choose either 8 or 15 puzzle = ")
        if(choose == '8' or choose == '15'):
            choose = int(choose)
            if(choose == 8):
                sizepuz = 3
                return sizepuz
            else:
                sizepuz = 4
                return sizepuz
        else:
            print("Your input is invalid! You should input either 8 or 15!")


def move():
    while(True):
        direction = input("Input 4 letters for left, right, up and down = ")
        count = 0
        visited = []
        alphabet = 0
        dirtru = []
        for x in range(0, 123):
            visited.append(False)
        for x in direction:
            if(x == " "):
                continue
            else:
                if((x >= chr(65) and x <= chr(90)) or (x >= chr(97) and x <= chr(122))):
                    # ord is use to get the ASCII code from the alphabet
                    alphabet = ord(x)
                    if (visited[alphabet] == True):
                        continue
                    dirtru.append(x)
                    count += 1
                    visited[alphabet] = True
        if(count == 4):
            print("Use letter %c,%c,%c,%c for left, right, up, and down moves" % (
                dirtru[0], dirtru[1], dirtru[2], dirtru[3]))
            return dirtru[0], dirtru[1], dirtru[2], dirtru[3]
        else:
            print("Please enter only 4 different letters!")


def puzzle(size):
    while (True):
        num = []
        for b in range(0, size+1):
            temp = []
            for k in range(0, size+1):
                temp.append(0)
            num.append(temp)
        visit = []
        for x in range(0, size*size):
            visit.append(False)

        for b in range(1, size+1):
            for k in range(1, size+1):
                if(b == size and k == size):
                    num[b][k] = 0
                    return num
                else:
                    rand = random.randint(1, size*size-1)
                    while(visit[rand] == True):
                        rand = random.randint(1, size*size-1)
                    num[b][k] = rand
                    visit[rand] = True


def inversion(size, num):
    arr1d = []
    count = 0
    for b in range(1, size+1):
        for k in range(1, size+1):
            arr1d.append(num[b][k])
    for a1 in range(0, size*size-1):
        for b1 in range(a1, size*size-1):
            if(arr1d[a1] > arr1d[b1]):
                count = count+1
    if(count % 2 == 0):
        return True
    else:
        return False


def blank_pos(size, num):
    for b in range(1, size+1):
        for k in range(1, size+1):
            if (num[b][k] == 0):
                return [b, k]


def move_pos(num, size, direction_input, direction):
    blank_row, blank_col = blank_pos(size, num)
    # left
    if(direction_input == direction[0]):
        num[blank_row][blank_col], num[blank_row][blank_col +
            1] = num[blank_row][blank_col+1], num[blank_row][blank_col]
        return num
    # right
    if(direction_input == direction[1]):
        num[blank_row][blank_col], num[blank_row][blank_col -
            1] = num[blank_row][blank_col-1], num[blank_row][blank_col]
        return num
    # up
    if(direction_input == direction[2]):
        num[blank_row][blank_col], num[blank_row +
            1][blank_col] = num[blank_row+1][blank_col], num[blank_row][blank_col]
        return num
    # down
    if(direction_input == direction[3]):
        num[blank_row][blank_col], num[blank_row -
            1][blank_col] = num[blank_row-1][blank_col], num[blank_row][blank_col]
        return num


def valid_move(size, blank, direction):
    # blank[0]=blank_row and blank[1]=blank_col
    available_direction = []
    if(blank[0] != 1):
        available_direction.append(direction[3])
    if(blank[0] != size):
        available_direction.append(direction[2])
    if(blank[1] != 1):
        available_direction.append(direction[1])
    if(blank[1] != size):
        available_direction.append(direction[0])

    return available_direction


def goal(size):
    if(size == 3):
        ans = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 4, 5, 6], [0, 7, 8, 0]]
        return ans
    else:
        ans = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 5, 6, 7, 8],
            [0, 9, 10, 11, 12], [0, 13, 14, 15, 0]]
        return ans


while(True):
        direc = move()
        sizepuzzle = main()

        num_puzzle = puzzle(sizepuzzle)
        while(True):
        if(inversion(sizepuzzle, num_puzzle) == True):
            for b in range(1, sizepuzzle+1):
                for k in range(1, sizepuzzle+1):
                    if(num_puzzle[b][k] >= 10):
                        print(num_puzzle[b][k], end=" ")
                    elif(num_puzzle[b][k] == 0):
                        break
                    else:
                        print(num_puzzle[b][k], end="  ")
                print()
            break
        else:
            num_puzzle = puzzle(sizepuzzle)

        count_move = 0
        while(True):
            blank = blank_pos(sizepuzzle, num_puzzle)
            validmove = valid_move(sizepuzzle, blank, list(direc))
            totalvalidmove = len(validmove)
            direction = 0

            while(True):
                move = False
                direction = input("Enter move %s : " % (validmove))
                for x in range(0, totalvalidmove):
                    if(direction == validmove[x]):
                        move = True
                        break
                if(move == True):
                    count_move += 1
                    break

            num_after_move = move_pos(
                num_puzzle, sizepuzzle, direction, list(direc))
            for b in range(1, sizepuzzle+1):
                for k in range(1, sizepuzzle+1):
                    if(num_after_move[b][k] != 0):
                        if(num_after_move[b][k] >= 10):
                            print(num_after_move[b][k], end=" ")
                        else:
                            print(num_after_move[b][k], end="  ")
                    else:
                        print(end="   ")
                print()
                if(num_after_move == goal(sizepuzzle)):
                    print("Total move = ", count_move)
    while(True):
        ask= input("Do you want to play again? (y/n) = ")
        if(ask=='y' or ask=='n'):
            break
        else:
            print("Input is invalid! Input only y/n!")
    if(ask=='n'):
        break
    else:
        continue
