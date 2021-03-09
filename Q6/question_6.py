def isRayIntersectsSegment(poi: list, s_poi: list, e_poi: list) -> bool:

    if s_poi[1] == e_poi[1]:
        return False
    if s_poi[1] > poi[1] and e_poi[1] > poi[1]:
        return False
    if s_poi[1] < poi[1] and e_poi[1] < poi[1]:
        return False
    if s_poi[1] == poi[1] and e_poi[1] > poi[1]:
        return False
    if e_poi[1] == poi[1] and s_poi[1] > poi[1]: 
        return False
    if s_poi[0] < poi[0] and e_poi[1] < poi[1]:
        return False

    xseg = e_poi[0] - (e_poi[0] - s_poi[0]) * (e_poi[1] - poi[1]) / (e_poi[1] - s_poi[1]) 
    if xseg < poi[0]:  
        return False
    return True  


def isPoiWithinPoly(poi: list, poly: list) -> bool:
    sinsc = 0  
    for i in range(len(poly) - 1):  # [0,len-1]
        s_poi = poly[i]
        e_poi = poly[i + 1]
        if isRayIntersectsSegment(poi, s_poi, e_poi):
            sinsc += 1  

    return True if sinsc % 2 == 1 else False


def main():
    fpoints = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q6/input_question_6_points', 'r')
    fpolygon = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q6/input_question_6_polygon', 'r')
    fout = open('/Users/zhaoweiyi/Desktop/AY20_MBDS_questions/AY20_MBDS_answers/Q6/output_question_6', 'w')
    points = []
    polygon = []
    while True: 
        line = fpoints.readline()
        if not line: break
        if line == '\n':
            continue
        points.append([int(x) for x in line.split(' ')])
    while True:
        line = fpolygon.readline()
        if not line:
            break
        if line == '\n':
            continue
        polygon.append([int(x) for x in line.split(' ')])
    polygon.append(polygon[0])
    for poi in points:
        if isPoiWithinPoly(poi, polygon):
            fout.write(str(poi[0]) + '\t' + str(poi[1]) + '\t' + 'inside\n')
        else:
            fout.write(str(poi[0]) + '\t' + str(poi[1]) + '\t' + 'outside\n')
    fpoints.close()
    fpolygon.close()
    fout.close()
    return

if __name__ == '__main__':
    main()
