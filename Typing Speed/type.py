from time import *
import random as r


# caculating the speed / words 
def speed_time(time_start, time_end, text_input):
    time_diff = time_end - time_start
    time_roundoff = round(time_diff, 2)
    speed = len(text_input) / time_roundoff
    return round(speed, 2)

# counting the mistakes
def mistake(text_shown, text_input):
    error = 0
    for i in range(len(text_shown)):
        try:
            if text_shown[i] != text_input[i]:
                error += 1
        except :
            erorr += 1
    return error


# List of random second
test = ["A quick brown fox jump over lazy dog", "So, you just typed from a to z", "And that's it Now is the time to go because the game is on."]

# print statements
print(" \n *** Typing speed calculator *** \n ")
text_shown = r.choice(test)
print(text_shown, "\n")

# starting the timer
time_start = time()

# taking input from user
text_input = input("Enter the above text \n")

# ending the timer
time_end = time()

print("Speed: ", speed_time(time_start, time_end, text_input), " characters per second")
print("Error: ", mistake(text_shown, text_input))