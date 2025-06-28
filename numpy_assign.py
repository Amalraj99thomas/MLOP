import numpy as np

#---------------------------Question 1--------------------------------------
heights = np.array([160, 170, 180, 150, 165,
                    175, 165, 185, 160, 170,
                    155, 165, 160, 170, 180,
                    180, 190, 185, 175, 160])

# groups = np.split(heights, 4)

# for i, group in enumerate(groups):
#     mid_idx = np.argpartition(group,2)
#     mid_val = group[mid_idx][2]
#     print(f"Middle guy in Group {i+1}:", mid_val)


#---------------------------Question 2--------------------------------------

heights2 = np.array([160, 170, 180, 150,
                    175, 165, 185, 160,
                    155, 165, 160, 170])

# groups = np.split(heights2, 3)

# for i, group in enumerate(groups):
#     top2_idx = np.argpartition(group,1)
#     top2_val = group[top2_idx][2:]
#     print(f"Tallest two in Group {i+1}:", top2_val)


#---------------------------Question 4--------------------------------------

heights3 = np.array([160, 170, 180,
                    175, 185, 165,
                    155, 165, 150])

# groups = np.split(heights3, 3)

# for i, group in enumerate(groups):
#     top_idx = np.argpartition(group,1)
#     top_val = group[top_idx][2]
#     print(f"Tallest in Group {i+1}:", top_val)


#---------------------------Question 8--------------------------------------

heights8 = np.array([
                    160, 170, 150, 180, 165, 155,
                    175, 165, 185, 160, 170, 155
                    ])

# groups = np.split(heights8, 2)

# # median = avg of middle two for even
# for i, group in enumerate(groups):
#     mid1 = group[np.argpartition(group, 2)][2]
#     mid2 = group[np.argpartition(group, 3)][3]
#     median = (mid1 + mid2)/2
#     print(f"Median of group {i+1} is ", median)


#---------------------------Question 9--------------------------------------

heights9 = np.array([
                    160, 170, 150, 180, 165,
                    175, 185, 155, 160, 170
                    ])

# groups = np.split(heights9,2)

# for i, group in enumerate(groups):
#     tallest = group[np.argmax(group)]
#     shortest = group[np.argmin(group)]
#     gap = tallest - shortest
#     print(f"Gap in group {i+1} is", gap)


#---------------------------Question 10--------------------------------------

heights10 = np.array([
                    160, 170, 165,
                    180, 190, 175,
                    155, 160, 150
                    ])


groups = np.split(heights10, 3)

for i, group in enumerate(groups):
    # avg = (np.sum(group))/3
    print(group[np.argpartition(group,1)][1])