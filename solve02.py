# flagの後半部分
from Cryptodome.Cipher import AES

C = [95, -59, -20, -93, -70, 0, -32, -93, -23, 63, -9, 60, 86, 123, -61, -8, 17, -113, -106, 28, 99, -72, -3, 1, -41, -123, 17, 93, -36, 45, 18, 71, 61, 70, -117, -55, 107, -75, -89, 3, 94, -71, 30]
C = "".join(chr(c%256) for c in C)
K = "IncrediblySecure"

aes = AES.new(K, AES.MODE_GCM, C[:12])
print(aes.decrypt(C[12:]))
