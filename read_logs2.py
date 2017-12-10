from collections import Counter
from collections import defaultdict

def read_logfile(logfile):
    with open(logfile) as f:
        for line in f:
            yield line

def process_logfile(logfile):
    counts = Counter()
    totals = defaultdict(int)
    for line in read_logfile(logfile):
        line = line.split()
        image, resp_code, size = line[3], line[5], line[6]
        if resp_code == '200':
            counts[image] += 1
            totals[image] += int(size)
    return print_counts(counts, totals)

def print_counts(counts, totals):
    top_10 = counts.most_common(10)
    for item, count in top_10:
        print '{} {}'.format(item, totals[item])

process_logfile('logfile.txt')
