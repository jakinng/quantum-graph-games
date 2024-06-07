from toqito.states import basis, bell
from toqito.state_props import is_ppt
import numpy as np

prob_mat = np.ones((2, 2)) * 1 / 4
S, T, A, B = 2, 2, 2, 2
pred_mat = np.zeros((S, T, A, B))
print(np.indices(pred_mat.shape))
print("hi its bea") 
print("test")
