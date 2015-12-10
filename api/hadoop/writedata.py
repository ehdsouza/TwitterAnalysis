uthor__ = 'erika'

import hadoopy
import os

# change the directory path...
hdfs_path = 'hdfs://localhost:9000/twitter1'

# this will create a key, value paif of filepath, data
def read_local_dir(local_path):
    for fn in os.listdir(local_path):
        path = os.path.join(local_path, fn)
        if os.path.isfile(path):
            yield path, open(path).read()


def main():
    local_path = '/home/hdusr/erika/data'
    hadoopy.writetb(hdfs_path, read_local_dir(local_path))

if __name__ == '__main__':
    main()