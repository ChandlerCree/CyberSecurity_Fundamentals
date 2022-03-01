#!/usr/bin/env python3

import random, sys, argparse

num_w = 4
num_c = 0
num_n = 0
num_s = 0

nums = ['0','1','2','3','4','5','6','7','8','9']
symbs = ['~','!','@','#','$','%','^','&','*','.',':',';']


with open("words.txt") as file:
	lines = [line.rstrip() for line in file]


parser = argparse.ArgumentParser()

parser.add_argument("-w", "--Words", type=int, help="Words Help")
parser.add_argument("-c", "--Caps", type=int, help="Caps Help")
parser.add_argument("-n", "--Numbers", type=int, help="Numbers Help")
parser.add_argument("-s", "--Symbols", type=int, help="Symbols Help")

args = parser.parse_args()


if args.Words:
	num_w = args.Words
	#print(str(num_w) + " words")
if args.Caps:
	num_c = args.Caps
	#print(str(num_c) + " caps")
if args.Numbers:
	num_n = args.Numbers
	#print(str(num_n) + " numbers")
if args.Symbols:
	num_s = args.Symbols
	#print(str(num_s) + " symbols")


usr_pw = []
has_been_cap = [0] * num_w
counter = num_c


#deals with -w flag
for _ in range(num_w):
	wint = random.randrange(1,len(lines))
	usr_pw.append(lines[wint])


#deals with -c flag
while counter > 0:
	cint = random.randrange(1, num_w)
	if has_been_cap[cint] == 0:
		temp_str = usr_pw[cint]
		usr_pw[cint] = temp_str.capitalize()
		has_been_cap[cint] = 1
		#print(has_been_cap)
		counter -= 1
		#print("dec" + str(cint))

for _ in range(num_n):
	nint = random.randrange(1, num_w)
	n = random.randrange(10)
	m = nums[n]
	#print(m)

	usr_pw.insert(nint, m)

for _ in range(num_s):	
	sint = random.randrange(1, num_w)
	o = random.randrange(1, len(symbs))
	p = symbs[o]
	#print(o)

	usr_pw.insert(sint, p)


print(usr_pw)

print(''.join(e for e in usr_pw))
