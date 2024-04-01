#!/usr/bin/python3
"""Module parses log data and computes metrics"""
import sys


def print_metrics(total_size, status_counts):
    """
    Prints the computed metrics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def parse_input(line, total_size, status_counts):
    """Parses each input line and updates the metrics."""
    try:
        parts = line.strip().split()
        if len(parts) >= 5:
            size = int(parts[-1])
            total_size += size
            status_code = parts[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1
    except ValueError:
        pass

    return total_size, status_counts


def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_counts = \
                    parse_input(line, total_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except keyboardInterrupt:
        print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
