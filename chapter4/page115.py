#!/usr/bin/python3


man=[]
other=[]
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missiong!')

try:
	man_data = open('man_data.txt', 'w')
	other_data = open('ohter_data.txt', 'w')
	print(man, file=man_data)
	print(other, file=other_data)
except IOError:
	print('Write file error!')

finally:
	man_data.close()
	other_data.close()
