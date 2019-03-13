# import numpy as np
#
# # g = [
# #     [1, 2],    # A
# #     [0, 2, 3], # B
# #     [0, 1, 4], # C
# #     [1, 4, 5], # D
# #     [2, 3, 6], # E
# #     [3],       # F
# #     [4]        # G
# # ]
#
a_list = [
    [1, 2],
    [3, 4],
    [4, 5],
    [6, 7],
    [7, 8],
    [8, 9],
    [],
    [],
    [],
    [],
]


# a_list = []
# for n in range(15):
#     for m in range(1,n+2):
#         if n == 14:
#             a_list.append([])
#         else:
#             a_list.append([int((n+1)*(n+2)/2)+(m-1), int((n+1)*(n+2)/2+m)])
#
# print(a_list)

def search(goal, path):
    n = path[-1]
    if n == goal:
        print(path)
    else:
        for x in a_list[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()


# for n in range(105,120):
#     search(n, [0])

search(9, [0])
