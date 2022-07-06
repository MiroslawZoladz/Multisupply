import serial

class Multimeter:
    def __init__(self,com_nr):
        self.com_nr = com_nr
        # self.check_id()
        
    def commmand(self,cmd):
       
        comm = serial.Serial(f'Com{self.com_nr}',115200,timeout=1)
        comm.flushInput()
        
        comm.write(cmd.encode('UTF-8')+b'\r\n')
        comm.flushOutput()
        
        comm.readline()
        res = comm.readline()
        
        comm.close()
        
        return res    
    
    def check_id(self):
        res = self.commmand('id').strip()
        assert res == b'multimeter', 'multimeter module not found'
    
    def ai(self,ch_nr=''):
        res = self.commmand(f'i {ch_nr}')
        return  list(map(float,res.split()[:-1]))
    
    def ao(self,out0, out1):
        self.commmand(f'o {out0} {out1}')


# USAGE EXAMPLE
mm = Multimeter(10)
_ = mm.commmand('sda')
print(_)

