import sys
import os # determine where the script is being called from
import time
import shutil

SCREENSHOTS_PATH = "/Users/owenallen/Desktop/screenshots"
TO_PATH = ""
REL_PATH = ""
count = 0

def determine_path():
    ### DETERMINE THE TO_PATH TO MOVE THE IMAGES TO
    # CASE 1: "." or ""
    global TO_PATH
    global REL_PATH
    if(len(sys.argv) == 1 or sys.argv[1] == "."):
        # MOVE TO CWD
        TO_PATH = os.getcwd()
    else:
        REL_PATH = os.path.relpath(sys.argv[1], start = os.getcwd())
        TO_PATH = os.getcwd() + "/" + REL_PATH

        if(not os.path.exists(TO_PATH)):
            print("ERROR: THE PATH YOU ENTERED DOES NOT EXIST")
            exit()

    print("USING PATH " + TO_PATH)

def monitor_screenshot(set_files):
    while(True):
        time.sleep(1)
        ls_screenshots = os.listdir(SCREENSHOTS_PATH)
        for filename in ls_screenshots: 
            if filename not in set_files:
                move_file(filename)

def move_file(filename):
    # move the file from SCREENSHOTS_PATH to TO_PATH
    global count
    count += 1
    from_file_path = SCREENSHOTS_PATH + "/" + filename
    to_file_path = TO_PATH + "/image" + str(count) + ".jpg"
    
    if(os.path.exists(from_file_path)): # just in case
        shutil.move(from_file_path, to_file_path)
        print("MARKDOWN INSERT: ![](" + REL_PATH + "/image" + str(count) + ".jpg)")
    else:
        print("Path error when trying to move " + filename)

def main():
    determine_path()
     # keeps track of the images in SCREENSHOTS_PATH at start of run time
    set_files = set(os.listdir(SCREENSHOTS_PATH)) 
    monitor_screenshot(set_files)



if __name__ == "__main__":
    main()

