import os
import sys
from shutil import copyfile

ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR_PATH)

if __name__ == '__main__':
    test_dir = os.path.join(ROOT_DIR_PATH, 'Test')
    testcases = sorted(os.listdir(test_dir))

    for idx, testcase in enumerate(testcases):
        testcase_path = os.path.join(test_dir, testcase)
        os.remove(os.path.join(testcase_path, 'db_out.json'))
        os.remove(os.path.join(testcase_path, 'output.txt'))