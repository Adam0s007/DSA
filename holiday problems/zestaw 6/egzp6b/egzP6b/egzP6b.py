from egzP6btesty import runtests 

def jump ( M ):
    vectors = []
    for elem in M:                       #x #y
        if elem == "UL": vectors.append((-1,-2))
        elif elem == "LU": vectors.append((-2,-1))
        elif elem == "LD": vectors.append((-2,1))
        elif elem == "DL": vectors.append((-1,2))
        elif elem == "DR": vectors.append((1,2))
        elif elem == "RD": vectors.append((2,1))
        elif elem == "RU": vectors.append((2,-1))
        elif elem == "UR":vectors.append((1,-2))
    position = {}
    counter =1
    pos = [0,0]
    position[tuple(pos)] = True
    for i in range(len(vectors)):
        pos[1] += vectors[i][1]
        pos[0] += vectors[i][0]
        
        if tuple(pos) not in position:
            position[tuple(pos)] = True
            counter+=1
        else:
            position.pop(tuple(pos))
            counter-=1


    return counter
    
runtests(jump, all_tests = True)