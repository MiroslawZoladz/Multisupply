# import os

nonvolatile_float_obj_ctr = 0

class nonvolatile_float:   
    
    def __init__(self):
        global nonvolatile_float_obj_ctr
        
        self._filename = f"../nv/vf_{nonvolatile_float_obj_ctr}.txt"
        try:
            with open(self._filename, "r") as file:
                self._data = float(file.read())
        except OSError:
            self._data = None
            
            
        nonvolatile_float_obj_ctr+=1
    
    def save(self):
        with open(self._filename, "w") as file:
            file.write(str(self._data))
        
    def get(self):
        return self._data
    
    def set(self, data):
        self._data = data