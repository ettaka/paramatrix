import matplotlib.pyplot as plt
import numpy as np

def samplemat(dims):
    aa = np.zeros(dims)
    for i in range(min(dims)):
        aa[i,i]=i
    return aa

nof_partitions = 4
cm_arrays = []
max_coord_i = []
max_coord_j = []
min_coord_i = []
min_coord_j = []
cms = []
for i in range(nof_partitions):
    cm_arrays.append(np.loadtxt("cm"+str(i)))
    max_coord_i.append(0)
    max_coord_j.append(0)
    min_coord_i.append(0)
    min_coord_j.append(0)
    max_coord_i[i] = int(np.max(cm_arrays[i].transpose()[0]))
    max_coord_j[i] = int(np.max(cm_arrays[i].transpose()[1]))
    min_coord_i[i] = int(np.min(cm_arrays[i].transpose()[0]))
    min_coord_j[i] = int(np.min(cm_arrays[i].transpose()[1]))

print min_coord_i, min_coord_j, max_coord_i, max_coord_j

total_max_coord_i = max(max_coord_i)
total_max_coord_j = max(max_coord_j)
total_min_coord_i = min(min_coord_i)
total_min_coord_j = min(min_coord_j)

print total_min_coord_i, total_min_coord_j, total_max_coord_i, total_max_coord_j

for i in range(nof_partitions):
    cms.append(np.zeros((total_max_coord_i, total_max_coord_j)))
    for rows in cm_arrays[i]:
        j = int(rows[0])-1
        k = int(rows[1])-1
        value = rows[2]
        if np.abs(value) > 0.0001:
            cms[i][j][k] = i+1
    #plt.matshow(cms[i])
    #plt.matshow(cms[i][min_coord_i[i]:, min_coord_j[i]:])
    #plt.matshow(cms[i][max_coord[i][0]-10:, 0:])

total_cm = np.zeros((total_max_coord_i, total_max_coord_j))
for cm in cms:
    total_cm += cm

plt.matshow(total_cm)

plt.show()
