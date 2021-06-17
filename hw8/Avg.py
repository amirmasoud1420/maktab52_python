import sys

if __name__ == '__main__':
    num_list = sys.argv[1:]
    num_list = list(map(int,num_list))
    sum_ = sum(num_list)
    avg = sum_ / len(num_list)
    print("Average = ", avg)
