from z3 import *
import json

def load_examples(task_num):
    """Loads relevant data from ARC-AGI and ARC-GEN."""
    with open("inputs/"+f"task{task_num:03d}.json") as f:
        examples = json.load(f)
    return examples

_PyHASH_XXPRIME_1 = 11400714785074694791
_PyHASH_XXPRIME_2 = 14029467366897019727
_PyHASH_XXPRIME_5 = 2870177450012600261
def _PyHASH_XXROTATE(x):
    if type(x) is int: return (x << 31) | (x >> 33)
    else: return RotateRight(x, 33)

bits = 1 << 64

def tuple_prefix(tup):
    acc = _PyHASH_XXPRIME_5
    for lane in tup:
        acc += lane * _PyHASH_XXPRIME_2
        acc &= bits - 1
        acc = _PyHASH_XXROTATE(acc)
        acc &= bits - 1
        acc *= _PyHASH_XXPRIME_1
        acc &= bits - 1

    return acc

def tuple_postfix(acc, length, tup):
    for lane in tup:
        acc += lane * _PyHASH_XXPRIME_2
        if type(acc) is int: acc &= bits - 1
        acc = _PyHASH_XXROTATE(acc)
        if type(acc) is int: acc &= bits - 1
        acc *= _PyHASH_XXPRIME_1
        if type(acc) is int: acc &= bits - 1

    acc += length + len(tup) ^ (_PyHASH_XXPRIME_5 ^ 3527539)
    if type(acc) is int: acc &= bits - 1

    #if acc == bits - 1: return 1546275796
    return acc


sol = Then('simplify',
           'bit-blast',
           'sat').solver()

ex = load_examples(319)

# load examples
ex = ex["train"] + ex["test"] + ex['arc-gen']
ex = ex[:30]
print('trying for %d cases'%len(ex))

# create the tuple
tnum = 4 #max(1, len(ex)//7)  # estimate for min tuple length
tup = [BitVec('O%d'%t,64) for t in range(tnum)]
for n in tup:
    sol.add(n > 0)
    sol.add(n < 128)

target_bit = BitVec("bit", 64)
sol.add(target_bit >= 0)
sol.add(target_bit <= 63)

for t in ex:
    z = (*sum(t['input'],[]),)
    s = sorted({*z},key=z.count)
    g = {s.index(c)for c in {*sum(t['output'],[])}}
    k = tuple_prefix(z)

    r = tuple_postfix(k, len(z), tup) >> target_bit & 1 == min(g)
    r = simplify(r)
    sol.add(r)

print('solving')
# solve
import time
start = time.time()
#print(sol)
print(sol.check())
print("time:", int(time.time()-start))
m = sol.model()
print(m)

tup = *[int(str(m[e]))for e in tup],
target_bit = int(str(m[target_bit]))

print('Bit:', target_bit)
print('Tuple:', tup)

for t in ex:
    z = (*sum(t['input'],[]),)
    s = sorted({*z},key=z.count)
    g = {s.index(c)for c in {*sum(t['output'],[])}}
    out = min(g)
    k = hash((*z, *tup))

    if k >> target_bit & 1 != out: print('Verification Failure'); break
else:
    print('Verification Success')