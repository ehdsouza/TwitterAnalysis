__author__ = 'erika'

"Use writetb to put data on HDFS with demo that writes local directory contents to HDFS"
import hadoopy
import os

hdfs_path = 'data_in_ex0.seq.tb'


def read_local_dir(local_path):
    for fn in os.listdir(local_path):
        path = os.path.join(local_path, fn)
        if os.path.isfile(path):
            yield path, open(path).read()


def main():
    local_path = '.'
    hadoopy.writetb(hdfs_path, read_local_dir(local_path))

if __name__ == '__main__':
    main()
