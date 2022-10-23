from math import *

class IPFragmentationCalculator:
  def __init__(self, pkt_size, mtu, frags=0):
    self.pkt_size = pkt_size
    self.mtu = mtu
    
    
  def no_of_fragments(self):
    '''displays the number of fragments the data packet will be divided into'''
    
    pkt = ( (self.pkt_size - 20) / (self.mtu - 20) )
    self.frags = ceil(pkt)
    self.total_length()
    
    
  
  def total_length(self):
    '''displays the total length of the data packet after fragmentation'''
    
    print(f"Inside total_length : {self.frags}")
    
    tl = 0                      # total length
    rem_payload = self.pkt_size - 20       # actual payload to be sent
    print(f"Remaining payload : {rem_payload}")
    
    
    while( rem_payload > self.mtu ):
      rem_payload = rem_payload - (self.mtu-20)
      print(f"Remaining payload : {rem_payload}")
    
    tl = self.pkt_size + rem_payload + 20     # the last fragment may be smaller than the payload in a datagram i.e. excluding IP headers (MTU - 20)
    print(f"The total size is : {tl}")    
    
  
  # def MF_Flag():
  #   pass

  def Offset(self):
    scaling_factor = 8
    tl = 0
    while tl < self.pkt_size:
      tl = tl + self.mtu
    pass
  
if __name__ == "__main__":
  PKT_SIZE = int(input("Enter the size of IP data packet to be sent : "))
  MTU = int(input("Enter the size of MTU : "))
  
  if (isinstance(PKT_SIZE, int) and isinstance(MTU, int)):
    obj1 = IPFragmentationCalculator(PKT_SIZE, MTU)
    obj1.no_of_fragments()
    
    
# obj1 = IPFragmentationCalculator()
# obj1.no_of_fragments()

  
  