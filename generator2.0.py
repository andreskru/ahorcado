import os
import time
import argparse
import random
from datetime import datetime

def create_file(size, directory,count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"generated_file_{timestamp}-{size}MB-{count}.txt"
    file_path = os.path.join(directory, file_name)

    with open(file_path, 'wb') as file:
        file.write(os.urandom(size*1024*1024))

    print(f"[{timestamp}] Created file: {file_name} ({size} megabytes) in {directory}")

def main():
    parser = argparse.ArgumentParser(description="Generate files with random content")
    parser.add_argument("size", type=int, help="Size of the file in megabytes")
    parser.add_argument("directory", type=str, help="Directory destination for the generated files")
    parser.add_argument("iterations", type=int, help="Number of files to be created")

    args = parser.parse_args()

    print(f"Starting generation of {args.iterations} files...")

    try:
            for i in range(args.iterations):
                create_file(args.size, args.directory,i)
    except KeyboardInterrupt:
        print("\nFile generation stopped.")

if __name__ == "__main__":
    main()
