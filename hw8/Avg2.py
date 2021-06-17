import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Average numbers')
    parser.add_argument('-g', '--grades', metavar='GRADES', action='store', nargs='+', help='list of the grades')
    parser.add_argument('-f', '--float', metavar='FLOAT', action='store', default=2, help='number of point for average')
    args = parser.parse_args()

    num_list = list(map(int, args.grades))
    sum_ = sum(num_list)
    avg = format((sum_ / len(num_list)),'.'+str(args.float)+'f')
    print("average = ", avg)
