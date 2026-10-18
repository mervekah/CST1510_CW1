# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
try:
    with open("records.txt") as f:
        result = f.read()
except FileNotFoundError:
    print("FileNotFoundError: [Errno 2] No such file or directory: 'records.txt' ")
else:
    print(result)
