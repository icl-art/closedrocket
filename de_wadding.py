#This file is a tool to remove wadding.png from unzipped openrocket files
#wadding.png is a menace and must be stopped
#Manually unzip the .orks (or just save from the new .jar), then run this script with:
# python de_wadding.py <filename>
# If you're in wsl - use python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python de_wadding.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, "r") as f:
        data = f.readlines()
    data = "\n".join(filter(lambda x: "wadding.png" not in x, data))
    with open(filename, "w") as f:
        f.write(data)

