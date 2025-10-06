import argparse

parser = argparse.ArgumentParser(description ="A simple command-line utility.")
parser.add_argument("filename", help="The file to rpcess.")
parser.add_argument("-n", "--number", type =int, default =1, help="Number of times to repeat the output")

args = parser.parse_args()

try:
    with open(args.filename, "r") as file:
        content = file.read()
        for _ in range(args.number):
            print(content)
except FileNotFoundError:
    print("File not found.")