from collections import abc

print(issubclass(tuple,abc.Sequence))
print(issubclass(list,abc.MutableSequence))

symbols = "$óúÑ¼"
codes = [ord(s) for s in symbols]
print(codes)

