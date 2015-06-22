# COUNTING VOWELS

count = 0
for lt in s:
    if lt == 'a' or lt == 'e' or lt == 'i' or lt == 'o' or lt == 'u':
        count += 1

print count

# COUNTING BOBS

count = 0

for idx, lt in enumerate(s):
	if lt == 'b':
		if s[idx:idx+3] == 'bob':
			count += 1

print 'Number of times bob occurs is:', count

# ALPHABETICAL SUBSTRINGS

ss = []

for idx, lt in enumerate(s):
	i = idx + 1
	while i <= len(s):
		if s[idx:i] == ''.join(sorted(s[idx:i])):
			ss.append(s[idx:i])
		i += 1

print 'Longest substring in alphabetical order is:', max(ss, key=len)