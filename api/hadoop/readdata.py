import hadoopy
import os

local_path = '/home/hdusr/erika/get_data'


def main():
    # insert the path that you want to read from
    hdfs_path = 'hdfs://127.0.0.1:9000/twitter1/'

    for key, value in hadoopy.readtb(hdfs_path):
        filename = key.split("/")[-1]
        path = os.path.join(local_path, filename)
        print("the path is {}".format(path))

        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass
        open(path, 'w').write(value)

if __name__ == '__main__':
    main()