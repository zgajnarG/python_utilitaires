import glob
import shutil
import sys, getopt


def main(argv):
    input , output = populate_args(argv)
    handle_error(input, output)
    copy_files(input, output)


def populate_args(argv):
    input =""
    output = ""
    opts, args = getopt.getopt(argv,"hi:o:",["idirectory=","odirectory="])
    for opt, arg in opts:
        if opt in ("-i", "--idirectory"):
            input = arg
        elif opt in ("-o", "--odirectory"):
            output = arg
    return input, output
    

def handle_error(input, output):
    if not input or not output:
        print("Usage: exportimages.py -i <inputdirectory> -o <outputdirectory>")
        sys.exit(2)
    
def copy_files(input, output):
    ext = ['png', 'jpg', 'gif']
    files = []
    [files.extend(glob.glob(input + '\*.' + e)) for e in ext]
    for f in files :
        input_file = f.replace('\\', '/');
        output_file = output + '/' + input_file.split('/')[-1]
        shutil.copy(input_file, output_file)    

if __name__ == "__main__":
   main(sys.argv[1:])



