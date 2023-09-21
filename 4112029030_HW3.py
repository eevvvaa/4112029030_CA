import os
os.makedirs('CS/homework')

absolute_path=r'C:\Users\eva19\CS\homework\homework.txt'
absolute_path2=r'C:\Users\eva19\CS'
with open(absolute_path, 'w') as file:
    file.write('4112029030_洪呈宜')
file=open(absolute_path, 'r')
content=file.read()
print({content})

import os
import time
file_size=os.path.getsize(absolute_path)
print(f'文件大小:{file_size}字節')
modification_time=os.path.getmtime(absolute_path)
print(f'最後修改時間:{modification_time}')
formatted_time=time.ctime(modification_time)
print(f'最後修改時間(人類可讀模式):{formatted_time}')
file.close();
    

import os
os.remove(absolute_path)
import shutil
shutil.rmtree(absolute_path2)
