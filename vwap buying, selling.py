from datetime import datetime
from pynse import *
import time


watchlist = ['SBIN','INFY','WIPRO','RELIANCE','ADANIENT',
                'TATAPOWER', 'TECHM', 'TITAN','JSWSTEEL', 'SBILIFE',  'M&M',
                'TATAMOTORS', 'TATASTEEL','TATACHEM',  'TCS', 'WIPRO']
nse=Nse()
count  = 0
buying = []
selling = []
while True:
  for i in watchlist:
    #  print(i)
            a = nse.get_quote(i)
            vwap = int(a['vwap'])
            ltp = int(a['lastPrice'])
            # print("ltp is:",ltp)
            # print("vwap is:",vwap)
            if vwap < ltp:
                  buying.append(str(i))
                  print("BUY SIGNEL in: "+str(i))
            elif vwap>ltp:
                  selling.append(str(i))
                  print("SELL SIGNEL: "+str(i))
              #prnt(i)
            count += 1
  print("-----------------------------------------------------")            
  time.sleep(300)
  
