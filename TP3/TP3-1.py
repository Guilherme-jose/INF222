import numpy as np


print("1.")

a = []

for D in [-1,1]:
    for C in [-1,1]:
        for B in [-1,1]:
            for A in [-1,1]:
                a.append([1, A, B, C, D, A*B, A*C, A*D, B*C, B*D, C*D, A*B*C, A*B*D, A*C*D, B*C*D, A*B*C*D])
                
a = np.array(a)         

b = np.array([9.9713, 3.2476, 22.4025, 6.4696, 9.8672, 3.1181, 22.8235, 6.6017, 0.4576, 0.0245, 0.9497, 0.049, 0.4371, 0.0225, 0.9722, 0.043])

x = np.linalg.solve(a, b)

print(x)

SST = np.sum((b - np.mean(b))**2)
SSA = 16 * (x[1]**2)
SSB = 16 * (x[2]**2)
SSC = 16 * (x[3]**2)
SSD = 16 * (x[4]**2)
SSAB = 16 * (x[5]**2)
SSAC = 16 * (x[6]**2)
SSAD = 16 * (x[7]**2)
SSBC = 16 * (x[8]**2)
SSBD = 16 * (x[9]**2)
SSCD = 16 * (x[10]**2)
SSABC = 16 * (x[11]**2)
SSABD = 16 * (x[12]**2)
SSACD = 16 * (x[13]**2)
SSBCD = 16 * (x[14]**2)
SSABCD = 16 * (x[15]**2)

print("SST: ", SST)
print("SSA: ", SSA, "SSB: ", SSB, "SSC: ", SSC, "SSD: ", SSD)
print("SSAB: ", SSAB, "SSAC: ", SSAC, "SSAD: ", SSAD, "SSBC: ", SSBC, "SSBD: ", SSBD, "SSCD: ", SSCD)
print("SSABC: ", SSABC, "SSABD: ", SSABD, "SSACD: ", SSACD, "SSBCD: ", SSBCD)
print("SSABCD: ", SSABCD)


print("A%: ", round(SSA/SST, 4), "B%: ", round(SSB/SST, 4), "C%: ", round(SSC/SST, 4), "D%: ", round(SSD/SST, 4))
print("AB%: ", round(SSAB/SST, 4), "AC%: ", round(SSAC/SST, 4), "AD%: ", round(SSAD/SST, 4), "BC%: ", round(SSBC/SST, 4), "BD%: ", round(SSBD/SST, 4), "CD%: ", round(SSCD/SST, 4))
print("ABC%: ", round(SSABC/SST, 4), "ABD%: ", round(SSABD/SST, 4), "ACD%: ", round(SSACD/SST, 4), "BCD%: ", round(SSBCD/SST, 4))
print("ABCD%: ", round(SSABCD/SST, 4))



print("2.")

a = []

for C in [-1,1]:
    for B in [-1,1]:
        for A in [-1,1]:
            a.append([1, A, B, C, A*B, A*C, B*C, A*B*C])
                
a = np.array(a)         
b = np.array([0.4326, 0.025, 21.9664, 8.1444, 9.6607, 3.8457, 0.9007, 0.0445])

x = np.linalg.solve(a, b)

print(x)

SST = np.sum((b - np.mean(b))**2)
SSA = 8 * (x[1]**2)
SSB = 8 * (x[2]**2)
SSC = 8 * (x[3]**2)
SSAB = 8 * (x[4]**2)
SSAC = 8 * (x[5]**2)
SSBC = 8 * (x[6]**2)
SSABC = 8 * (x[7]**2)

print("SST: ", SST, "SSA: ", SSA, "SSB: ", SSB, "SSC: ", SSC)
print("SSAB: ", SSAB, "SSAC: ", SSAC, "SSD: ", SSBC)
print("SSE: ", SSABC)

print("A%: ", round(SSA/SST, 4), "B%: ", round(SSB/SST, 4), "C%: ", round(SSC/SST, 4))
print("AB%: ", round(SSAB/SST, 4), "AC%: ", round(SSAC/SST, 4), "D%: ", round(SSBC/SST, 4))
print("E%: ", round(SSABC/SST, 4))

print("3.")

a = []

for D in [-1,1]:
    for C in [-1,1]:
        for B in [-1,1]:
            for A in [-1,1]:
                a.append([1, A, B, C, D, A*B, A*C, A*D, B*C, B*D, C*D, A*B*C, A*B*D, A*C*D, B*C*D, A*B*C*D])
                
a = np.array(a)

b1 = ([9.9713, 3.2476, 22.4025, 6.4696, 9.8672, 3.1181, 22.8235, 6.6017, 0.4576, 0.0245, 0.9497, 0.049, 0.4371, 0.0225, 0.9722, 0.043])
b2 = ([9.9092, 3.3611, 22.9585, 6.6442, 10.6559, 3.0535, 23.6042, 6.5507, 0.4621, 0.0245, 0.9457, 0.0505, 0.4416, 0.019, 0.9182, 0.046])
b3 = ([9.6912, 3.2476, 22.959, 6.7037, 9.6962, 3.089, 22.7925, 6.4201, 0.4656, 0.028, 0.9722, 0.0525, 0.4506, 0.0195, 0.9662, 0.0455])
b4 = ([9.7587, 3.3666, 22.2229, 6.6737, 9.6627, 3.111, 22.4505, 6.4981, 0.4706, 0.0255, 0.9632, 0.0515, 0.4776, 0.0195, 0.9647, 0.044])
b5 = ([9.9032, 3.2126, 22.3564, 6.6757, 10.2368, 3.0925, 22.2434, 6.4056, 0.4671, 0.0245, 1.0402, 0.052, 0.4671, 0.02, 0.9497, 0.045])

b = np.mean([b1, b2, b3, b4, b5], axis=0)

e1 = b1 - b
e2 = b2 - b
e3 = b3 - b
e4 = b4 - b
e5 = b5 - b

SSE = np.sum(e1**2) + np.sum(e2**2) + np.sum(e3**2) + np.sum(e4**2) + np.sum(e5**2)

x = np.linalg.solve(a, b)

print(x)

SSA = 16 * 5 * (x[1]**2)
SSB = 16 * 5 * (x[2]**2)
SSC = 16 * 5 * (x[3]**2)
SSD = 16 * 5 * (x[4]**2)
SSAB = 16 * 5 * (x[5]**2)
SSAC = 16 * 5 * (x[6]**2)
SSAD = 16 * 5 * (x[7]**2)
SSBC = 16 * 5 * (x[8]**2)
SSBD = 16 * 5 * (x[9]**2)
SSCD = 16 * 5 * (x[10]**2)
SSABC = 16 * 5 * (x[11]**2)
SSABD = 16 * 5 * (x[12]**2)
SSACD = 16 * 5 * (x[13]**2)
SSBCD = 16 * 5 * (x[14]**2)
SSABCD = 16 * 5 * (x[15]**2)

SST = SSA + SSB + SSC + SSD + SSAB + SSAC + SSAD + SSBC + SSBD + SSCD + SSABC + SSABD + SSACD + SSBCD + SSABCD + SSE

print("SST: ", SST, "SSA: ", SSA, "SSB: ", SSB, "SSC: ", SSC, "SSD: ", SSD, "SSE: ", SSE)
print("SSAB: ", SSAB, "SSAC: ", SSAC, "SSAD: ", SSAD, "SSBC: ", SSBC, "SSBD: ", SSBD, "SSCD: ", SSCD)
print("SSABC: ", SSABC, "SSABD: ", SSABD, "SSACD: ", SSACD, "SSBCD: ", SSBCD)
print("SSABCD: ", SSABCD)

print("A%: ", round(SSA/SST, 4), "B%: ", round(SSB/SST, 4), "C%: ", round(SSC/SST, 4), "D%: ", round(SSD/SST, 4), "E%: ", round(SSE/SST, 4))
print("AB%: ", round(SSAB/SST, 4), "AC%: ", round(SSAC/SST, 4), "AD%: ", round(SSAD/SST, 4), "BC%: ", round(SSBC/SST, 4), "BD%: ", round(SSBD/SST, 4), "CD%: ", round(SSCD/SST, 4))
print("ABC%: ", round(SSABC/SST, 4), "ABD%: ", round(SSABD/SST, 4), "ACD%: ", round(SSACD/SST, 4), "BCD%: ", round(SSBCD/SST, 4))
print("ABCD%: ", round(SSABCD/SST, 4))

