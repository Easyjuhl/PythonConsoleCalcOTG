#For Errorhandling
from time import sleep

#Handles value errors
def valerror(val):
    print("Error: Your input {} is not a valid input".format(val))
    sleep(5)
