import os
import sys
import json
import shutil
import inspect
import traceback
# Break the 《Go To Statement Considered Harmful》! Make Python capable of using goto too!
# 打破《goto有害论》！让Python也能用得上goto!
def write(name, cmd, encoding="utf-8"):
    os.makedirs("pygoto", exist_ok=True)
    with open(f"pygoto/{name}.pygoto", "w+", encoding=encoding) as file:
        file.write(cmd)
def creative(location, cmd, encoding="utf-8"):
    if location.endswith(".pygoto"):
        print(f"Please don't create files with the suffix >>> .pygoto <<< !Error at line {traceback.extract_stack()[-2].lineno}")
        sys.exit(1)
    directory = os.path.dirname(location)
    os.makedirs(directory, exist_ok=True)
    with open(location, "w", encoding=encoding) as file:
        file.write(cmd)

def run(name, encoding="utf-8"):
    with open(f"pygoto/{name}.pygoto", "r", encoding=encoding) as file:
        code=file.read()
        exec(code,inspect.currentframe().f_back.f_globals)
def execute(location, encoding="utf-8"):
    if location.endswith(".json"):
        with open(location, 'r', encoding=encoding) as file:
            jsonfile = json.load(file)
        return jsonfile
    
    if location.endswith(".pygoto"):
        print(f"Please don't open files with the suffix >>> .pygoto <<< ! Error at line {traceback.extract_stack()[-2].lineno}")
        sys.exit(1)

    with open(location, "r", encoding=encoding) as file:
        code=file.read()
        exec(code,inspect.currentframe().f_back.f_globals)

def init():
    if os.path.exists("pygoto/"):shutil.rmtree("pygoto")

def strcmd(cmd):
    exec(cmd,inspect.currentframe().f_back.f_globals)