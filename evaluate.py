import os
import sys
import json
from subprocess import run
from shutil import copyfile

ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR_PATH)
os.chdir(ROOT_DIR_PATH)

def check_answer(answer_path: str, output_path: str, db_ans_path: str, db_out_path: str):
    correct = True
    with open(answer_path, 'r') as f:
        answer: str = f.read().strip()
        f.close()
    with open(output_path, 'r') as f:
        output: str = f.read().strip()
        f.close()
    
    with open(db_ans_path, 'r') as f:
        db_ans: dict = json.load(f)
        f.close()

    with open(db_out_path, 'r') as f:
        db_out: dict = json.load(f)
        f.close()
        
    if answer != output:
        correct = False
    elif len(db_ans.keys()) != len(db_out.keys()):
        correct = False
    else:
        for key in db_ans:
            if db_ans[key] != db_out[key]:
                correct = False
                break
    return correct


def test(dir_path: str):
    input_path: str = os.path.join(dir_path, 'input.txt')
    output_path: str = os.path.join(dir_path, 'output.txt')
    answer_path: str = os.path.join(dir_path, 'answer.txt')
    db_ori_path: str = os.path.join(dir_path, 'db_ori.json')
    db_ans_path: str = os.path.join(dir_path, 'db_ans.json')
    db_out_path: str = os.path.join(ROOT_DIR_PATH, 'db.json')
    
    copyfile(db_ori_path, db_out_path)
    with open(input_path, 'r') as f:
        input_data = f.read().encode()
        f.close()
    output_file = open(output_path, 'w')
    run(['python', 'main.py'], input=input_data, stdout=output_file)
    output_file.close()
    
    return check_answer(answer_path, output_path, db_ans_path, db_ori_path)
    
    

if __name__ == "__main__":
    test_dir = os.path.join(ROOT_DIR_PATH, 'Test')
    testcases = sorted(os.listdir(test_dir))

    for idx, testcase in enumerate(testcases):
        testcase_path = os.path.join(test_dir, testcase)
        
        
        if test(testcase_path):
            print(f'[{testcase}] Pass')
        else:
            print(f'[{testcase}] Fail')
        if idx == 1:
            break
    
    

    
    
    
