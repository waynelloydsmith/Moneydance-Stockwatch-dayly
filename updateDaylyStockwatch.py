#!/usr/bin/env python
# called by RunScripts

import sys


# this takes a long time to run because it trys to write every ticker into moneydance ( 2000 of them ) . 
# I fixed this by filtering the io to moneydance
# the import data files should be down loaded from www.stockwatch.com and be placed in the directory /opt/moneydance/scripts/tmp/StockwatchDay
# goto www.stockwatch.com and click on quotes->download quotes-> Date -> select Exchange -> select csv format -> submit
# you must have a stockwatch account and be logged in
# one file per Exchange . Will contain all of closing values for all of the securties on that exchange . file name can be anything that ends in .csv
# this program processes all the .csv files in the StockwatchDay directory and moves them to /opt/moneydance/scripts/tmp/Done
# the /opt/moneydance/scripts/tmp part of the directory name is defined in the definitions.py script
# Tested on Tsx , New York and Canadian Mutual funds 
# The mutual fund symbols the stockwatch uses are different than what is used by most sites. 
# the StockwatchSymbols list in definitions.py must be filled in to convert the symbols 
# example 'TML202':'BIF*CDN',  my moneydance symbol is TML202 . Stockwatch uses BIF*CDN for this same fund.
# stock symbols are automaticly converted by this program from AAA.AA.A to AAA-AA-A-T or AAA-AA-A-N
# ie the stockwatch dots are converted to GlobeIvestor dashes and the exchange is tacked on the end -T is TSX -N is newyork
# <ticker>	<date>	   <exchange>	<open>	<high>	<low>	<close>	<change>	<vol>	<trades>
# BRN*GLO	20141117	F	10.9856	10.9856	10.9856	10.9856	 -0.01	          0	0
# the above is the standard ASCII csv format produced by Stockwatch
# 
# Exchange codes used by Stockwatch
# Code 	Region 	Exchange
# U 	US 	Special code that matches any US symbol
# C 	Canada 	Special code that matches any Canadian symbol
# Z 	US 	Composite feed including the New York and American exchanges -- confirmed GlobeInvestor uses -N
# Q 	US 	Nasdaq, OTCBB, Pink Sheets and Other OTC
# O 	US 	OPRA - US Options
# S 	US 	S&P indexes
# P 	US 	PBOT indexes
# B 	US 	CBOE indexes
# I 	US 	Non-exchange and other indexes such as Dow Jones, Russel, Longon Gold Fix
# T 	Canada 	TSX - Toronto Stock Exchange -- confirmed same as GlobeInvestor
# V 	Canada 	TSX Venture Exchange Calgary
# M 	Canada 	Montreal Exchange
# C 	Canada 	CSE
# F 	Canada 	Canadian Mutual Funds  -- confirmed
# E     NEO

# on the jython270 console run ----->>>execfile("updateDaylyStockwatch.py")
# issue #1 stockwatch doesn't use fundserv fund numbers so we have to convert them . example BIP151 = BRN*GLO
# issue #2 stockwatch is missing the mutual fund GOC309

class updateDaylyStockwatch:
   import glob
   import sys
#   execfile("/opt/moneydance/scripts/definitions.py")
   from definitions import definitions
   
   def setPriceForSecurity(symbol, price2, dateint , volume2 , high2 , low2 ): # this version is the latest Dec 29 2017

     root = moneydance.getRootAccount()
  ##   currencies = root.getCurrencyTable() fix from roywsmith
     AcctBook = root.getBook() 
     currencies = AcctBook.getCurrencies()
     if price2 != 0:
       price2 = 1/price2
     else:
       print "Error Zero Price found Skipping it"
       return
     if low2 != 0:
       low2   = 1/low2
     else:
       low2 = price2
     if high2 != 0:
       high2  = 1/high2
     else:
       high2 = price2 
     security = currencies.getCurrencyByTickerSymbol(symbol) #returns a CurrencyType
     if not security:
       print "No security with symbol/name: %s"%(symbol)
       return
     if dateint:
       snapshot = security.setSnapshotInt(dateint, price2) # this returns a CurrencyType.Snapshot
       security.setUserRate(price2)
       snapshot.setDailyVolume (long(volume2) )
       snapshot.setUserRate ( price2 )
       snapshot.setUserDailyHigh ( high2 )
       snapshot.setUserDailyLow ( low2 )
       security.setSnapshotInt(dateint, price2).syncItem() # added this April 19 2019 for change in MD2019 see note below
     else:  
       print "No Date for symbol/name: %s"%(symbol)
       
# words of wisdom from Sean Reilly on Jan 02 2019 
#Ah yes, sorry about that. We moved a while ago to requiring a sync/save call for snapshots to prevent an overflow of history entries which were coming from 
#calls to create snapshots which weren't meant to be saved. Anyway, you should just change any calls to security.setSnapshotInt(dateint, price) to 
#change any calls to security.setSnapshotInt(dateint, price) to invoke syncItem() on the result: security.setSnapshotInt(dateint, price).syncItem().
#I'll update the sample code now too.

       
#     print price2,volume2,high2,low2
     print "Successfully set price for %s"%(security)	    	      
     
   def setPriceForCurrency(symbol, price2, dateint , volume2 , high2 , low2 ):

     root = moneydance.getRootAccount()
  ##   currencies = root.getCurrencyTable() fix from roywsmith
     AcctBook = root.getBook() 
     currencies = AcctBook.getCurrencies()
     if price2 != 0:
       price2 = 1/price2
     else:
       print "Error Zero Price found Skipping it"
       return
     if low2 != 0:
       low2   = 1/low2
     else:
       low2 = price2
     if high2 != 0:
       high2  = 1/high2
     else:
       high2 = price2 
     security = currencies.getCurrencyByIDString(symbol) #returns a CurrencyType
     if not security:
       print "No security with ID String: %s"%(symbol)
       return
     if dateint:
       snapshot = security.setSnapshotInt(dateint, price2) # this returns a CurrencyType.Snapshot
       security.setUserRate(price2)
       snapshot.setDailyVolume (long(volume2) )
       snapshot.setUserRate ( price2 )
       snapshot.setUserDailyHigh ( high2 )
       snapshot.setUserDailyLow ( low2 )
       security.setSnapshotInt(dateint, price2).syncItem() # added this April 19 2019 for change in MD2019 see note below
     else:  
       print "No Date for currency: %s"%(symbol)

       
#     print price2,volume2,high2,low2
     print "Successfully set rate for %s"%(security)	    	      
     
     
   execfile("fetchhtmlDaylyStockwatch.py") #    go get the end of day close prices     	    	      
   execfile("fetchhtmlDaylyStockwatchIndexs.py") #    go get the end of day Indexs    	    	      
   
   files = glob.glob(definitions.directory+'StockwatchDay/*.csv') # open the directory to be processsed 
                                                                  # should be a file containing the days closing prices for all the stocks on the TSX
   
#   print files
   
   for fle in files:
    fin = open(fle,'r')
#      with open(fle) as fin:
#      fin = open(fle,'r')
#	sym = fin.readline() # disgard the first line its a header
#	print sym            # print the header           
       
   
   
#   fin = open(definitions.directory+'Stockwatch.csv','r') # could use a hard coded file location  /opt/moneydance/scripts/tmp
    print fle   
    sym = fin.readline() # disgard the first line its a header
    print sym            # print the header           

    while 1:
       sym = fin.readline()
       if len(sym) <= 0:
         break
#       sym = sym.replace(',',' ') # strip out all the comma s
     
       lst = sym.split(",") # chop it up into 10 fields    

   #  print lst[0] #ticker
   #  print lst[1] #date
   #  print lst[2] #exchange
   #  print lst[3] #open
   #  print lst[4] #high
   #  print lst[5] #low
   #  print lst[6] #close
   #  print lst[7] #change
   #  print lst[8] #volume
   #  print lst[9] #trades
       if lst[2] == 'F': # check the exchange field to see if its a mutual fund .. currently not being downloaded see fetchhtmlDaylyStockwatch.py
#          print 'Its a Mutual Fund' # so we need to look up the symbol being used in moneydance
          tickerSym = None
          ticker2 = lst[0]
     
          for mdSym , swSym in definitions.StockwatchSymbols.items():  # use this list in definitions to look up the moneydance mutual fund ticker
#        print fundsym , fundname            # the key is backwards on this Dictionary for this query
#        print len(fundname)
	     if len(swSym) <= 0: break
	     if  swSym.count (ticker2) > 0:
	       print "found it", mdSym ,swSym
	       tickerSym = mdSym
#	     print "found tickerSym=",tickerSym
	       break
          if tickerSym == None:	
#	     print "updateDaylyStockwatch.py Ticker symbol Look up failed ------------------------"
	     continue
       elif lst[2] == 'I': # check the exchange field to see if its an Index ($ exchange rate)
#         print 'Its an Index' # so we need to look up the moneydance IDsymbol
          tickerSym = None
          ticker2 = lst[0]
     
          for mdID , swSym in definitions.StockwatchIndexs.items():  # use this dictionary in definitions to look up the currency ID
#        print mdID , swSym                 # the key is backwards in this dictionary for this query
#        print len(swSym)
	     if len(swSym) <= 0: break
	     if  swSym.count (ticker2) > 0:
#               print "found it", mdID ,swSym
	       tickerSym = mdID # will be the currency ID
#	     print "found tickerSym=",tickerSym
	       break
          if tickerSym == None:	
#	     print "updateDaylyStockwatch.py Ticker symbol Look up failed ------------------------"
	     continue	   
       else : 
         tickerSym = lst[0] # need to add a -T to the end of it to match the Globeinvestor standard
         tickerSym = tickerSym.replace('.','-')  #  sym = sym.replace(')',' ')  Stockwatch uses dots but GlobeInvestor uses dashes
         if lst[2] == 'T':
             tickerSym = tickerSym+'-T' # if its the TSX
         elif lst[2] == 'Z':    
             tickerSym = tickerSym+'-N' # if its the NewYork  Stockwatch=Z and GlobeInvestor=N differ here  
         elif lst[2] == 'V':    
             tickerSym = tickerSym+'-X' # Toronto Venture Exchange    
         elif lst[2] == 'E':    
             tickerSym = tickerSym+'-NEO' # The Aequitas NEO Exchange             
#         elif lst[2] == 'I': 
#	     print "Its the Indexes file ",lst[2],tickerSym
#	     raise ValueError('Index file')
         else: 
	     print "Unknown Exchange ",lst[2],tickerSym
	     raise ValueError('Unknown Exchange Code') # worked great script execution stopped cold here but moneydance kept running.
# ------------------ end while(1):	   
       volume = long (lst[8])  
       high = float ( lst[4] )
       low =  float  ( lst[5])
# --------------- looks like the date is already in the right format 
     
       number = int( lst[1] ) # this is the date
# if its not in the Stockwatch list we'll just skip it   
# moneydance was locking up rejecting all the symbols we really don't need    
# the webpage isn't required for this check . just need the symbol in the list . could put a fake web page in it.
# the key is useful on this dictionary so we'll use it
       try:
         webpage =  definitions.StockPriceHistoryStockwatch[tickerSym] 
       except KeyError as e:
#	 print "Not Wanted by md"
	 webpage = None
       else:
         print tickerSym,float(lst[6]),number,volume,high,low
         if lst[2] == 'I': # its an Index
	    setPriceForCurrency(tickerSym,float(lst[6]),number , volume , high , low )            # this is a local function
         else: 
            setPriceForSecurity(tickerSym,float(lst[6]),number , volume , high , low )            # this is a local function
###       print tickerSym,float(lst[6]),number,volume,high,low
#     break 
#   print fle+" time to move it"  # fle has a full path
    dest = fle
    dest = dest.replace('/',' ')
    dest = dest.strip()
    lst = dest.split()
    filename = lst[len(lst)-1]
    import os
#   print filename
    print definitions.directory+'Done/'+filename
    os.rename(fle, definitions.directory+'Done/'+filename) # opt/moneydance/scripts/tmp/Stockwatch/Stockwatch6.csv
     
   print "Done updateDaylyStockwatch.py"

