import os
import numpy as np

def merge_npy(file_n):
     rgb_path = 'flow'
     flow_path = 'rgb'
     data1 = np.load(os.path.join(rgb_path, file_n))
     data2 = np.load(os.path.join(flow_path, file_n))
     jmin = min(data1.shape[0], data2.shape[0])
     wmin = min(data1.shape[1], data2.shape[1])
     newshape = (jmin, wmin)
     data1 = np.resize(data1, newshape)
     data2 = np.resize(data2, newshape)
     np.save(os.path.join(rgb_path, file_n),data1)
     np.save(os.path.join(flow_path, file_n),data2)

if __name__ == '__main__':

    rgb_path = 'flow_feature_npz'

    for fi in os.listdir(rgb_path):
        merge_npy(fi)
