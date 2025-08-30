import sys
sys.path.append("google-code-golf-2025\\code_golf_utils")
from code_golf_utils import *
def load_examples(task_num):
  """Loads relevant data from ARC-AGI and ARC-GEN."""
  if not task_num:
    return task_zero
  with open("google-code-golf-2025\\"+f"task{task_num:03d}.json") as f:
    examples = json.load(f)
  return examples

def verify_task_test(task_num, path):
  examples = load_examples(task_num)
  task_name, task_path = "task_with_imports", path
  spec = importlib.util.spec_from_file_location(task_name, task_path)
  if spec is None:
    print("Error: Unable to import task.py.")
    return
  module = sys.modules[task_name] = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  if not hasattr(module, "p"):
    print("Error: Unable to locate function p() in task.py.")
    return
  program = getattr(module, "p")
  if not callable(program):
    print("Error: Function p() in task.py is not callable.")
    return
  def verify(example_subset):
    right, wrong, expected = 0, 0, None
    for example in example_subset:
      example_copy = copy.deepcopy(example)
      try:
        if program(example_copy["input"]) == example_copy["output"]:
          right += 1
        else:
          expected = copy.deepcopy(example)
          wrong += 1
      except:
        wrong += 1
    return right, wrong, expected
  arc_agi_right, arc_agi_wrong, arc_agi_expected = verify(examples["train"] + examples["test"])
  arc_gen_right, arc_gen_wrong, arc_gen_expected = verify(examples["arc-gen"])
  if arc_agi_wrong + arc_gen_wrong == 0:
    return True
  else:
   return False

task_nums = []
failed = []

import os
import zlib
total_save=0
for n in (task_nums or range(1,401)):
 path = "submission_passing_\\task%03d.py"%n
 wpath = "submission_zipped\\task%03d.py"%n
 if not os.path.exists(path):continue
 body = ""
 with open(path,"rb") as file:
  s=bytes([b for b in file.read()if b!=13])
 comp = zlib.compress(s,9)
 delim = b'"""'
 if ord('"')not in comp and ord("\n")not in comp:delim=b'"'
 executable = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("+delim+comp+delim+b",\"L1\")))"
 exe2 = bytearray()
 for ch,ch1 in zip(executable,executable[1:]+b"_"):
  if   ch==0  : exe2+=b"\\x00" if ch1 in b"01234567" else b"\\0"
  elif ch==13 : exe2+=b"\\r"
  elif ch==92 : exe2+=b"\\\\"
  else:         exe2.append(ch)
 exe2=b""+exe2
 prev_len = len(s)
 save=max(0,len(s)-len(exe2))
 if save:
  with open("temp_zipped.py","wb")as file:
   file.write(exe2)
  if(verify_task_test(n,"temp_zipped.py")):
   total_save += save
   s=exe2
  else:print("FAILED #",n);failed.append(n)
 print(f"task{n:03d}.py: saved {save/prev_len:.02%} ({save}b/{prev_len}b)")
 with open(wpath,"wb")as file:
  file.write(s)

print(f"saved {total_save}b")

if failed:print(f"FAILED:\n{failed}")
else:print("ALL PASSED")
