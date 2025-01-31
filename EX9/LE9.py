import numpy as np

print("1.")

a = np.array([[1,-1,-1, 1],
              [1, 1,-1,-1],
              [1,-1, 1,-1],
              [1, 1, 1, 1]])
b = np.array([680,210,540,180])

x = np.linalg.solve(a,b)

print(x)

y_line = b.sum()/4

SST = np.sum((b-y_line)**2)
SSA = 4 * x[1]**2
SSB = 4 * x[2]**2
SSAB = 4 * x[3]**2


print(SST, SSA, SSB, SSAB)
print(round(SSA/SST, 2), round(SSB/SST, 2), round(SSAB/SST, 2))

print("2.")

a = np.array([[ 1,-1,-1,-1, 1, 1, 1,-1],
              [ 1, 1,-1,-1,-1,-1, 1, 1],
              [ 1,-1, 1,-1,-1, 1,-1, 1],
              [ 1, 1, 1,-1, 1,-1,-1,-1],
              [ 1,-1,-1, 1, 1,-1,-1, 1],
              [ 1, 1,-1, 1,-1, 1,-1,-1],
              [ 1,-1, 1, 1,-1,-1, 1,-1],
              [ 1, 1, 1, 1, 1, 1, 1, 1]])

b = np.array([20,40,120,100,50,30,10,15])

x = np.linalg.solve(a,b)

print(x)

SST = np.sum((b-b.sum()/8)**2)
SSA = 8 * x[1]**2
SSB = 8 * x[2]**2
SSC = 8 * x[3]**2
SSAB = 8 * x[4]**2
SSAC = 8 * x[5]**2
SSBC = 8 * x[6]**2
SSABC = 8 * x[7]**2

print(SST, SSA, SSB, SSC, SSAB, SSAC, SSBC, SSABC)


print(round(SSA/SST, 2), round(SSB/SST, 2), round(SSC/SST, 2), round(SSAB/SST, 2), round(SSAC/SST, 2), round(SSBC/SST, 2), round(SSABC/SST, 2))


print("3.")

b = np.array([0.2370,0.4135,0.5430,0.8796,4.8433,1.7543,10.4854,6.6476])

x = np.linalg.solve(a,b)

print(x)

SST = np.sum((b-b.sum()/8)**2)
SSA = 8 * x[1]**2
SSB = 8 * x[2]**2
SSC = 8 * x[3]**2
SSAB = 8 * x[4]**2
SSAC = 8 * x[5]**2
SSBC = 8 * x[6]**2
SSABC = 8 * x[7]**2

print(round(SST, 2), round(SSA, 2), round(SSB, 2), round(SSC, 2), round(SSAB, 2), round(SSAC, 2), round(SSBC, 2), round(SSABC, 2))

print(round(SSA/SST, 2), round(SSB/SST, 2), round(SSC/SST, 2), round(SSAB/SST, 2), round(SSAC/SST, 2), round(SSBC/SST, 2), round(SSABC/SST, 2))