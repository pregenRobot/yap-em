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

if not os.path.exists(ROOT_FOLDER):
    os.makedirs(ROOT_FOLDER)



# if not os.path.exists(ROOT_FOLDER):
    # os.makedirs(ROOT_FOLDER)




