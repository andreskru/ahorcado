import os
import time
import argparse
import random
import gc
from datetime import datetime

#3.0 Generates N files of size S[MB]

# python3 ./generate-3.0.py 10000 "/mnt/c/Users/Administrator/OneDrive - Personal/Backup" 60
# python3 ./generate-3.0.py 10 "/home/akruger" 5


def create_file(size, directory,count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"generated_file_{timestamp}-{size}MB-{count}.txt"
    file_path = os.path.join(directory, file_name)

    chunk_size = 1024*1024 # Set the chunk size to 1 MB
    num_chunks = size*1024*1024 // chunk_size

    with open(file_path, 'ab') as file:
        #open modes 'a':append, 'w':write, 'b:binary'
        for _ in range(num_chunks):
            file.write(os.urandom(chunk_size))
            gc.collect()
            #print("sleeping")
            #time.sleep(1) # sleep for debug purposes
        
        remaining_bytes = size*1024*1024 % chunk_size
        if remaining_bytes > 0:
            file.write(os.urandom(remaining_bytes))

    print(f"[{timestamp}] Created file: {file_name} ({size} MB) in {directory}")

def main():
    parser = argparse.ArgumentParser(description="Generate files with random content")
    parser.add_argument("size", type=int, help="Size of the file in megabytes")
    parser.add_argument("directory", type=str, help="Directory destination for the generated files")
    parser.add_argument("iterations", type=int, help="Number of files to be created")

    args = parser.parse_args()

    print(f"Starting generation of {args.directory} files...")

    try:
            for i in range(args.iterations):
                create_file(args.size, args.directory,i)
    except KeyboardInterrupt:
        print("\nFile generation stopped.")

if __name__ == "__main__":
    main()
