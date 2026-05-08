# Your name: Abdimalik Hussein [1]
# Your student ID: 202028878 [1]
# You state that the code submitted is wholly written by yourself. [1]
# Date: 01/02/2025 [1]

states = { "red":4, "red_amber":3, "green":5, "amber":3 } [1]

systime = 0 [1]
maxtime = int(input("Enter the number of steps that you want to complete: ")) # read an integer number of steps (>0) [1]

systime = 0 [1, 2]

state = "red" [1, 2]


while systime <= maxtime: [1, 2]
    count = systime % 15 [1, 2]
    if count >= 0 and count < 4: [1, 2]
        state = "red" [1, 2]
        print(f"Time {systime:03} State {state}") [1, 2]
    elif count >= 4 and count < 7: [1, 2]
        state = "red_amber" [1, 2]
        print(f"Time {systime:03} State {state}") [1, 2]
    elif count >= 7 and count < 12: [1, 2]
        state = "green" [1, 2]
        print(f"Time {systime:03} State {state}") [1, 2]
    elif count >= 12 and count < 15: [2]
        state = "amber" [2]
        print(f"Time {systime:03} State {state}") [2]
    systime = systime + 1 [2]






# Simulate the traffic light system up to time=maxtime in 1-second steps [2]

# at the end of each step you should output the time and state using the statement 
