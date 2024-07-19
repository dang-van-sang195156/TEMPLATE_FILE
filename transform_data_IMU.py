import pandas as pd
import numpy as np

# Đọc dữ liệu từ file CSV ban đầu
input_file = 'lanq1-imu0.csv'  # Thay thế bằng tên file CSV của bạn
output_file = 'output_lanq1-imu0.csv'  # Tên file CSV để lưu dữ liệu đã xử lý

# Đọc dữ liệu từ file CSV
data = pd.read_csv(input_file, skiprows = 1)

header_C = data.iloc[:, 2].astype(float)
header_D = data.iloc[:, 3].astype(float)

 
qx= data.iloc[:, 5].astype(float)
qy= data.iloc[:, 6].astype(float)
qz= data.iloc[:, 7].astype(float)
qw= data.iloc[:, 8].astype(float)

def to_time(header_C, header_D):
    time_fake = header_C + header_D * 10**-9
    return time_fake

def quaternion_to_euler(q_w, q_x, q_y, q_z):
    # Tính toán phi
    phi = np.arctan2(2 * (q_w * q_x + q_y * q_z), 1 - 2 * (q_x**2 + q_y**2))

    # Tính toán theta
    sin_theta = 2 * (q_w * q_y - q_x * q_z)
    sin_theta = np.clip(sin_theta, -1.0, 1.0)  # Giới hạn giá trị nằm trong khoảng [-1, 1]
    theta = np.arcsin(sin_theta)

    # Tính toán psi
    psi = np.arctan2(2 * (q_w * q_z + q_x * q_y), 1 - 2 * (q_y**2 + q_z**2))

    return np.array([phi, theta, psi])

# Tính toán thời gian
time_fake = to_time(header_C, header_D)
# Lấy giá trị thời gian đầu tiên
first_time = time_fake[0]

# Tạo các cột mới để lưu kết quả
phi_list = []
theta_list = []
psi_list = []
time_list = []

# Lặp qua từng dòng dữ liệu
for i in range(len(data)):
    q_w = qw[i]
    q_x = qx[i]
    q_y = qy[i]
    q_z = qz[i]

    # Tính toán các góc Euler
    euler_angles = quaternion_to_euler(q_w, q_x, q_y, q_z)

    time = time_fake[i] - first_time

    # Lưu kết quả vào danh sách
    phi_list.append(euler_angles[0])
    theta_list.append(euler_angles[1])
    psi_list.append(euler_angles[2])
    time_list.append(time)

# Tạo DataFrame mới cho các góc Euler
euler_data = pd.DataFrame({
    't': time_list,
    'phi': phi_list,
    'theta': theta_list,
    'psi': psi_list
})


# Lưu DataFrame thành file CSV mới
euler_data.to_csv(output_file, index=False)
print("da chuyen !!!")