# zad6test_spec.py

ALLOWED_TIME = 1000

from random import randint,shuffle
end = None

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n - liczba miast
#  n 
  [4,  [0,1,2,3]],                     # 0
  [7,  [0,1,2,3,4,5,6]],               # 1
  [10, [8,9,7,3,4,6,2,0,1,5]],         # 2
  [11, None],                          # 3
  [13, '*'],                           # 4
  [20, '*'],                           # 5
  [32, '*'],                           # 6
  [40, '*'],                          # 7
 ]


def gentest(n, hint ):
    from testy import MY_random

    if n==4:
      G = [ ([1],[3]),      
            ([2],[0]), 
            ([3],[1]),  
            ([0],[2]) ]
      return [G], hint

    if n==7:
      G = [ ([1],[3,4,6]),      
            ([2],[0]), 
            ([3],[1]),  
            ([0,4,6],[2]),
            ([5],[3,6,0]),
            ([6],[4]),
            ([0,3,4],[5]) ]
      return [G], hint

    elif n==10:
      G = [ ([1],[2,3,4]),      
             ([0],[2,5,6]), 
             ([1,5,6],[0,3,4]),  
             ([0,2,4],[5,7,8]), 
             ([0,2,3],[6,7,9]),  
             ([1,2,6],[3,7,8]), 
             ([1,2,5],[4,7,9]),  
             ([4,6,9],[3,5,8]), 
             ([3,5,7],[9]),      
             ([4,6,7],[8]) ]
      return [G], hint

    elif n==11:
      G = [ ([1,10],[2,3,4]),      
            ([0,10],[2,5,6]), 
            ([1,5,6],[0,3,4]),  
            ([0,2,4],[5,7,8]), 
            ([0,2,3],[6,7,9]),  
            ([1,2,6],[3,7,8]), 
            ([1,2,5],[4,7,9]),  
            ([4,6,9],[3,5,8]), 
            ([3,5,7],[9,10]),      
            ([4,6,7],[8,10]), 
            ([0,1],[8,9]) ]
      return [G], hint

    elif n==13:
      G = [ ([1,10,11],[2,3,4]),      
            ([0,10,11],[2,5,6]), 
            ([1,5,6],[0,3,4]),  
            ([0,2,4],[5,7,8]), 
            ([0,2,3],[6,7,9]),  
            ([1,2,6],[3,7,8]), 
            ([1,2,5],[4,7,9]),  
            ([4,6,9],[3,5,8]), 
            ([3,5,7],[9,10,12]),      
            ([4,6,7],[8,10,12]), 
            ([0,1,11],[8,9,12]),
            ([0,1,10],[12]),
            ([11],[8,9,10]) ]
      return [G], hint

    elif n==20:
      G=[([1,9,10,],[2,3,5,42,44,]),
      ([0,9,10,],[2,19,20,36,38,48,50,52,53,54,56,]),
      ([1,19,20,36,38,48,50,52,53,54,56,],[0,3,5,42,44,]),
      ([4,6,7,33,34,51,52,],[0,2,5,42,44,]),
      ([3,6,7,33,34,51,52,],[5,10,11,16,17,49,50,]),
      ([4,10,11,16,17,49,50,],[0,2,3,42,44,]),
      ([3,4,7,33,34,51,52,],[8,43,44,58,59,]),
      ([3,4,6,33,34,51,52,],[8,25,26,28,29,37,38,]),
      ([7,25,26,28,29,37,38,],[6,43,44,58,59,]),
      ([0,1,10,],[11,18,20,]),
      ([0,1,9,],[4,5,11,16,17,49,50,]),
      ([4,5,10,16,17,49,50,],[9,18,20,]),
      ([13,24,25,],[14,31,32,]),
      ([12,24,25,],[14,18,19,34,35,57,58,]),
      ([13,18,19,34,35,57,58,],[12,31,32,]),
      ([16,39,40,],[17,30,32,45,47,51,53,57,59,]),
      ([15,39,40,],[4,5,10,11,17,49,50,]),
      ([4,5,10,11,16,49,50,],[15,30,32,45,47,51,53,57,59,]),
      ([13,14,19,34,35,57,58,],[9,11,20,]),
      ([13,14,18,34,35,57,58,],[1,2,20,36,38,48,50,52,53,54,56,]),
      ([1,2,19,36,38,48,50,52,53,54,56,],[9,11,18,]),
      ([22,36,37,],[23,33,35,46,47,]),
      ([21,36,37,],[23,30,31,40,41,42,43,48,49,]),
      ([22,30,31,40,41,42,43,48,49,],[21,33,35,46,47,]),
      ([12,13,25,],[26,]),
      ([12,13,24,],[7,8,26,28,29,37,38,]),
      ([7,8,25,28,29,37,38,],[24,]),
      ([28,54,55,],[29,39,41,]),
      ([27,54,55,],[7,8,25,26,29,37,38,]),
      ([7,8,25,26,28,37,38,],[27,39,41,]),
      ([22,23,31,40,41,42,43,48,49,],[15,17,32,45,47,51,53,57,59,]),
      ([22,23,30,40,41,42,43,48,49,],[12,14,32,]),
      ([12,14,31,],[15,17,30,45,47,51,53,57,59,]),
      ([3,4,6,7,34,51,52,],[21,23,35,46,47,]),
      ([3,4,6,7,33,51,52,],[13,14,18,19,35,57,58,]),
      ([13,14,18,19,34,57,58,],[21,23,33,46,47,]),
      ([21,22,37,],[1,2,19,20,38,48,50,52,53,54,56,]),
      ([21,22,36,],[7,8,25,26,28,29,38,]),
      ([7,8,25,26,28,29,37,],[1,2,19,20,36,48,50,52,53,54,56,]),
      ([15,16,40,],[27,29,41,]),
      ([15,16,39,],[22,23,30,31,41,42,43,48,49,]),
      ([22,23,30,31,40,42,43,48,49,],[27,29,39,]),
      ([22,23,30,31,40,41,43,48,49,],[0,2,3,5,44,]),
      ([22,23,30,31,40,41,42,48,49,],[6,8,44,58,59,]),
      ([6,8,43,58,59,],[0,2,3,5,42,]),
      ([46,55,56,],[15,17,30,32,47,51,53,57,59,]),
      ([45,55,56,],[21,23,33,35,47,]),
      ([21,23,33,35,46,],[15,17,30,32,45,51,53,57,59,]),
      ([22,23,30,31,40,41,42,43,49,],[1,2,19,20,36,38,50,52,53,54,56,]),
      ([22,23,30,31,40,41,42,43,48,],[4,5,10,11,16,17,50,]),
      ([4,5,10,11,16,17,49,],[1,2,19,20,36,38,48,52,53,54,56,]),
      ([3,4,6,7,33,34,52,],[15,17,30,32,45,47,53,57,59,]),
      ([3,4,6,7,33,34,51,],[1,2,19,20,36,38,48,50,53,54,56,]),
      ([1,2,19,20,36,38,48,50,52,54,56,],[15,17,30,32,45,47,51,57,59,]),
      ([27,28,55,],[1,2,19,20,36,38,48,50,52,53,56,]),
      ([27,28,54,],[45,46,56,]),
      ([45,46,55,],[1,2,19,20,36,38,48,50,52,53,54,]),
      ([13,14,18,19,34,35,58,],[15,17,30,32,45,47,51,53,59,]),
      ([13,14,18,19,34,35,57,],[6,8,43,44,59,]),
      ([6,8,43,44,58,],[15,17,30,32,45,47,51,53,57,]),]

      
      return [G],hint 

    elif n==32:

      G=[([1,61,62,99,100,108,109,115,116,126,127,],[2,4,5,25,26,70,71,97,98,105,107,]),
      ([0,61,62,99,100,108,109,115,116,126,127,],[2,9,10,31,32,57,58,67,68,135,136,]),
      ([1,9,10,31,32,57,58,67,68,135,136,],[0,4,5,25,26,70,71,97,98,105,107,]),
      ([4,15,16,81,82,144,145,],[5,132,134,135,137,]),
      ([3,15,16,81,82,144,145,],[0,2,5,25,26,70,71,97,98,105,107,]),
      ([0,2,4,25,26,70,71,97,98,105,107,],[3,132,134,135,137,]),
      ([7,21,22,48,49,132,133,],[8,9,11,96,98,99,101,130,131,]),
      ([6,21,22,48,49,132,133,],[8,12,13,40,41,79,80,85,86,87,88,147,148,]),
      ([7,12,13,40,41,79,80,85,86,87,88,147,148,],[6,9,11,96,98,99,101,130,131,]),
      ([1,2,10,31,32,57,58,67,68,135,136,],[6,8,11,96,98,99,101,130,131,]),
      ([1,2,9,31,32,57,58,67,68,135,136,],[11,12,14,16,17,22,23,37,38,60,62,63,65,90,92,]),
      ([10,12,14,16,17,22,23,37,38,60,62,63,65,90,92,],[6,8,9,96,98,99,101,130,131,]),
      ([7,8,13,40,41,79,80,85,86,87,88,147,148,],[10,11,14,16,17,22,23,37,38,60,62,63,65,90,92,]),
      ([7,8,12,40,41,79,80,85,86,87,88,147,148,],[14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,]),
      ([13,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,],[10,11,12,16,17,22,23,37,38,60,62,63,65,90,92,]),
      ([3,4,16,81,82,144,145,],[17,18,20,24,26,123,125,129,131,]),
      ([3,4,15,81,82,144,145,],[10,11,12,14,17,22,23,37,38,60,62,63,65,90,92,]),
      ([10,11,12,14,16,22,23,37,38,60,62,63,65,90,92,],[15,18,20,24,26,123,125,129,131,]),
      ([19,91,92,96,97,102,103,139,140,],[15,17,20,24,26,123,125,129,131,]),
      ([18,91,92,96,97,102,103,139,140,],[20,52,53,127,128,136,137,148,149,]),
      ([19,52,53,127,128,136,137,148,149,],[15,17,18,24,26,123,125,129,131,]),
      ([6,7,22,48,49,132,133,],[23,45,47,51,53,54,56,69,71,93,95,108,110,]),
      ([6,7,21,48,49,132,133,],[10,11,12,14,16,17,23,37,38,60,62,63,65,90,92,]),
      ([10,11,12,14,16,17,22,37,38,60,62,63,65,90,92,],[21,45,47,51,53,54,56,69,71,93,95,108,110,]),
      ([25,66,67,138,139,],[15,17,18,20,26,123,125,129,131,]),
      ([24,66,67,138,139,],[0,2,4,5,26,70,71,97,98,105,107,]),
      ([0,2,4,5,25,70,71,97,98,105,107,],[15,17,18,20,24,123,125,129,131,]),
      ([28,36,37,51,52,123,124,],[29,39,41,66,68,72,74,114,116,]),
      ([27,36,37,51,52,123,124,],[29,94,95,100,101,103,104,106,107,121,122,133,134,142,143,145,146,]),
      ([28,94,95,100,101,103,104,106,107,121,122,133,134,142,143,145,146,],[27,39,41,66,68,72,74,114,116,]),
      ([31,33,34,64,65,],[32,55,56,82,83,118,119,124,125,138,140,]),
      ([30,33,34,64,65,],[1,2,9,10,32,57,58,67,68,135,136,]),
      ([1,2,9,10,31,57,58,67,68,135,136,],[30,55,56,82,83,118,119,124,125,138,140,]),
      ([30,31,34,64,65,],[35,58,59,88,89,102,104,109,110,]),
      ([30,31,33,64,65,],[13,14,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,]),
      ([13,14,34,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,],[33,58,59,88,89,102,104,109,110,]),
      ([27,28,37,51,52,123,124,],[38,75,77,78,80,120,122,]),
      ([27,28,36,51,52,123,124,],[10,11,12,14,16,17,22,23,38,60,62,63,65,90,92,]),
      ([10,11,12,14,16,17,22,23,37,60,62,63,65,90,92,],[36,75,77,78,80,120,122,]),
      ([40,60,61,75,76,141,142,],[27,29,41,66,68,72,74,114,116,]),
      ([39,60,61,75,76,141,142,],[7,8,12,13,41,79,80,85,86,87,88,147,148,]),
      ([7,8,12,13,40,79,80,85,86,87,88,147,148,],[27,29,39,66,68,72,74,114,116,]),
      ([43,63,64,78,79,],[44,81,83,87,89,126,128,]),
      ([42,63,64,78,79,],[13,14,34,35,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,]),
      ([13,14,34,35,43,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,],[42,81,83,87,89,126,128,]),
      ([46,114,115,],[21,23,47,51,53,54,56,69,71,93,95,108,110,]),
      ([45,114,115,],[13,14,34,35,43,44,47,49,50,73,74,76,77,105,106,112,113,117,118,129,130,]),
      ([13,14,34,35,43,44,46,49,50,73,74,76,77,105,106,112,113,117,118,129,130,],[21,23,45,51,53,54,56,69,71,93,95,108,110,]),
      ([6,7,21,22,49,132,133,],[50,144,146,]),
      ([6,7,21,22,48,132,133,],[13,14,34,35,43,44,46,47,50,73,74,76,77,105,106,112,113,117,118,129,130,]),
      ([13,14,34,35,43,44,46,47,49,73,74,76,77,105,106,112,113,117,118,129,130,],[48,144,146,]),
      ([27,28,36,37,52,123,124,],[21,23,45,47,53,54,56,69,71,93,95,108,110,]),
      ([27,28,36,37,51,123,124,],[19,20,53,127,128,136,137,148,149,]),
      ([19,20,52,127,128,136,137,148,149,],[21,23,45,47,51,54,56,69,71,93,95,108,110,]),
      ([55,72,73,90,91,120,121,],[21,23,45,47,51,53,56,69,71,93,95,108,110,]),
      ([54,72,73,90,91,120,121,],[30,32,56,82,83,118,119,124,125,138,140,]),
      ([30,32,55,82,83,118,119,124,125,138,140,],[21,23,45,47,51,53,54,69,71,93,95,108,110,]),
      ([1,2,9,10,31,32,58,67,68,135,136,],[59,111,113,141,143,147,149,]),
      ([1,2,9,10,31,32,57,67,68,135,136,],[33,35,59,88,89,102,104,109,110,]),
      ([33,35,58,88,89,102,104,109,110,],[57,111,113,141,143,147,149,]),
      ([39,40,61,75,76,141,142,],[10,11,12,14,16,17,22,23,37,38,62,63,65,90,92,]),
      ([39,40,60,75,76,141,142,],[0,1,62,99,100,108,109,115,116,126,127,]),
      ([0,1,61,99,100,108,109,115,116,126,127,],[10,11,12,14,16,17,22,23,37,38,60,63,65,90,92,]),
      ([42,43,64,78,79,],[10,11,12,14,16,17,22,23,37,38,60,62,65,90,92,]),
      ([42,43,63,78,79,],[30,31,33,34,65,]),
      ([30,31,33,34,64,],[10,11,12,14,16,17,22,23,37,38,60,62,63,90,92,]),
      ([24,25,67,138,139,],[27,29,39,41,68,72,74,114,116,]),
      ([24,25,66,138,139,],[1,2,9,10,31,32,57,58,68,135,136,]),
      ([1,2,9,10,31,32,57,58,67,135,136,],[27,29,39,41,66,72,74,114,116,]),
      ([70,],[21,23,45,47,51,53,54,56,71,93,95,108,110,]),
      ([69,],[0,2,4,5,25,26,71,97,98,105,107,]),
      ([0,2,4,5,25,26,70,97,98,105,107,],[21,23,45,47,51,53,54,56,69,93,95,108,110,]),
      ([54,55,73,90,91,120,121,],[27,29,39,41,66,68,74,114,116,]),
      ([54,55,72,90,91,120,121,],[13,14,34,35,43,44,46,47,49,50,74,76,77,105,106,112,113,117,118,129,130,]),
      ([13,14,34,35,43,44,46,47,49,50,73,76,77,105,106,112,113,117,118,129,130,],[27,29,39,41,66,68,72,114,116,]),
      ([39,40,60,61,76,141,142,],[36,38,77,78,80,120,122,]),
      ([39,40,60,61,75,141,142,],[13,14,34,35,43,44,46,47,49,50,73,74,77,105,106,112,113,117,118,129,130,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,105,106,112,113,117,118,129,130,],[36,38,75,78,80,120,122,]),
      ([42,43,63,64,79,],[36,38,75,77,80,120,122,]),
      ([42,43,63,64,78,],[7,8,12,13,40,41,80,85,86,87,88,147,148,]),
      ([7,8,12,13,40,41,79,85,86,87,88,147,148,],[36,38,75,77,78,120,122,]),
      ([3,4,15,16,82,144,145,],[42,44,83,87,89,126,128,]),
      ([3,4,15,16,81,144,145,],[30,32,55,56,83,118,119,124,125,138,140,]),
      ([30,32,55,56,82,118,119,124,125,138,140,],[42,44,81,87,89,126,128,]),
      ([85,93,94,111,112,],[86,117,119,]),
      ([84,93,94,111,112,],[7,8,12,13,40,41,79,80,86,87,88,147,148,]),
      ([7,8,12,13,40,41,79,80,85,87,88,147,148,],[84,117,119,]),
      ([7,8,12,13,40,41,79,80,85,86,88,147,148,],[42,44,81,83,89,126,128,]),
      ([7,8,12,13,40,41,79,80,85,86,87,147,148,],[33,35,58,59,89,102,104,109,110,]),
      ([33,35,58,59,88,102,104,109,110,],[42,44,81,83,87,126,128,]),
      ([54,55,72,73,91,120,121,],[10,11,12,14,16,17,22,23,37,38,60,62,63,65,92,]),
      ([54,55,72,73,90,120,121,],[18,19,92,96,97,102,103,139,140,]),
      ([18,19,91,96,97,102,103,139,140,],[10,11,12,14,16,17,22,23,37,38,60,62,63,65,90,]),
      ([84,85,94,111,112,],[21,23,45,47,51,53,54,56,69,71,95,108,110,]),
      ([84,85,93,111,112,],[28,29,95,100,101,103,104,106,107,121,122,133,134,142,143,145,146,]),
      ([28,29,94,100,101,103,104,106,107,121,122,133,134,142,143,145,146,],[21,23,45,47,51,53,54,56,69,71,93,108,110,]),
      ([18,19,91,92,97,102,103,139,140,],[6,8,9,11,98,99,101,130,131,]),
      ([18,19,91,92,96,102,103,139,140,],[0,2,4,5,25,26,70,71,98,105,107,]),
      ([0,2,4,5,25,26,70,71,97,105,107,],[6,8,9,11,96,99,101,130,131,]),
      ([0,1,61,62,100,108,109,115,116,126,127,],[6,8,9,11,96,98,101,130,131,]),
      ([0,1,61,62,99,108,109,115,116,126,127,],[28,29,94,95,101,103,104,106,107,121,122,133,134,142,143,145,146,]),
      ([28,29,94,95,100,103,104,106,107,121,122,133,134,142,143,145,146,],[6,8,9,11,96,98,99,130,131,]),
      ([18,19,91,92,96,97,103,139,140,],[33,35,58,59,88,89,104,109,110,]),
      ([18,19,91,92,96,97,102,139,140,],[28,29,94,95,100,101,104,106,107,121,122,133,134,142,143,145,146,]),
      ([28,29,94,95,100,101,103,106,107,121,122,133,134,142,143,145,146,],[33,35,58,59,88,89,102,109,110,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,106,112,113,117,118,129,130,],[0,2,4,5,25,26,70,71,97,98,107,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,112,113,117,118,129,130,],[28,29,94,95,100,101,103,104,107,121,122,133,134,142,143,145,146,]),
      ([28,29,94,95,100,101,103,104,106,121,122,133,134,142,143,145,146,],[0,2,4,5,25,26,70,71,97,98,105,]),
      ([0,1,61,62,99,100,109,115,116,126,127,],[21,23,45,47,51,53,54,56,69,71,93,95,110,]),
      ([0,1,61,62,99,100,108,115,116,126,127,],[33,35,58,59,88,89,102,104,110,]),
      ([33,35,58,59,88,89,102,104,109,],[21,23,45,47,51,53,54,56,69,71,93,95,108,]),
      ([84,85,93,94,112,],[57,59,113,141,143,147,149,]),
      ([84,85,93,94,111,],[13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,113,117,118,129,130,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,117,118,129,130,],[57,59,111,141,143,147,149,]),
      ([45,46,115,],[27,29,39,41,66,68,72,74,116,]),
      ([45,46,114,],[0,1,61,62,99,100,108,109,116,126,127,]),
      ([0,1,61,62,99,100,108,109,115,126,127,],[27,29,39,41,66,68,72,74,114,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,118,129,130,],[84,86,119,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,129,130,],[30,32,55,56,82,83,119,124,125,138,140,]),
      ([30,32,55,56,82,83,118,124,125,138,140,],[84,86,117,]),
      ([54,55,72,73,90,91,121,],[36,38,75,77,78,80,122,]),
      ([54,55,72,73,90,91,120,],[28,29,94,95,100,101,103,104,106,107,122,133,134,142,143,145,146,]),
      ([28,29,94,95,100,101,103,104,106,107,121,133,134,142,143,145,146,],[36,38,75,77,78,80,120,]),
      ([27,28,36,37,51,52,124,],[15,17,18,20,24,26,125,129,131,]),
      ([27,28,36,37,51,52,123,],[30,32,55,56,82,83,118,119,125,138,140,]),
      ([30,32,55,56,82,83,118,119,124,138,140,],[15,17,18,20,24,26,123,129,131,]),
      ([0,1,61,62,99,100,108,109,115,116,127,],[42,44,81,83,87,89,128,]),
      ([0,1,61,62,99,100,108,109,115,116,126,],[19,20,52,53,128,136,137,148,149,]),
      ([19,20,52,53,127,136,137,148,149,],[42,44,81,83,87,89,126,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,130,],[15,17,18,20,24,26,123,125,131,]),
      ([13,14,34,35,43,44,46,47,49,50,73,74,76,77,105,106,112,113,117,118,129,],[6,8,9,11,96,98,99,101,131,]),
      ([6,8,9,11,96,98,99,101,130,],[15,17,18,20,24,26,123,125,129,]),
      ([6,7,21,22,48,49,133,],[3,5,134,135,137,]),
      ([6,7,21,22,48,49,132,],[28,29,94,95,100,101,103,104,106,107,121,122,134,142,143,145,146,]),
      ([28,29,94,95,100,101,103,104,106,107,121,122,133,142,143,145,146,],[3,5,132,135,137,]),
      ([1,2,9,10,31,32,57,58,67,68,136,],[3,5,132,134,137,]),
      ([1,2,9,10,31,32,57,58,67,68,135,],[19,20,52,53,127,128,137,148,149,]),
      ([19,20,52,53,127,128,136,148,149,],[3,5,132,134,135,]),
      ([24,25,66,67,139,],[30,32,55,56,82,83,118,119,124,125,140,]),
      ([24,25,66,67,138,],[18,19,91,92,96,97,102,103,140,]),
      ([18,19,91,92,96,97,102,103,139,],[30,32,55,56,82,83,118,119,124,125,138,]),
      ([39,40,60,61,75,76,142,],[57,59,111,113,143,147,149,]),
      ([39,40,60,61,75,76,141,],[28,29,94,95,100,101,103,104,106,107,121,122,133,134,143,145,146,]),
      ([28,29,94,95,100,101,103,104,106,107,121,122,133,134,142,145,146,],[57,59,111,113,141,147,149,]),
      ([3,4,15,16,81,82,145,],[48,50,146,]),
      ([3,4,15,16,81,82,144,],[28,29,94,95,100,101,103,104,106,107,121,122,133,134,142,143,146,]),
      ([28,29,94,95,100,101,103,104,106,107,121,122,133,134,142,143,145,],[48,50,144,]),
      ([7,8,12,13,40,41,79,80,85,86,87,88,148,],[57,59,111,113,141,143,149,]),
      ([7,8,12,13,40,41,79,80,85,86,87,88,147,],[19,20,52,53,127,128,136,137,149,]),
      ([19,20,52,53,127,128,136,137,148,],[57,59,111,113,141,143,147,]),]

      return [G],hint 
    
    elif n==40:

      G=[([15,16,72,73,159,160,],[2,45,47,88,89,90,92,105,107,]),
      ([15,16,72,73,159,160,],[2,102,103,115,116,117,118,124,125,]),
      ([1,102,103,115,116,117,118,124,125,],[0,45,47,88,89,90,92,105,107,]),
      ([4,48,49,141,142,],[5,57,59,117,119,156,158,]),
      ([3,48,49,141,142,],[5,13,14,18,20,55,56,85,86,138,140,154,155,160,161,]),
      ([4,13,14,18,20,55,56,85,86,138,140,154,155,160,161,],[3,57,59,117,119,156,158,]),
      ([7,24,25,138,139,162,163,],[8,40,41,72,74,96,98,118,119,129,131,144,146,]),
      ([6,24,25,138,139,162,163,],[8,34,35,126,127,]),
      ([7,34,35,126,127,],[6,40,41,72,74,96,98,118,119,129,131,144,146,]),
      ([10,54,55,90,91,171,172,],[11,30,32,63,65,]),
      ([9,54,55,90,91,171,172,],[11,79,80,82,83,109,110,148,149,]),
      ([10,79,80,82,83,109,110,148,149,],[9,30,32,63,65,]),
      ([13,25,26,97,98,106,107,121,122,133,134,],[14,33,35,111,113,178,179,]),
      ([12,25,26,97,98,106,107,121,122,133,134,],[4,5,14,18,20,55,56,85,86,138,140,154,155,160,161,]),
      ([4,5,13,18,20,55,56,85,86,138,140,154,155,160,161,],[12,33,35,111,113,178,179,]),
      ([0,1,16,72,73,159,160,],[17,102,104,]),
      ([0,1,15,72,73,159,160,],[17,18,19,60,61,70,71,91,92,145,146,165,166,177,178,]),
      ([16,18,19,60,61,70,71,91,92,145,146,165,166,177,178,],[15,102,104,]),
      ([16,17,19,60,61,70,71,91,92,145,146,165,166,177,178,],[4,5,13,14,20,55,56,85,86,138,140,154,155,160,161,]),
      ([16,17,18,60,61,70,71,91,92,145,146,165,166,177,178,],[20,28,29,39,40,42,43,45,46,76,77,94,95,142,143,172,173,]),
      ([19,28,29,39,40,42,43,45,46,76,77,94,95,142,143,172,173,],[4,5,13,14,18,55,56,85,86,138,140,154,155,160,161,]),
      ([22,73,74,136,137,169,170,],[23,36,38,108,110,120,122,153,155,171,173,]),
      ([21,73,74,136,137,169,170,],[23,31,32,46,47,52,53,103,104,112,113,157,158,166,167,]),
      ([22,31,32,46,47,52,53,103,104,112,113,157,158,166,167,],[21,36,38,108,110,120,122,153,155,171,173,]),
      ([6,7,25,138,139,162,163,],[26,39,41,78,80,84,86,177,179,]),
      ([6,7,24,138,139,162,163,],[12,13,26,97,98,106,107,121,122,133,134,]),
      ([12,13,25,97,98,106,107,121,122,133,134,],[24,39,41,78,80,84,86,177,179,]),
      ([28,120,121,147,148,168,169,],[29,48,50,51,53,126,128,]),
      ([27,120,121,147,148,168,169,],[19,20,29,39,40,42,43,45,46,76,77,94,95,142,143,172,173,]),
      ([19,20,28,39,40,42,43,45,46,76,77,94,95,142,143,172,173,],[27,48,50,51,53,126,128,]),
      ([31,139,140,],[9,11,32,63,65,]),
      ([30,139,140,],[22,23,32,46,47,52,53,103,104,112,113,157,158,166,167,]),
      ([22,23,31,46,47,52,53,103,104,112,113,157,158,166,167,],[9,11,30,63,65,]),
      ([34,57,58,81,82,114,115,135,136,],[12,14,35,111,113,178,179,]),
      ([33,57,58,81,82,114,115,135,136,],[7,8,35,126,127,]),
      ([7,8,34,126,127,],[12,14,33,111,113,178,179,]),
      ([37,69,70,84,85,93,94,105,106,123,124,],[21,23,38,108,110,120,122,153,155,171,173,]),
      ([36,69,70,84,85,93,94,105,106,123,124,],[38,49,50,58,59,61,62,66,67,87,88,100,101,111,112,130,131,163,164,]),
      ([37,49,50,58,59,61,62,66,67,87,88,100,101,111,112,130,131,163,164,],[21,23,36,108,110,120,122,153,155,171,173,]),
      ([19,20,28,29,40,42,43,45,46,76,77,94,95,142,143,172,173,],[24,26,41,78,80,84,86,177,179,]),
      ([19,20,28,29,39,42,43,45,46,76,77,94,95,142,143,172,173,],[6,8,41,72,74,96,98,118,119,129,131,144,146,]),
      ([6,8,40,72,74,96,98,118,119,129,131,144,146,],[24,26,39,78,80,84,86,177,179,]),
      ([19,20,28,29,39,40,43,45,46,76,77,94,95,142,143,172,173,],[44,67,68,135,137,165,167,]),
      ([19,20,28,29,39,40,42,45,46,76,77,94,95,142,143,172,173,],[44,60,62,64,65,123,125,127,128,151,152,]),
      ([43,60,62,64,65,123,125,127,128,151,152,],[42,67,68,135,137,165,167,]),
      ([19,20,28,29,39,40,42,43,46,76,77,94,95,142,143,172,173,],[0,2,47,88,89,90,92,105,107,]),
      ([19,20,28,29,39,40,42,43,45,76,77,94,95,142,143,172,173,],[22,23,31,32,47,52,53,103,104,112,113,157,158,166,167,]),
      ([22,23,31,32,46,52,53,103,104,112,113,157,158,166,167,],[0,2,45,88,89,90,92,105,107,]),
      ([3,4,49,141,142,],[27,29,50,51,53,126,128,]),
      ([3,4,48,141,142,],[37,38,50,58,59,61,62,66,67,87,88,100,101,111,112,130,131,163,164,]),
      ([37,38,49,58,59,61,62,66,67,87,88,100,101,111,112,130,131,163,164,],[27,29,48,51,53,126,128,]),
      ([52,75,76,129,130,],[27,29,48,50,53,126,128,]),
      ([51,75,76,129,130,],[22,23,31,32,46,47,53,103,104,112,113,157,158,166,167,]),
      ([22,23,31,32,46,47,52,103,104,112,113,157,158,166,167,],[27,29,48,50,51,126,128,]),
      ([9,10,55,90,91,171,172,],[56,87,89,]),
      ([9,10,54,90,91,171,172,],[4,5,13,14,18,20,56,85,86,138,140,154,155,160,161,]),
      ([4,5,13,14,18,20,55,85,86,138,140,154,155,160,161,],[54,87,89,]),
      ([33,34,58,81,82,114,115,135,136,],[3,5,59,117,119,156,158,]),
      ([33,34,57,81,82,114,115,135,136,],[37,38,49,50,59,61,62,66,67,87,88,100,101,111,112,130,131,163,164,]),
      ([37,38,49,50,58,61,62,66,67,87,88,100,101,111,112,130,131,163,164,],[3,5,57,117,119,156,158,]),
      ([16,17,18,19,61,70,71,91,92,145,146,165,166,177,178,],[43,44,62,64,65,123,125,127,128,151,152,]),
      ([16,17,18,19,60,70,71,91,92,145,146,165,166,177,178,],[37,38,49,50,58,59,62,66,67,87,88,100,101,111,112,130,131,163,164,]),
      ([37,38,49,50,58,59,61,66,67,87,88,100,101,111,112,130,131,163,164,],[43,44,60,64,65,123,125,127,128,151,152,]),
      ([64,153,154,174,175,],[9,11,30,32,65,]),
      ([63,153,154,174,175,],[43,44,60,62,65,123,125,127,128,151,152,]),
      ([43,44,60,62,64,123,125,127,128,151,152,],[9,11,30,32,63,]),
      ([37,38,49,50,58,59,61,62,67,87,88,100,101,111,112,130,131,163,164,],[68,147,149,174,176,]),
      ([37,38,49,50,58,59,61,62,66,87,88,100,101,111,112,130,131,163,164,],[42,44,68,135,137,165,167,]),
      ([42,44,67,135,137,165,167,],[66,147,149,174,176,]),
      ([36,37,70,84,85,93,94,105,106,123,124,],[71,75,77,168,170,175,176,]),
      ([36,37,69,84,85,93,94,105,106,123,124,],[16,17,18,19,60,61,71,91,92,145,146,165,166,177,178,]),
      ([16,17,18,19,60,61,70,91,92,145,146,165,166,177,178,],[69,75,77,168,170,175,176,]),
      ([0,1,15,16,73,159,160,],[6,8,40,41,74,96,98,118,119,129,131,144,146,]),
      ([0,1,15,16,72,159,160,],[21,22,74,136,137,169,170,]),
      ([21,22,73,136,137,169,170,],[6,8,40,41,72,96,98,118,119,129,131,144,146,]),
      ([51,52,76,129,130,],[69,71,77,168,170,175,176,]),
      ([51,52,75,129,130,],[19,20,28,29,39,40,42,43,45,46,77,94,95,142,143,172,173,]),
      ([19,20,28,29,39,40,42,43,45,46,76,94,95,142,143,172,173,],[69,71,75,168,170,175,176,]),
      ([79,144,145,150,151,156,157,],[24,26,39,41,80,84,86,177,179,]),
      ([78,144,145,150,151,156,157,],[10,11,80,82,83,109,110,148,149,]),
      ([10,11,79,82,83,109,110,148,149,],[24,26,39,41,78,84,86,177,179,]),
      ([33,34,57,58,82,114,115,135,136,],[83,150,152,159,161,162,164,]),
      ([33,34,57,58,81,114,115,135,136,],[10,11,79,80,83,109,110,148,149,]),
      ([10,11,79,80,82,109,110,148,149,],[81,150,152,159,161,162,164,]),
      ([36,37,69,70,85,93,94,105,106,123,124,],[24,26,39,41,78,80,86,177,179,]),
      ([36,37,69,70,84,93,94,105,106,123,124,],[4,5,13,14,18,20,55,56,86,138,140,154,155,160,161,]),
      ([4,5,13,14,18,20,55,56,85,138,140,154,155,160,161,],[24,26,39,41,78,80,84,177,179,]),
      ([37,38,49,50,58,59,61,62,66,67,88,100,101,111,112,130,131,163,164,],[54,56,89,]),
      ([37,38,49,50,58,59,61,62,66,67,87,100,101,111,112,130,131,163,164,],[0,2,45,47,89,90,92,105,107,]),
      ([0,2,45,47,88,90,92,105,107,],[54,56,87,]),
      ([9,10,54,55,91,171,172,],[0,2,45,47,88,89,92,105,107,]),
      ([9,10,54,55,90,171,172,],[16,17,18,19,60,61,70,71,92,145,146,165,166,177,178,]),
      ([16,17,18,19,60,61,70,71,91,145,146,165,166,177,178,],[0,2,45,47,88,89,90,105,107,]),
      ([36,37,69,70,84,85,94,105,106,123,124,],[95,99,101,114,116,]),
      ([36,37,69,70,84,85,93,105,106,123,124,],[19,20,28,29,39,40,42,43,45,46,76,77,95,142,143,172,173,]),
      ([19,20,28,29,39,40,42,43,45,46,76,77,94,142,143,172,173,],[93,99,101,114,116,]),
      ([97,99,100,108,109,],[6,8,40,41,72,74,98,118,119,129,131,144,146,]),
      ([96,99,100,108,109,],[12,13,25,26,98,106,107,121,122,133,134,]),
      ([12,13,25,26,97,106,107,121,122,133,134,],[6,8,40,41,72,74,96,118,119,129,131,144,146,]),
      ([96,97,100,108,109,],[93,95,101,114,116,]),
      ([96,97,99,108,109,],[37,38,49,50,58,59,61,62,66,67,87,88,101,111,112,130,131,163,164,]),
      ([37,38,49,50,58,59,61,62,66,67,87,88,100,111,112,130,131,163,164,],[93,95,99,114,116,]),
      ([1,2,103,115,116,117,118,124,125,],[15,17,104,]),
      ([1,2,102,115,116,117,118,124,125,],[22,23,31,32,46,47,52,53,104,112,113,157,158,166,167,]),
      ([22,23,31,32,46,47,52,53,103,112,113,157,158,166,167,],[15,17,102,]),
      ([36,37,69,70,84,85,93,94,106,123,124,],[0,2,45,47,88,89,90,92,107,]),
      ([36,37,69,70,84,85,93,94,105,123,124,],[12,13,25,26,97,98,107,121,122,133,134,]),
      ([12,13,25,26,97,98,106,121,122,133,134,],[0,2,45,47,88,89,90,92,105,]),
      ([96,97,99,100,109,],[21,23,36,38,110,120,122,153,155,171,173,]),
      ([96,97,99,100,108,],[10,11,79,80,82,83,110,148,149,]),
      ([10,11,79,80,82,83,109,148,149,],[21,23,36,38,108,120,122,153,155,171,173,]),
      ([37,38,49,50,58,59,61,62,66,67,87,88,100,101,112,130,131,163,164,],[12,14,33,35,113,178,179,]),
      ([37,38,49,50,58,59,61,62,66,67,87,88,100,101,111,130,131,163,164,],[22,23,31,32,46,47,52,53,103,104,113,157,158,166,167,]),
      ([22,23,31,32,46,47,52,53,103,104,112,157,158,166,167,],[12,14,33,35,111,178,179,]),
      ([33,34,57,58,81,82,115,135,136,],[93,95,99,101,116,]),
      ([33,34,57,58,81,82,114,135,136,],[1,2,102,103,116,117,118,124,125,]),
      ([1,2,102,103,115,117,118,124,125,],[93,95,99,101,114,]),
      ([1,2,102,103,115,116,118,124,125,],[3,5,57,59,119,156,158,]),
      ([1,2,102,103,115,116,117,124,125,],[6,8,40,41,72,74,96,98,119,129,131,144,146,]),
      ([6,8,40,41,72,74,96,98,118,129,131,144,146,],[3,5,57,59,117,156,158,]),
      ([27,28,121,147,148,168,169,],[21,23,36,38,108,110,122,153,155,171,173,]),
      ([27,28,120,147,148,168,169,],[12,13,25,26,97,98,106,107,122,133,134,]),
      ([12,13,25,26,97,98,106,107,121,133,134,],[21,23,36,38,108,110,120,153,155,171,173,]),
      ([36,37,69,70,84,85,93,94,105,106,124,],[43,44,60,62,64,65,125,127,128,151,152,]),
      ([36,37,69,70,84,85,93,94,105,106,123,],[1,2,102,103,115,116,117,118,125,]),
      ([1,2,102,103,115,116,117,118,124,],[43,44,60,62,64,65,123,127,128,151,152,]),
      ([7,8,34,35,127,],[27,29,48,50,51,53,128,]),
      ([7,8,34,35,126,],[43,44,60,62,64,65,123,125,128,151,152,]),
      ([43,44,60,62,64,65,123,125,127,151,152,],[27,29,48,50,51,53,126,]),
      ([51,52,75,76,130,],[6,8,40,41,72,74,96,98,118,119,131,144,146,]),
      ([51,52,75,76,129,],[37,38,49,50,58,59,61,62,66,67,87,88,100,101,111,112,131,163,164,]),
      ([37,38,49,50,58,59,61,62,66,67,87,88,100,101,111,112,130,163,164,],[6,8,40,41,72,74,96,98,118,119,129,144,146,]),
      ([133,],[134,141,143,]),
      ([132,],[12,13,25,26,97,98,106,107,121,122,134,]),
      ([12,13,25,26,97,98,106,107,121,122,133,],[132,141,143,]),
      ([33,34,57,58,81,82,114,115,136,],[42,44,67,68,137,165,167,]),
      ([33,34,57,58,81,82,114,115,135,],[21,22,73,74,137,169,170,]),
      ([21,22,73,74,136,169,170,],[42,44,67,68,135,165,167,]),
      ([6,7,24,25,139,162,163,],[4,5,13,14,18,20,55,56,85,86,140,154,155,160,161,]),
      ([6,7,24,25,138,162,163,],[30,31,140,]),
      ([30,31,139,],[4,5,13,14,18,20,55,56,85,86,138,154,155,160,161,]),
      ([3,4,48,49,142,],[132,134,143,]),
      ([3,4,48,49,141,],[19,20,28,29,39,40,42,43,45,46,76,77,94,95,143,172,173,]),
      ([19,20,28,29,39,40,42,43,45,46,76,77,94,95,142,172,173,],[132,134,141,]),
      ([78,79,145,150,151,156,157,],[6,8,40,41,72,74,96,98,118,119,129,131,146,]),
      ([78,79,144,150,151,156,157,],[16,17,18,19,60,61,70,71,91,92,146,165,166,177,178,]),
      ([16,17,18,19,60,61,70,71,91,92,145,165,166,177,178,],[6,8,40,41,72,74,96,98,118,119,129,131,144,]),
      ([27,28,120,121,148,168,169,],[66,68,149,174,176,]),
      ([27,28,120,121,147,168,169,],[10,11,79,80,82,83,109,110,149,]),
      ([10,11,79,80,82,83,109,110,148,],[66,68,147,174,176,]),
      ([78,79,144,145,151,156,157,],[81,83,152,159,161,162,164,]),
      ([78,79,144,145,150,156,157,],[43,44,60,62,64,65,123,125,127,128,152,]),
      ([43,44,60,62,64,65,123,125,127,128,151,],[81,83,150,159,161,162,164,]),
      ([63,64,154,174,175,],[21,23,36,38,108,110,120,122,155,171,173,]),
      ([63,64,153,174,175,],[4,5,13,14,18,20,55,56,85,86,138,140,155,160,161,]),
      ([4,5,13,14,18,20,55,56,85,86,138,140,154,160,161,],[21,23,36,38,108,110,120,122,153,171,173,]),
      ([78,79,144,145,150,151,157,],[3,5,57,59,117,119,158,]),
      ([78,79,144,145,150,151,156,],[22,23,31,32,46,47,52,53,103,104,112,113,158,166,167,]),
      ([22,23,31,32,46,47,52,53,103,104,112,113,157,166,167,],[3,5,57,59,117,119,156,]),
      ([0,1,15,16,72,73,160,],[81,83,150,152,161,162,164,]),
      ([0,1,15,16,72,73,159,],[4,5,13,14,18,20,55,56,85,86,138,140,154,155,161,]),
      ([4,5,13,14,18,20,55,56,85,86,138,140,154,155,160,],[81,83,150,152,159,162,164,]),
      ([6,7,24,25,138,139,163,],[81,83,150,152,159,161,164,]),
      ([6,7,24,25,138,139,162,],[37,38,49,50,58,59,61,62,66,67,87,88,100,101,111,112,130,131,164,]),
      ([37,38,49,50,58,59,61,62,66,67,87,88,100,101,111,112,130,131,163,],[81,83,150,152,159,161,162,]),
      ([16,17,18,19,60,61,70,71,91,92,145,146,166,177,178,],[42,44,67,68,135,137,167,]),
      ([16,17,18,19,60,61,70,71,91,92,145,146,165,177,178,],[22,23,31,32,46,47,52,53,103,104,112,113,157,158,167,]),
      ([22,23,31,32,46,47,52,53,103,104,112,113,157,158,166,],[42,44,67,68,135,137,165,]),
      ([27,28,120,121,147,148,169,],[69,71,75,77,170,175,176,]),
      ([27,28,120,121,147,148,168,],[21,22,73,74,136,137,170,]),
      ([21,22,73,74,136,137,169,],[69,71,75,77,168,175,176,]),
      ([9,10,54,55,90,91,172,],[21,23,36,38,108,110,120,122,153,155,173,]),
      ([9,10,54,55,90,91,171,],[19,20,28,29,39,40,42,43,45,46,76,77,94,95,142,143,173,]),
      ([19,20,28,29,39,40,42,43,45,46,76,77,94,95,142,143,172,],[21,23,36,38,108,110,120,122,153,155,171,]),
      ([63,64,153,154,175,],[66,68,147,149,176,]),
      ([63,64,153,154,174,],[69,71,75,77,168,170,176,]),
      ([69,71,75,77,168,170,175,],[66,68,147,149,174,]),
      ([16,17,18,19,60,61,70,71,91,92,145,146,165,166,178,],[24,26,39,41,78,80,84,86,179,]),
      ([16,17,18,19,60,61,70,71,91,92,145,146,165,166,177,],[12,14,33,35,111,113,179,]),
      ([12,14,33,35,111,113,178,],[24,26,39,41,78,80,84,86,177,]),]

      return [G],hint 



    exit()
