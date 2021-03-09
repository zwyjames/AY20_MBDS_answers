def path_for_num(m: int, n : int, target: int) -> str:
    min_num = n - 1 + (m + 1) * m // 2
    max_num = (m + 1) * m // 2 + (n - 1) * m
    diff = target - min_num
    quotient = diff // (n - 1)
    remainder = diff % (n - 1)
    if remainder != 0:
        return 'D' * quotient + 'R' * (n - 1 - remainder) + 'D' + 'R' * remainder + 'D' * (m - 2 - quotient)
    else:
        return 'D' * quotient + 'R' * (n - 1) + 'D' * (m - 1 - quotient)

def main() :
    temp = input("Please input row, col, and target. With space splited. \n")
    nums = temp.split(' ')
    print("The path is " + path_for_num(int(nums[0]), int(nums[1]), int(nums[2])))

if __name__ == '__main__':
    # main()
    with open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q1/output_question_1','w') as f:
        print("65 {}".format(path_for_num(9, 9, 65)), file=f)
        print("72 {}".format(path_for_num(9, 9, 72)), file=f)
        print("90 {}".format(path_for_num(9, 9, 90)), file=f)
        print("110 {}".format(path_for_num(9, 9, 110)), file=f)
        print("87127231192 {}".format(path_for_num(90000, 1000000, 87127231192)), file=f)
        print("5994891682 {}".format(path_for_num(90000, 1000000, 5994891682)), file=f)