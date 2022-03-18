from typing import List
from time import time

start = 1
end = 10000
file_path = "test.txt"

output = str([i for i in range(start, end)])
output = output.replace('[', '')
output = output.replace(']', '')


file = open(file_path, 'w')
file.write(output)
file.close()

output: List[int] = []
file = open("test.txt", 'r')
content = file.read()
for item in content.split(','):
        value = int(item)
        output.append(value)
        
output.sort(reverse=True) 

cpu_start_time = 0
cpu_binary_time = 0
cpu_linear_time = 0

cpu_start_time = time()
for i in range(1, len(output)):
    j = i
    while j > 0 and output[j - 1] > output[j]:
        output[j - 1], output[j] = output[j], output[j - 1]
        j -= 1

cpu_linear_time = (time() - cpu_start_time) * 1000
print(f'Milisegundos: {cpu_linear_time}')
print(output)





