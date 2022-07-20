data = []
i = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		i += 1
		if i % 1000 == 0:
			print(len(data))
print('There are',len(data),'of information')

data = []
total = 0
i = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		total += len(data[i])
		i += 1
print('The average of the reviews is',int(total/int(len(data))))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'of imformation','less than 100 words.')
	

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good),'of reviews got good in their messages.')
