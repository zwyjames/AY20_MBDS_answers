import numpy as np

def put_label(input):
    label = 0

    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 1:
                label = computeLabel(i, j, input, label)


def computeLabel(i, j, input, label) -> int:
    
    if i == 0 and j == 0:
        input[i][j] = label + 1
    elif i == 0:
        if input[i][j-1] != 0:
            input[i][j] = input[i][j-1]
        else:
            input[i][j] = label + 1
    elif j == 0:
        if input[i-1][j] != 0:
            input[i][j] = input[i-1][j]
        else:
            input[i][j] = label + 1
    else:
        # left & up
        if input[i][j-1] != 0 and input[i-1][j] != 0:
            if input[i][j-1] < input[i-1][j]:
                input[i][j] = input[i][j-1]
                replace(input[i-1][j], input[i][j-1], i, input)
            elif input[i][j-1] > input[i-1][j]:
                input[i][j] = input[i-1][j]
                replace(input[i][j-1], input[i-1][j], i, input)
            else:
                input[i][j] = input[i][j-1]
        # left 
        elif input[i][j-1] != 0:
            input[i][j] = input[i][j-1]
        # up
        elif input[i-1][j] != 0:
            input[i][j] = input[i-1][j]
        # none
        else:
            input[i][j] = label + 1

    return max(input[i][j], label)


def replace(source, target, i, input):
    for i in range(i+1):
        for j in range(len(input[0])):
            if input[i][j] == source:
                input[i][j] = target


def tidy(input):
    cnt = 1
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == cnt:
                cnt += 1
            elif input[i][j] > cnt:
                replace(input[i][j], cnt, len(input) - 1, input)
                cnt += 1





if __name__ == '__main__':
    input= np.loadtxt('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q4/input_question_4', dtype='uint8')

    put_label(input)
    tidy(input)
    with open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q4/output_question_4','w') as f:
        for row in input:
            for col in row:
                print(str(col), end='\t', file=f)
            print(file=f)
