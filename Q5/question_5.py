from io import TextIOWrapper
import operator

isFirstRound = True

def leastPenalty(color2count: dict, n: int) -> list:
    global isFirstRound
    isFirstRound = True
    table = [['' for _ in range(n)] for _ in range(n)]
    color2count = dict(sorted(color2count.items(), key = lambda x: x[1], reverse=True))
    row = 0
    col = 0
    for color, count in color2count.items():
        for _ in range(count):
            table[row][col] = color
            row, col = makeAJump(row, col, n)
    return table

def makeAJump(r, c, n):
    global isFirstRound
    newR = r
    newC = c + 2
    if newC >= n:
        newR += 1
        if newR >= n:
            newR = 0
            isFirstRound = False
        if isFirstRound:
            if newR % 2 == 0:
                newC = 0
            else:
                newC = 1
        else:
            if newR % 2 == 0:
                newC = 1
            else:
                newC = 0
    return newR, newC

def output(outTable: list, out: TextIOWrapper) -> None:
    for row in outTable:
        for value in row:
            out.write(value + ' ')
        out.write('\n')

def main():
    outTable1 = leastPenalty({'R' : 12, 'B' : 13}, 5)
    outTable2 = leastPenalty({'R': 2, 'B': 2}, 4)
    outTable2 = leastPenalty({'R' : 139, 'B' : 1451, 'G': 977, 'W' : 1072, 'Y' : 457}, 64)
    out1 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q5/output_question_5_1', 'w')
    out2 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q5/output_question_5_2', 'w')
    output(outTable1, out1)
    output(outTable2, out2)
    return

if __name__ == '__main__':
    main()

        
        

