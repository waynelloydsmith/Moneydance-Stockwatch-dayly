#!/usr/bin/env python

# called from updateDaylyStockwatch.py

# testing to try and get the stockwatch dayly close prices with out sending my user name and password
# I was able to do  Download.aspx fussy about the way I'm was passing the cookies to it.
# the WebQuery worked fine with &auth=
# I got it to work using the XXX cookie from seamonkey . I had a space at the start of the XXX token
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


#raise Exception('I know Python!')


file2 = open('/opt/moneydance/scripts/tmp/StockwatchDay/stockwatch.csv', 'wb')
print file2

#url =  'http://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&date=20171222&exopt=N&ex=T&ats=N&id=username&pw=password' # end of day closing worked great
#url = 'http://www.stockwatch.com/Quote/WebQuery.aspx?what=quote&format=comma&fields=SXRLVOHITE&pf=1&region=C&header=Y&id=username&pw=password' # my portfolio worked great
#url = 'http://www.stockwatch.com/Quote/WebQuery.aspx?what=quote&format=comma&fields=SXRLVOHITE&pf=1&region=C&header=Y&auth=43704855,385549,631607,username' 
# the above worked on my portfolio and seamonkey session didn't logout..... os where is seamonkey putting this XXX cookie ?
# found it in /home/wayne/.mozilla/seamonkey/iOtpuie4.default/cookies.sqlite use seamonkey/datamanger to see it.
# the cookie XXX matches the number on https://www.stockwatch.com/Quote/Webquery.aspx
# the auth parameter did not work with the Download.aspx so would need to do it by portfolio or one at a time.
# need to figure out how to get the XXX cookie out of cookie.sqlite then you just need to log into stockwatch before you run the script.
# no more sending passwords to stockwatch.

#&ex=TE   gets both NEO and the TSX
#&ats=Y   includes volumes from the ATS exchanges
#&exopt=N ???  I changed this to Y and didnt see any difference in the files
#Exchange	# Data Point
#B - CBOE Indexes	301	american indexes
#C - CSE	        215	Canadian Securities Exchange 
#D - CanDeal	        649	Canadian Bonds
#E - AQ-NEO	         31	
#F - CA Mutual Funds	7062	
#I - Indexes	        4830 has exchanges rates in it.	
#Q - Nasdaq	        8740	
#S - S&P Indexes	2482	
#T - TSX	        1892	
#V - TSX-V	        1320	
#X - Amex	        2020	
#Z - NYSE	        3101	
#M - Montreal	        2845	was empty 
#O - OPRA	       121469   options
# so currently there is no mutual fund prices in the download file. I don't have any  ..need &ex=TEVF for this...

#url = 'https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=T&ats=Y&id=userName&pw=password' # most recent end of day closing no date returns empty file if markets are closed
url = 'https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=TEV&ats=Y' # most recent end of day closing no date returns empty file if markets are closed

print url
opener = urllib2.build_opener()
#opener.addheaders = [('User-Agent', 'Mozilla/5.0')] # was enough to fool NEO 
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0 SeaMonkey/2.49.1 Slackware/14.2')]
#opener.addheaders.append(('Cookie', '__AntiXsrfToken=f7d2c333e118449996f9040e8498a912')) # failed
###
opener.addheaders.append(('Cookie','XXX='+XXX)) # success

req = urllib2.Request(url)
try:
  #response = urllib2.urlopen(req)
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
  print 'length=', len(webContent)       #  got  1932 lines when I specified a day  
#  print webContent


  file2.write(webContent) # this function does not return anything useful .. I changed the permission on the file and crashed the program with an IOError:[Errno 13] Permission denied:  
  file2.close() 
  print "Done fetchhtmlDaylyStockwatch.py"

# below is what www.stockwatch sent me in addition to the csv file.
#>>> execfile("dev-Stockwatch.py")
#<open file '/opt/moneydance/scripts/tmp/StockwatchDay/stockwatch.csv', mode 'wb' at 0x10>
#https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=T&ats=Y
#Cache-Control: private
#Content-Type: application/mytext; charset=utf-8
#Server: Microsoft-IIS/8.5
#Content-Disposition: Attachment; Filename="data.txt"
#X-AspNet-Version: 4.0.30319
#Set-Cookie: __AntiXsrfToken=f7d2c333e118449996f9040e8498a912; path=/; HttpOnly
#X-Powered-By: ASP.NET
#Date: Tue, 23 Jan 2018 00:32:39 GMT
#Connection: close
#Content-Length: 110891
# it worked even though I didn't fill in the __AntiXsrfToken
#see _ViewState protect against CSRF/XSRF attacks. 
# so i filled in the __AntiXsrfToken and it failed . I took it out and it worked.??
# so log in to stockwatch with seamonkey and we'll pull the number out of seamonkey with sqlite
#below it watch www.stockwatch.com sends you when you first log in
#Set-Cookie: __AntiXsrfToken=fbe40c645e3843b38bdc9dc90b7c2614; path=/; HttpOnly
 
#Set-Cookie: XXX=43706343%2c385549%2c978934%2cuserName; domain=.stockwatch.com; expires=Mon, 21-Jan-2019 21:27:04 GMT; path=/
# ASP.NET is microsoft . .aspx is an ASP.NET Web Forms page http://msdn.microsoft.com/en-us/library/2wawkw1c.aspx 

