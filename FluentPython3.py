dial_codes = [
    (880,'Bangladesh'),
    (55,'Brazil'),
    (86,'China'),
    (91,'India'),
    (62,'Indonesia'),
    (81,'Japan'),
    (234,'Nigeria'),
    (92,'Pakistan'),
    (7,'Russia'),
    (1,'UnitedStates'),
]

codesdict = {country : code for code, country in dial_codes}
print(dial_codes)
print(codesdict)

print({code:country.upper() for country, code in sorted(codesdict.items()) if code < 70})

#P85
print(hash((1,2,frozenset([30,40]))))

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open('Progress report', encoding = 'utf-8') as fp:
    for line_no, line in enumerate(fp,1):

        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no, column_no)
            #UGLYEXAMPLE
            occurances = index.get(word, [])
            occurances.append(location)
            index[word] = occurances
#print out by alphabet
for word in sorted(index,key=str.upper):
    print(word, index[word])

print('-'*80)

class StrKeyDict0(dict):
    
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, __key: object) -> bool:
        return key in self.keys() or str(key) in self.keys()
    