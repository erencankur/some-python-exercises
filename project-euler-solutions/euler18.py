import copy
from colorama import Fore, Style, init
init(autoreset = True)

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

copied_triangle = copy.deepcopy(triangle)
reversed_triangle = list(reversed(triangle))

for i in range(len(triangle)):
    for j in range(len(reversed_triangle[i])-1):
        reversed_triangle[i+1][j] += max(reversed_triangle[i][j],reversed_triangle[i][j+1])

path_list=[]
indexes_of_path_list=[]
indexes_of_path_list.append([0,0])

def index(i, j):
    n = triangle[i][j] - copied_triangle[i][j]
    path_list.append(copied_triangle[i][j])
    if i + 1 >= len(triangle):
        return
    k = triangle[i+1].index(n)
    indexes_of_path_list.append([i+1,k])
    index(i+1,k)
index(0, 0)

result_list = ' -> '.join(map(str, path_list))
print("\n" + Fore.GREEN + str(triangle[0][0]) + " = " + result_list + Style.RESET_ALL + "\n")

for i in indexes_of_path_list:
    copied_triangle[i[0]][i[1]] = Fore.RED + str(copied_triangle[i[0]][i[1]]) + Style.RESET_ALL

formatted_triangle = [
    [str(num).zfill(2) for num in row] # tek haneli sayıları iki haneye çıkarır
    for row in copied_triangle
]

max_width = len(' '.join(map(str, formatted_triangle[-1])))

for row in formatted_triangle:
    print(' '.join(map(str, row)).center(max_width))