import sys
sys.path.append('../lib')

from machine import Pin, SoftSPI

class DAC:
    
    def __init__(self, spi_sck_pn, spi_mosi_pn, spi_miso_pn, spi_cs): # spi_miso_pn dumy, must by any input pin 
        
        #spi
        sck  = Pin(spi_sck_pn, Pin.OUT)
        mosi = Pin(spi_mosi_pn, Pin.OUT)
        miso = Pin(spi_miso_pn, Pin.IN) 
        self.cs   = Pin(spi_cs, Pin.OUT, value = 1)
        
        self.spi = SoftSPI(baudrate=100000, polarity=0, phase=0, bits=8, firstbit=SoftSPI.MSB, sck=sck, mosi=mosi, miso=miso)
                
        # other
#         self.callib_min = nonvolatile_float() 
#         self.callib_max = nonvolatile_float() 

    def gnd(self): #Power-Down with 1kΩ to GND        
        msb = 0b0010000
        lsb = 0x00 
        self.cs.off()
        self.spi.write(bytearray([msb,lsb]))
        self.cs.on()
        
    # Procedura kalibracji, argumenty w woltach
    # 1. set_min
    # 2. write down
    # 3. set_max
    # 4. write down
    # 5. calib(min,max)        
#     def callib(self, min_in_V, max_in_V):
#         self.callib_min.set(min_in_V)
#         self.callib_max.set(max_in_V)
#         self.callib_min.save()
#         self.callib_max.save()
        
        
#     def voltage(self,V):
#         assert self.callib_min.get() != None or self.callib_max.get() != None , 'err dac_not_calibrated'
#         assert  self.callib_min.get() <= V <= self.callib_max.get(), 'err voltage_out_of_valid_range'
#         lsb = int(((V-self.callib_min.get())*self.RANGE_MAX_LSB)/(self.callib_max.get()-self.callib_min.get()))+1
#         self.raw(lsb)
                
    def raw(self,value):
        msb = (value>>8) & 0x0F
        lsb = value & 0xFF 
        self.cs.off()
        self.spi.write(bytearray([msb,lsb]))
        self.cs.on()        

    # Testy klasy DAC
    # bp = BoardPinout()
    # dac = DAC(bp.SPI_SCK, bp.SPI_MOSI, bp.SPI_MISO_ADC_0_7, bp.SPI_CS_DAC_OUT0)
    # # dac.set_gnd()
    # # dac.set_raw(0)
    # # dac.set_raw(0xfff)
    # dac.calib(0.0036,3.3065)
    # dac.set_voltage(1.234)


