import os

data_folder = '/Users/ff/Desktop/TW/'
names = []
for dir_path, subpaths, files in os.walk(data_folder):
    for name in files:  # 文件夹下的所有文件
        if not name.endswith('.DS_Store'):
            file_path = os.path.join(dir_path, name)
            names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as f_in:
        # 有后缀
        # with open(file_path.replace('.txt', '.despace'), 'w', encoding='utf-8') as f_out:
        # 无后缀
        with open(file_path.replace(name, name+'.only'), 'w', encoding='utf-8') as f_out:
            for lines in f_in:
                time=lines.split('\t')[0].replace('-','')
                if str(time)==str(name):
                    f_out.write(lines)
    os.remove(file_path)
    os.rename(file_path.replace(name, name+'.only'),file_path)