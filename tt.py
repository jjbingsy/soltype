from pathlib import Path
import os

def read_file_to_list(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip() for line in f]
    return lines

def resetLink():
    file_path = 'paths.txt'
    paths = read_file_to_list(file_path)

    # Directory to store the soft links
    link_dir = Path (read_file_to_list('softlinkdir.txt')[0])

    x = Path(link_dir).glob('*')
    for f in x:
        if os.path.islink(f):
            os.unlink(f)

    all_files = []
    for path in paths:
        p = Path(path).glob('*')
        files = [x for x in p if x.is_file()]
        all_files.extend (files)


    for y in all_files:
        if y.exists() and y.suffix.lower() in ['dummy', '.wmv', '.avi', '.mkv', '.mp4'] :
                count = 0
                counter = ""
                while Path(link_dir / (y.stem.lower() + counter + y.suffix.lower())).exists():
                    count += 1
                    counter = "-" + str(count)
                    print (y)
                os.symlink (y, Path(link_dir / (y.stem.lower() + counter + y.suffix.lower())))

    print (len(all_files))

def parseTitle (str1):
    x = 0
    preF = ""
    sufF = ""
    for c in str1:
        if x == 0:
            if c.isalpha():
                preF += c
            else:
                x = 1
        if x == 1:
            if c.isdigit():
                x = 2
        if x == 2:
            if c.isdigit():
                sufF += c
            else:
                x = 3
    return preF.upper() + "-" + sufF.upper()

#if __name__ == '__main__':
#    resetLink()
