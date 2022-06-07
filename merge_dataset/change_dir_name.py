import os

# 変換元
base_path =  '/data/design_contest_dataset/2022_06_01_v2.2/'
# 変換先
change_path = '/data/design_contest_dataset/2022_06_06_v2.2/'

file_list = ['train','valid','test']

print('\"'+base_path+'\"'+' >> '+'\"'+change_path+'\"')
for i,file_type in enumerate(file_list):
    print("step:"+str(i)+"/"+str(len(file_list))+", rewrite \""+file_type+".txt\"")
    read_path  = './'+file_type+'.txt'
    write_path = './'+file_type+'.txt' 
    open_file = open(read_path,'r')
    lines_str = [s.strip() for s in open_file.readlines()]
    open_file.close()
    write_file = open(write_path,'w')
    for line_str in lines_str:
        ## here replace path ##
        new_line_str = line_str = line_str.replace(base_path,change_path) + '\n'
        write_file.write(line_str)  
    write_file.close()
