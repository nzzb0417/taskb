# Your name: Abdimalik Hussein [1]
# Your student ID: 202028878 [1]
# You state that the code submitted is wholly written by yourself. [1]
# Date: 01/02/2025 [1]
systime = 0

maxtime = int(input())

while systime <= maxtime:

    count = systime % 15

    if count < 4:
        state = "red"

    elif count < 7:
        state = "red_amber"

    elif count < 12:
        state = "green"

    else:
        state = "amber"

    print(f"Time {systime:03} State {state}")

    systime = systime + 1






# Simulate the traffic light system up to time=maxtime in 1-second steps [2]

# at the end of each step you should output the time and state using the statement 
