import os

lax_coords = (33.8425, 118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, .66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE235465'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

print('\n========\n')
for country, _ in traveler_ids:
    print(country)

print('\n========\n')
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(f'Is a equal to b?:{a == b}')
b[-1].append(99)
print(f'Is a equal to b?:{a == b}')
print(a)
print(b)


# P33

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])

print(fixed(tf))
print(fixed(tm))

# P36
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

# p36
_, filename = os.path.split('/home/bwpeter/.ssh/id_rsa.pub')
print(filename)


