import numpy
l = [4, 8, 5, 9, 6, 7]

def coordinate2index(coordinate: list) -> int:
    index = 0
    for i, v in enumerate(coordinate):
        product = 1
        for j in range(i) :
            product *= l[j]
        index += product * v
    return index

def index2coordinate(index: int) -> list:
    coordinate = []
    product = numpy.prod(l)
    for v in reversed(l):
        product //= v
        coordinate.append(index // product)
        index %= product
    coordinate.reverse()
    return coordinate

def main():
    in1 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_2/input_coordinates_7_2.txt', 'r')
    in2 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_2/input_index_7_2.txt', 'r')
    out1 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_2/output_index_7_2.txt', 'w')
    out2 = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q7/Q7_2/output_coordinates_7_2.txt', 'w')
    in1.readline()
    in2.readline()
    out1.write('index\n') 
    out2.write('x1\tx2\tx3\tx4\tx5\tx6\n')
    while True:
        line = in1.readline()
        if not line: break
        coordinate = [int(x) for x in line.split()]
        out1.write(str(coordinate2index(coordinate)) + '\n')
    while True:
        line = in2.readline()
        if not line: break
        index = int(line)
        coordinate = index2coordinate(index)
        for x in coordinate:
            out2.write(str(x) + '\t')
        out2.write('\n')

if __name__ == '__main__':
    main()  