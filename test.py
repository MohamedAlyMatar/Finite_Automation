transitions = {frozenset({'q0', 'q2', 'q1'}): {'0': 'q3', '1': 'q3'}, frozenset({'q3'}): {'1': 'q4'}}
new_keys = []
new_dict = {}
c = 0
for k in transitions.keys():
    new_keys.append(str(k)[11:-2].replace("'", "").replace(" ", ""))
    new_dict[new_keys[c]] = transitions[k]
    c += 1
transitions = new_dict
print(transitions)
# print(transitions.items())
