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
    
  
  def MF_Flag(self):
    '''records the MF flag'''
    sr_pkt_no = self.frags                   # serial packet number
    i = 0
    
    while( True ):
      i += 1
      if (sr_pkt_no > 1):
        sr_pkt_no = sr_pkt_no - 1
        print(f"MF {i}: 1")
      else:
        print(f"MF {i}: 0")
        break
    

  def Offset(self):
    scaling_factor = 8  
    payload = ceil((self.pkt_size - 20) / scaling_factor)      # actual data to be sent in bytes
    fragment_payload = ceil((self.mtu - 20) / scaling_factor)      # data bytes that each fragment carries in bytes
    offset = 0                  
    i = 0                                   # loop counter
    
    while(i < self.frags):
      i += 1
      print(f"Offset {i} : {offset}")
      offset = fragment_payload*i
      payload = payload - fragment_payload       
  
  
if __name__ == "__main__":
  PKT_SIZE = int(input("Enter the size of IP data packet to be sent : "))
  MTU = int(input("Enter the size of MTU : "))
  
  if (isinstance(PKT_SIZE, int) and isinstance(MTU, int)):
    obj1 = IPFragmentationCalculator(PKT_SIZE, MTU)
    print()
    obj1.no_of_fragments()
    print()
    obj1.MF_Flag()
    print()
    obj1.Offset()
    

  
  