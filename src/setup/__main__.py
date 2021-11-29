import json
import os
import pwd

# Stores location of current file
__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

__currentuser__ = pwd.getpwuid(os.getuid())[0]

with open(os.path.join(__location__, 'default.json'), 'r') as f:
   settings = json.load(f)

ROOT_FOLDER = settings['root'].replace("$USER",__currentuser__)

WAREHOUSE_PATH = os.path.join(ROOT_FOLDER, "warehouse")
BIN_PATH = os.path.join(ROOT_FOLDER, "bin")
ALIAS_PATH = os.path.join(ROOT_FOLDER, "alias.json")
YAPM_PATH = os.path.join(WAREHOUSE_PATH, "bin/yapm")

def add_path(path: str, action: str):
    if (action == "folder"):
        if not os.path.exists(path):
            os.makedirs(path)
    elif (action == "file"):
        if not os.path.isfile(path):
            open(path, 'a').close()
    else:
        raise Exception("Invalid action")


# Add the necessary folders to the system
add_path(ROOT_FOLDER, "folder")
add_path(BIN_PATH, "folder")
add_path(WAREHOUSE_PATH, "folder")
add_path(ALIAS_PATH, "file")

# Add a default alias.json tracker
with open(ALIAS_PATH, 'w') as f:
    json.dump({
        "yap-em": [YAPM_PATH],
    }, f, indent = 4, sort_keys = True)


