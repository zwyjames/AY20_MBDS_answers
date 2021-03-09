n = 50
m = 57

def coordinate2index(x1: int, x2: int) -> int:
    return x2 * n + x1

def index2coordinate(index: int) -> int:
    return index % n, index // n

def main():
    in1 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_1/input_coordinates_7_1.txt', 'r')
    in2 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_1/input_index_7_1.txt', 'r')
    out1 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_1/output_index_7_1.txt', 'w')
    out2 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_1/output_coordinates_7_1.txt', 'w')
    in1.readline()
    in2.readline()
    out1.write('index\n') 
    out2.write('x1\tx2\n')
    while True:
        line = in1.readline()
        if not line: break
        coordinate = line.split()
        out1.write(str(coordinate2index(int(coordinate[0]), int(coordinate[1]))) + '\n')
    while True:
        line = in2.readline()
        if not line: break
        index = int(line)
        x1, x2 = index2coordinate(index)
        out2.write(str(x1) + '\t' + str(x2) + '\n')

if __name__ == '__main__':
    main()