import math


class node:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival = int(arrival)
        self.duration = math.inf
        self.burst = int(burst)
        self.done = False
        self.inQueue = False
        self.ending = math.inf


name_array = ["A", "B", "C", "D", "E"]
arrival_array = [0, 5, 1, 6, 8]
burst_array = [8, 2, 7, 3, 5]

no_of_prc = len(name_array)

time_quantum = int(input("Enter The Time Quantum : "))

NODES = []

for x in range(no_of_prc):
    new_node = node(name_array[x], arrival_array[x], burst_array[x])
    NODES.append(new_node)

NODES.sort(key=lambda x: x.arrival, reverse=False)

i = NODES[0].arrival
next_i = i
done_nodes = 0

queue = [NODES[0]]
queue[0].inQueue = True
time_for_this_prc = 0
serial_counter = 0

boss_comming = False
front_line_solder = NODES[0]

while done_nodes != no_of_prc:

    for x in NODES:
        if not x.inQueue:
            if i >= x.arrival:
                queue.append(x)
                x.inQueue = True
            else:
                break

    if (i == next_i) and boss_comming:
        queue.append(front_line_solder)

    if i == NODES[0].arrival or i == next_i:

        front_line_solder = queue.pop(0)
        if not front_line_solder.done:
            serial_counter += 1

            if front_line_solder.burst >= time_quantum:
                next_i += time_quantum
                front_line_solder.burst -= time_quantum

                if front_line_solder.burst == 0:
                    front_line_solder.done = True
                    front_line_solder.ending = next_i
                    front_line_solder.duration = front_line_solder.ending - front_line_solder.arrival
                    print(serial_counter, ") ", front_line_solder.name, " --- (", i, ",", next_i, ") --- TAA : ",
                          front_line_solder.duration)
                    done_nodes += 1
                    boss_comming = False
                else:
                    print(serial_counter, ") ", front_line_solder.name, " --- (", i, ",", next_i, ")")
                    boss_comming = True

            else:
                next_i += front_line_solder.burst
                front_line_solder.burst = 0
                front_line_solder.done = True
                front_line_solder.ending = next_i
                front_line_solder.duration = front_line_solder.ending - front_line_solder.arrival
                print(serial_counter, ") ", front_line_solder.name, " --- (", i, ",", next_i, ") --- TAA : ",
                      front_line_solder.duration)
                done_nodes += 1
                boss_comming = False

    i += 1

print()
print()

ATT = 0
for x in NODES:
    ATT += x.duration
ATT = ATT / no_of_prc

print("The Average Time Around Time : ", ATT)