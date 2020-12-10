import argparse
import matplotlib.pyplot as plt
def match_IDs(talk_log, list_log):
    ID_field = 3
    data = []
    smallr = len(talk_log)
    longr = len(list_log)
    small_log = talk_log
    long_log = list_log
    if len(list_log) < len(talk_log):
        smallr = len(list_log)
        longr = len(talk_log)
        small_log = list_log
        long_log = talk_log
    for l in range(smallr):
        talk = small_log[l].replace('\n','').replace('[','').replace(']','').split(" ")
        for ll in range(longr):
            liste = long_log[ll].replace('\n','').replace('[','').replace(']','').split(" ")
            if(talk[5] == liste[5]):
                entry = []
                entry.append(int(talk[5]))
                entry.append(abs(float(talk[1]) -float( liste[1])))
                if len(talk) > len(liste):
                    entry.append(int(talk[8]))
                else:
                    entry.append(int(liste[8]))
    
                data.append(entry)        
                break
    return data

def get_averages(data):
    output = []
    avgs = []
    curr_ID = 0
    curr_size = data[0][2]
    index = 0
    entry = []
    for dat in data:
        if dat[2] == curr_size:
            if(len(entry) < 1):
                entry.append(curr_size)
        elif len(avgs) > 0:
            sum = 0.0
            for a in avgs:
                sum += a
            sum /= len(avgs)
            entry.append(len(avgs))
            avgs = []
            entry.append(sum)
            output.append(entry)
            entry = []
        avgs.append(dat[1])
        curr_size = dat[2]
    return output
            
def draw_graph(data):
    data_sizes = []
    avg_times = []
    for dat in data:
        data_sizes.append(dat[0])
        avg_times.append(dat[2])
    plt.plot(data_sizes, avg_times)
    plt.ylabel('seconds')
    plt.xlabel('data size /bytes')
    plt.show()

def main(files):
    talker = files[0]
    listener = files[1]
    count = 0
    with open(talker) as f:
        talker_log = f.readlines()
    with open(listener) as f:
        listener_log = f.readlines()
    data = match_IDs(talker_log, listener_log)
    date = get_averages(data)
    for i in date:
        print(i)
    draw_graph(date)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('[log file]', nargs=2, help='path to the file')
   # parser.add_argument('[comparison file]', nargs='4?', help='path to files of data to be compared against \n must be provided in sets of 2')
   # parser.add_argument('[listener log file]', nargs = 1, help='path to the file')
    args_namespace = parser.parse_args()
    args = vars(args_namespace)['[log file]']
   # comparison = vars(args_namespace)['[comparison file]']

    main(args)
