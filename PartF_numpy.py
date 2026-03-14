import numpy as np

# ======================================
# Part A: create arrays and basic operations
# 学习内容：
# np.array / np.arange / np.linspace
# 逐元素运算
# ======================================

a = np.array([1, 2, 3, 4, 5])              # 直接从列表创建数组
b = np.arange(0, 10)                       # 从 0 到 9
c = np.linspace(-1, 1, 5)                  # 在 -1 到 1 之间均匀取 5 个数
d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("===== Part A: basic arrays =====")
print("a =", a)
print("b =", b)
print("b + 1 =", b + 1)                    # 每个元素都加 1
print("b * 2 =", b * 2)                    # 每个元素都乘 2
print("b ** 2 =", b ** 2)                  # 每个元素平方
print("c =", c)
print("b + d =", b + d)                    # 两个同形状数组逐元素相加


# ======================================
# Part B: reshape / transpose / reductions
# 学习内容：
# reshape / T / sum / max / mean / axis
# ======================================

x = np.arange(12)
print("\n===== Part B: reshape and axis =====")
print("x =", x)

x = x.reshape(3, 4)                        # 变成 3 行 4 列
print("reshaped x =")
print(x)

t = x.T                                    # 转置：行列交换
print("transpose of x =")
print(t)

print("sum =", x.sum())                    # 所有元素求和
print("max =", x.max())                    # 所有元素最大值
print("mean =", x.mean())                  # 所有元素平均值

# axis=0 表示按列计算
# axis=1 表示按行计算
print("sum in columns =", x.sum(axis=0))
print("max in columns =", x.max(axis=0))
print("sum in rows =", x.sum(axis=1))
print("max in rows =", x.max(axis=1))


# ======================================
# Part C: boolean filtering and modifying arrays
# 学习内容：
# 布尔筛选 / 条件修改 / copy
# ======================================

x = np.arange(-5, 6)
print("\n===== Part C: boolean filtering =====")
print("x =", x)

print("positive numbers in x =", x[x > 0])         # 筛出正数
print("odd numbers =", x[x % 2 != 0])              # 筛出奇数
print("even numbers =", x[x % 2 == 0])             # 筛出偶数
print("abs > 3 =", x[np.abs(x) > 3])               # 绝对值大于 3 的元素

# 条件修改：把负数改成 0
x[x < 0] = 0
print("After changing negative numbers to 0:", x)

# copy 的作用：复制一份，不改原数组
x = np.arange(-5, 6)
y = x.copy()
y[y < 0] = 0
y[y > 0] = 100
print("y changed =", y)

x = np.arange(12)
z = x.copy()
z[z > 5] = 999
print("z changed =", z)


# ======================================
# Part D: zeros / ones / full / dtype
# 学习内容：
# 特殊数组创建 / 数据类型 dtype
# ======================================

a = np.zeros(5)                            # 5 个 0
b = np.ones(5)                             # 5 个 1
c = np.full(5, 7)                          # 5 个 7

d = np.array([1, 2, 3, 4], dtype=float)   # 指定为浮点数
e = np.array([1.8, 2.4, 3.5], dtype=int)  # 指定为整数，小数会被截掉

print("\n===== Part D: zeros / ones / full / dtype =====")
print("zeros:", a)
print("ones:", b)
print("full:", c)
print("d =", d)
print("d dtype =", d.dtype)
print("e =", e)
print("e dtype =", e.dtype)


# ======================================
# Part E: 2D slicing
# 学习内容：
# 二维数组切片
# ======================================

x = np.arange(12).reshape(3, 4)

print("\n===== Part E: 2D slicing =====")
print("x =")
print(x)

print("first row:", x[0])                  # 第 1 行
print("second row:", x[1])                 # 第 2 行
print("first column:", x[:, 0])            # 第 1 列
print("second column:", x[:, 1])           # 第 2 列

print("top-left corner:", x[0, 0])         # 左上角元素
print("last element:", x[2, 3])            # 最后一个元素

print("first two rows:")
print(x[0:2])                              # 前两行

print("last two columns:")
print(x[:, 2:])                            # 后两列

print("middle block:")
print(x[1:2, 1:3])                         # 按你的定义：中间这一小块


# ======================================
# Part F: argmax / argmin
# 学习内容：
# 最大值最小值及其位置
# ======================================

y = np.array([10, 3, 25, 8, 17])
z = np.array([[4, 9, 2],
              [8, 1, 6]])

print("\n===== Part F: argmax / argmin =====")
print("y =", y)
print("z =")
print(z)

print("max y =", y.max())                  # y 的最大值
print("min y =", y.min())                  # y 的最小值
print("argmax y =", y.argmax())            # y 最大值的位置
print("argmin y =", y.argmin())            # y 最小值的位置

print("max z =", z.max())                  # z 的最大值
print("argmax z =", z.argmax())            # z 最大值位置（按拉平后算）


# ======================================
# Part G: broadcasting
# 学习内容：
# 广播 broadcasting
# ======================================

a = np.array([1, 2, 3, 4])
b = np.array([[1], [2], [3]])
c = np.array([10, 20, 30])

print("\n===== Part G: broadcasting =====")
print("a =", a)
print("b =")
print(b)
print("c =", c)

print("a + 10 =", a + 10)                  # 标量广播到每个元素
print("b + c =")
print(b + c)                               # 不同形状但兼容，自动广播

# 这一句不要运行，因为形状不兼容，不能广播
# print(a + c)


# ======================================
# Part H: matrix multiplication
# 学习内容：
# 逐元素乘法 vs 矩阵乘法
# ======================================

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("\n===== Part H: matrix multiplication =====")
print("A =")
print(A)
print("B =")
print(B)

print("elementwise A * B =")
print(A * B)                               # 逐元素乘法

print("matrix product A @ B =")
print(A @ B)                               # 矩阵乘法