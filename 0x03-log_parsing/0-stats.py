#!/usr/bin/python3
"""Log Parser"""
import sys
import signal

# Initialize the total file size and status code counts
file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    """Print statistics for total file size and status code counts."""
    print(f"File size: {file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """Parse a log line and update file size and status code counts."""
    global file_size
    try:
        parts = line.split()
        # Update file size
        file_size += int(parts[-1])
        # Update status code count if it's valid
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except (IndexError, ValueError):
        # Ignore lines that don't match the expected format
        pass

def handle_interrupt(signum, frame):
    """Handle keyboard interrupt (CTRL + C) by printing statistics."""
    print_stats()
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_interrupt)  # Setup interrupt handler
    line_count = 0

    for line in sys.stdin:
        parse_line(line)
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

    print_stats()  # Print any remaining stats after processing all lines
