import sys,numpy as np,json,os,importlib,copy,time,re
sys.path.append("google-code-golf-2025\\code_golf_utils")

import warnings
warnings.simplefilter("ignore")
from code_golf_utils import *
def load_examples(task_num):
  """Loads relevant data from ARC-AGI and ARC-GEN."""
  if not task_num:
    return task_zero
  with open("inputs\\"+f"task{task_num:03d}.json") as f:
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
        result = program(example_copy["input"])
        result = json.dumps(result)
        result = result.replace("true", "1").replace("false", "0")
        unsafe_chars = re.compile(r"[^0-9,\[\]\s\.]")
        if unsafe_chars.search(result):
          raise ValueError(f"Invalid output from user code: {result[:500]}")
        result = json.loads(result)
        user_output = np.array(result)
        label_output = np.array(example_copy["output"])
        if np.array_equal(user_output, label_output):
          right += 1
        else:
          expected = copy.deepcopy(example)
          wrong += 1
      except KeyboardInterrupt:
        return
      except Exception as e:
        print(e)
        wrong += 1
    return right, wrong, expected
  arc_agi_right, arc_agi_wrong, arc_agi_expected = verify(examples["train"] + examples["test"])
  arc_gen_right, arc_gen_wrong, arc_gen_expected = verify(examples["arc-gen"])
  if arc_agi_wrong + arc_gen_wrong == 0:
    return True
  else:
   return False

pass_cnt = 0
fail_cnt = 0
failed = []
slow = []

for n in range(1,401):
 path = "submission\\task%03d.py"%n
 if os.path.exists(path):
     start = time.time()
     if verify_task_test(n, path):pass_cnt += 1;print(f"{n:03d}: PASS")
     else:fail_cnt += 1;failed += [n];print(f"{n:03d}: FAIL")
     t = time.time()-start
     if t > 20: print(f"{n:03d}: SLOW");slow.append((t, n))
     

print("FAILED:", fail_cnt, failed)
for t,n in sorted(slow)[::-1]: print(f"{n:03d}:", int(t), "seconds")