import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV ban đầu
input_file = 'output_lan3-imu0.csv'  # Tên file CSV để lưu dữ liệu đã xử lý

# Đọc dữ liệu từ file CSV
data = pd.read_csv(input_file, skiprows = 1)

t = data.iloc[:, 0].astype(float)
phi = data.iloc[:, 1].astype(float)
theta = data.iloc[:, 2].astype(float)
psi = data.iloc[:, 3].astype(float)

# print(t)

plt.figure()
plt.subplot(3,1,1)
plt.plot(t, phi)
plt.title("phi")
plt.subplot(3,1,2)
plt.plot(t, theta)
plt.title("theta")

plt.subplot(3,1,3)
plt.plot(t, psi)
plt.title("psi")

#plt.axis('equal')
plt.show()