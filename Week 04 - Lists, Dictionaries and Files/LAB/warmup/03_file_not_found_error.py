# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
#%%

try:
    with open("records.txt", "r") as f:
        result = f.read()

except FileNotFoundError:
    print("File not found")

else:
    print(result)
# %%
