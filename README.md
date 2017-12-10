# logfileparser

There are 2 python files which read thr given logfile (logfile.txt) to generate the cumulative stats for the most frequent items

read_logs.py assumes that the log file can be read into memory. It uses counter to track the most frequent items. Totals is used to the cumulative bytes transferred. The top 10 frequently accessed items can be accessed via Counter's most_common method.

read_logs2.py uses yield for the use case where the file is too large and cannot be loaded into memory
