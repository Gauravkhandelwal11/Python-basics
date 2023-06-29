'''f =open("data.txt" , 'r')

# using for loops:-

for lines in f:
	print(lines)


# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

f.close()

'''
 

# With automatically closes the file

with open("data.txt") as f:
	# for lines in f:
	# 	print(lines)

	# print(f.read(19))
	# print(f.read(19))

    print(f.read(19))
    f.seek(0)
	print(f.read(19))