import os
import sys
from synb0 import synb0
from shutil import rmtree, copy

def gen_synb0_single(in_file, root, output_folder):
    print("gen single synb0")
    # Generate tmp_folder
    temp_folder = os.path.join(output_folder, "synb0_tmp")

    # Grab the base name of the file
    name = (os.path.basename(in_file)).split("_T1")[0]

    # Call the function to generate the Synb0
    output_file = synb0(temp_folder, in_file, name, root)

    # Copy the synb0 out of the temp file
    copy(output_file, output_folder)

    # Clear all other files
    rmtree(temp_folder)

def main():
    in_file = sys.argv[1]
    synb0_root = sys.argv[2]
    output_folder = sys.argv[3]

    gen_synb0_single(in_file, synb0_root, output_folder)

if __name__== "__main__":
    main()
