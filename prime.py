from math import sqrt
import sys

prime=[3]
limit=int(sys.argv[1])

f = open('prime_numbers', 'r')

for x in f.readlines(): 
	prime.append(int(x))
	if (not limit==0 and int(x)>=sqrt(limit)):	
		break	
f.close()

f = open('prime_numbers', 'r')
for x in f.readlines():
        last_number=x           
f.close()
last_number=int(last_number)

test_number=last_number

if limit == 0:
	limit = last_number*last_number
print ("limit:",limit,"\nNumber of prime number in memory:",len(prime),"\nLast Number:", last_number)
while (test_number<limit ):
	i=0
	is_prime=1
	while (prime[i]<=sqrt(test_number)):
		if test_number%prime[i]==0:
			is_prime=0
			break
		i=i+1
	if (is_prime):
		#prime.append(test_number)
		#print (test_number,end ="\t")
		if (test_number > last_number):
			file1 = open('prime_numbers', 'a+')
			file1.write(str(test_number)+"\n")
			file1.close()
	test_number=test_number+2

#print (prime)
