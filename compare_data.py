import matplotlib.pyplot as plt
import argparse


def main(files):
    data_set = []
    print(files)
    for fi in files:
        data = []
        avg = []
        size = []
        with open(fi) as f:
            content = f.readlines()
        for c in content:
            con = c.replace('\n','').replace('[','').replace(']','').split(", ")
            print(con)
            avg.append(con[2])
            size.append(con[0])
        data.append(avg)
        data.append(size)
        data_set.append(data)
    for count in range(len(data_set)):
        print(data_set)
        plt.plot(data_set[count][1], data_set[count][0], label="line" + str(count))
    plt.legend()
    plt.show()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('[avged file]', nargs='+', help='path to the file')
    args_namespace = parser.parse_args()
    args = vars(args_namespace)['[avged file]']
    main(args)
