import re
import os

print("css 파일 읽기 시작!")
directory = os.getcwd() + '\\input'
filename = 'style.css'
file_path = os.path.join(directory, filename)
f = open(file_path, 'r', encoding='UTF8')
lines = f.read()

print("-"*10)
print("-"*10)

## HEX CODE 추출
pattern = '#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}'
matches = sorted(list(set(re.findall(pattern, lines))))
print("HEX CODE 추출 완료!")
print("-"*10)
f.close()
print("HEX 파일 쓰기 시작!")
f = open('output/result.txt', 'w', encoding='UTF8')
for i in matches:
    data = i + '\n'
    val = '#' + i[1:] + i[1:]
    if val not in matches:
        if len(i) == 4:
            val = '#' + i[1:] + i[1:] + "\n"
        else:
            val = data
        f.write(val)
f.close()
print("HEX 파일 쓰기 완료!")
print("-"*10)
print("-"*10)

## RGB, RGBA 추출
pattern = r'(rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+(?:\.\d+)?))?\))'
matches = re.findall(pattern, lines)
print("RGB, RGBA 추출 완료!")
print("-"*10)
f.close()

print("RGB, RGBA 파일 쓰기 시작!")
matches = sorted(list(set(matches)))
array = set()
f = open('output/result.txt', 'a', encoding='UTF8')
for i in matches:
    array.add(i[0].replace(" ",""))
for i in array:
    data = i + "\n"
    f.write(data)
f.close()
print("RGB, RGBA 파일 쓰기 완료!")
