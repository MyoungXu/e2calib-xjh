"""
@Time ： 2023/2/11 17:40
@Auth ： Haoyue Liu
@File ：timestamp_transfer.py
"""
import argparse

def get_timestamp(file_name):
    timestamp = []
    with open(file_name, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 0:
                start_t = int(line.strip().split()[0])/1000
                continue
            t = int(line.strip().split()[0])/1000 - start_t
            timestamp.append(str(int(t)) + '\n')
    return timestamp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file name')
    args = parser.parse_args()

    timestamp_file = args.input
    convert_file = 'timestamp_convert.txt'
    timestamp_list = get_timestamp(timestamp_file)
    with open(convert_file, mode='w', encoding='utf-8') as f:
        f.writelines(timestamp_list)
    print("Conversion completed.")