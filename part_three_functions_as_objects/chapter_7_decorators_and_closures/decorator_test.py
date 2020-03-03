import time
from decorators import clock

@clock
def snooze(seconds):
    time.sleep(seconds)
                                                                                                                                                              
if __name__ == "__main__":
    snooze(.123)
 