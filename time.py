import time
import subprocess
from pathlib import Path

text = \
"""\
# project-euler  
https://projecteuler.net/

"""

files = sorted(Path('./src').glob('*.py'))
for file in files:
  print(file)
  now = time.time()
  subprocess.run(['python', file])
  exec_time = time.time() - now
  text += '\n'.join([
    '---',
    f"{file.name}",
    str(exec_time),
    '\n',
  ])


Path('./README.md').write_text(text)