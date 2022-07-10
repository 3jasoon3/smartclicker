import mouse
from collections import OrderedDict
import keyboard
from parser import parse
from events import get_event
def listen(start_key, end_key)->set:
    coordinates = []
    is_started = False
    try:
        while True:
            if keyboard.is_pressed(start_key):
                if is_started==False:
                    print(get_event("start"))
                    is_started = True
                ''' We should get points which has been pressed and commit theim '''
            if is_started == True:
                while True:
                    if mouse.is_pressed(button='left') :
                        coordinates.append((mouse.get_position()))

                    if keyboard.is_pressed(end_key):
                        print(get_event("stop"))
                        ''' We have stopped our listennig, leaving from cycles '''
                        raise
                        
            
            
    except:  
        return list(OrderedDict.fromkeys(coordinates))



def repeat(coordinates):
    try:
        for i in range(len(coordinates)-1):
            start_x, start_y = coordinates[i]
            end_x, end_y = coordinates[i+1]
            mouse.drag(start_x, start_y, end_x, end_y, duration=0.3)

    except StopIteration:
        print(get_event("done"))




