from array import array
from random import random
floats = array('d',(random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp2 = open('floats.bin','rb')
floats2.fromfile(fp2,10**7)
fp.close
print(floats2[-1])
print(floats == floats2);
print (floats.typecode, floats2.typecode)

floats = array(floats.typecode, sorted(floats))

print(floats == floats2);
print(f"lowest:{floats[0]}  highest:{floats[-1]}")
print (floats[-1])
