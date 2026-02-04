
# demo 1 — базовый цикл whileс необычными именами

quantum_counter = 1
while quantum_counter < 6:
    print(quantum_counter)
    quantum_counter += 1

# demo 2  while с break
#

warp_index = 1
while warp_index < 6:
    print(warp_index)
    if warp_index == 3:
        print("Warp field stabilized — breaking loop!")
        break
    warp_index += 1


#demo3 — while с continue


phase = 0
while phase < 6:
    phase += 1
    if phase == 3:
        print("Phase 3 skipped!")
        continue
    print(phase)


#demo 4— while с else

cycle = 1
while cycle < 6:
    print(cycle)
    cycle += 1
else:
    print("Cycle counter reached its maximum limit")
