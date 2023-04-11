total = 0
count_num = 0

open_file = open('numbers.txt', 'w')
open_file.write('1' + '\n')
open_file.write('2' + '\n')
open_file.write('3' + '\n')
open_file.close()

open_numbers = open('numbers.txt', 'r')

# line = open_file.readline()

for line in open_numbers:
    num = float(line)
    total += num
    count_num += 1
    
print('the average is: ', total/count_num)
open_numbers.close()
