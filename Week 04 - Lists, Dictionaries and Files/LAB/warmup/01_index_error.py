# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]

try:
    result = labels[2]
    print(result)
except IndexError:
    print ("Index is out of range")


