import sys
import subprocess
from datetime import datetime
import os

args = sys.argv[1:]
print(args)

day = int(args[0])
part = int(args[1])


os.chdir(f"day{day}")
start_time = datetime.now()
subprocess.call(["python3", f".\\day{day}-part{part}.py"])
end_time = datetime.now()

print(end_time - start_time)