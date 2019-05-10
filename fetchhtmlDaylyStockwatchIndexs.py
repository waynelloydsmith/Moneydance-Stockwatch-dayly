#!/usr/bin/env python
#purpose is to get the csv index data to update the currencies (exchange rates in money dance) FX$CAD/USD
# choice of indexes #of values
# B -CBOE Indexes        305       "Chicago Board of Trade" example BFLY is the Cboe S&P 500 Iron Butterfly Index
# F - Mutual Funds        0
# H - PBOT Indexes        5        "Philadelphia Board of Trade" 
# I Indexes              4482 
# Q Nasdaq               8100
# S S&P Indexes          2490
# X Amex                 2013
# NYSE                   3109
#The download you requested can be performed by the following URL:
#https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&date=20180330&exopt=N&ex=I&ats=N&id=userName&pw=password
#Note: If you leave out the &date=<date> part you will get the most recent date available. Otherwise set it to the specific date you want.
#This URL will always give you the most recent date:
#https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=I&ats=N&id=userName&pw=password
# the above was with I selected &ex=I , should use https
# the I Indexes contains the currencys FX$.... FX$CAD/USD is 0.7757   FX$USD/CAD is 1.28825 there are around 100 CAD conversions in this file


# called from updateDaylyStockwatch.py
##### sqlite is broken in MD 2019 so going back to loggin with a password  


import sys
import urllib2
import urllib
import subprocess

# use jython to get the cookie . sqlite is broken in moneydance 2019
try:
            output = subprocess.check_output(
                ['jython', '/opt/moneydance/scripts/fetch-Stockwatch-ID.py'],
                stderr=subprocess.STDOUT).decode('UTF-8')
#	        universal_newlines=True).decode('UTF-8')
except subprocess.CalledProcessError as e:
            print "It Failed"
            print e.output  # Traceback messages 
            raise

print "output=",output # normal print from python script
            
file1 = open('/opt/moneydance/scripts/tmp/stockwatchID.txt', 'rb')
print file1    
XXX = file1.read()
file1.close()

file2 = open('/opt/moneydance/scripts/tmp/StockwatchDay/indexs.csv', 'wb')
print file2


#url = "https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&date=20180330&exopt=N&ex=I&ats=N&id=userName&pw=password"
#url = "https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&date=20180330&exopt=N&ex=I&ats=N"
url = "https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=I&ats=N" # removed &date

print url
opener = urllib2.build_opener()
#opener.addheaders = [('User-Agent', 'Mozilla/5.0')] # was enough to fool NEO 
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0 SeaMonkey/2.49.1 Slackware/14.2')]
#opener.addheaders.append(('Cookie', '__AntiXsrfToken=f7d2c333e118449996f9040e8498a912')) # failed
###
opener.addheaders.append(('Cookie','XXX='+XXX)) # success



req = urllib2.Request(url)
try:
#  response = urllib2.urlopen(req)
  response = opener.open(url)
except urllib2.URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    if hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:  
  print response.headers   
  webContent = response.read()           # just got a single line of column headings when the market was closed.for days close request
#  print 'length=', len(webContent)       #  got  1932 lines when I specified a day  
#  print webContent


  file2.write(webContent) # this function does not return anything useful
  file2.close() 

## results of test run .. success got 4483 lines of values including 1790 currencies 
##>>> execfile("dev-stockwatch-indexs.py")
##<open file '/opt/moneydance/scripts/tmp/StockwatchDay/indexs.csv', mode 'wb' at 0xc>
##44003922%2c385549%2c700028%2cuserName
##https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&date=20180330&exopt=N&ex=I&ats=N
##Cache-Control: private
##Content-Type: application/mytext; charset=utf-8
##Server: Microsoft-IIS/8.5
##Content-Disposition: Attachment; Filename="data.txt"
##X-AspNet-Version: 4.0.30319
##Set-Cookie: __AntiXsrfToken=39ab1db4198c4e85b6498204b7df7e52; path=/; HttpOnly
##X-Powered-By: ASP.NET
##Date: Mon, 02 Apr 2018 17:35:54 GMT
##Connection: close
##Content-Length: 272835
