import numpy as np

# 純量(0D張量)
x = np.array(12) # 建立純量
print(x, x.ndim) # ndim查看階數

# 向量(1D張量)
x = np.array([1, 2, 3]) # 建立向量
print(x, x.ndim) # ndim查看階數

# 矩陣(2D張量)
x = np.array([[1, 2, 3], [4, 5, 6]]) # 建立矩陣
print(x, x.ndim) # ndim查看階數

# 三維張量(3D張量)
x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # 建立三維張量
print(x, x.ndim) # ndim查看階數