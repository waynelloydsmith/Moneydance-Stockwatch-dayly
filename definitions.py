#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import
# this file is used by almost all of the scripts.
# see updateHistoryStockwatch.py for info on some of the lists stored here 
# a lot of history in this script .. interfaces that I tried and later abandoned
# stockwatch has become the best place to get your US and Canadian stock and mutual fund data
# its not free but its also cheap ,reliable and up to date.

class definitions:
  
   import sys

   ClassPathNames = [   # these items get executed by both the console extensions jconsole270 and jython270 when they are started
   "sys.path.append(r'/opt/moneydance/scripts/jython270/')",  # location of console.py file only needed for the Jython270 console extension
#  "sys.path.append(r'/home/wayne/source/jython2.7.0/jython.jar')",#location of the jython jar file (this is linked to one of the moneydance/jre/ext ,so its not required now )
#  "sys.path.append(r'/home/wayne/source/jython2.7.0/Lib/')", # os.py lives here  ( done with a link to moneydance/jre/ext now, so not required )
#  "sys.path.append(r'/home/wayne/source/jython2.7.0/Lib/site-packages')", # nothing in here
#   "sys.path.append(r'/opt/moneydance/jre/lib/ext/sqlite-jdbc.jar')", # 
   "sys.path.append(r'/opt/moneydance/scripts/')", # custom scripts live here ... needed for import custom.py files to load
   "import os",
   "os.chdir('/opt/moneydance/scripts')", # change the cwd. the jython execfile("custom.py") uses this as its default directory 
#   "import java",
#   "java.lang.System.setProperty('java.library.path','/opt/moneydance/jre/lib/amd64')",  
#   "try:\n  execfile('StockGlance75.py')\nexcept:\n  sys.stderr.write('Jython failed to load StockGlance75.py\\n')\n",  # fire up STockGlance   doesn't work
#   "try:\n  execfile('sitecustomize.py')\nexcept:\n  sys.stderr.write('Jython found no sitecustomize.py\\n')\n",  # run the sitecustomize.py file if it exists
   "try:\n  execfile('runScripts.py')\nexcept:\n  sys.stderr.write('Jython failed to load runScripts.py\\n')\n",  # fire up the script picker swing GUI
   "del buff"
    ]


   directory = "/opt/moneydance/scripts/tmp/" #set this to the directory where you want the temporary files stored.
   
   # remember to create the directory /opt/moneydance/scripts/tmp/
   # should also create /opt/moneydance/scripts/tmp/Done 
   # should also create /opt/moneydance/scripts/tmp/Stockwatch for updateHistoryStockwatch.py..Note:all csv files placed here are processed and moved to tmp/Done
   # should also create /opt/moneydance/scripts/tmp/StockwatchDay for updateDaylyStockwatch.py..Note:all csv files placed here are processed and moved to tmp/Done
   # should also create /opt/moneydance/scripts/tmp/TMX for updateTMX.py need to create a TMX portfolio and save its csv file export here.
   # should also create /opt/moneydance/scripts/tmp/ScotiaBank for Investment account csv file imports.
   # should also create /opt/moneydance/scripts/tmp/BMO for Investment account csv file imports.
                                                                      
# the two structures below are used by the Globe and Mail Canadian mutual fund price update scripts 
# update this list with your mutual fund info . quotes and commas are important .
# both the fund symbol(TML202) and the id (53895) need to be changed. They both can be found on www.globeandmail.com
# the symbols must match what has been entered in moneydance as the ticker symbol
# the globe and mail are busy rebuilding their web site so expect more changes ..
# see globeinvestor.com , globefunddb , http://gold.globeinvestor.com/generated/hubs/home.html
# also https://globeandmail.happyfox.com
# https://secure.globeadvisor.com/

#the globe and mail links below are broken ... Globe has a new web site 
# could be revived by rewrite of fetchhtml but its simpler to use the GlobeInvestor history version which still works (or stockwatch)
# used by fetchhtml.py to get todays canadian mutual fund price from the GlobeInvestor web site
#   FindFund = { 
#  'TML202': 'https://www.theglobeandmail.com/investing/markets/funds/TML202.CF/', #worked
#  'MFC738': 'https://www.quicken.com/investing/mutual-funds/MUTUAL%3AMFC738/Cundill-Canadian-Security-Fund-Series-C', #failed
#  'BIP151': 'http://quote.morningstar.ca/quicktakes/Fund/f_ca.aspx?t=0P000072C0&region=CAN&culture=en-CA', #failed
#  'BIP151': 'https://www.theglobeandmail.com/investing/markets/watchlist/', #failed
#  'FID281': 'https://marketsandresearch.td.com/tdwca/Public/MutualFundsProfile/PerformanceAndRisk/ca/FID281', #worked
#  'BMO471': 'https://ycharts.com/mutual_funds/M:BMO471.TO',  #worked
#  'GOC309': 'https://ycharts.com/mutual_funds/M:GOC309.TO/holdings', #worked
#  'BNS344': 'https://www.msn.com/en-ca/money/funddetails/fi-F0CAN05NUM'     #worked
#  'BNS744': 'http://www.theglobeandmail.com/globe-investor/funds-and-etfs/funds/summary/?id=68435',
#  'BNS361': 'http://www.theglobeandmail.com/globe-investor/funds-and-etfs/funds/summary/?id=18254',
#  'BNS741': 'http://www.theglobeandmail.com/globe-investor/funds-and-etfs/funds/summary/?id=68432',
#  'BMO146': 'http://www.theglobeandmail.com/globe-investor/funds-and-etfs/funds/summary/?id=17696' 
#   }

# used by fetchhhtmlHistory.py to get historical prices of a canadian mutual fund from the globefunddb web site   
#these links still work but the id number is a little harder to find	  
# https://www.theglobeandmail.com/investing/markets/funds/TML202.CF/performance ..three months of price data from barchart
# the corporate actions button of this page pulls up years of dividend history.

# https://secure.globeadvisor.com/
# http://portfoliodb.theglobeandmail.com/gishome/plsql/port_gaf.login
# http://gold.globeinvestor.com/ seems broken
#/www.globefund.com/v5/         ? what is this
# http://globefunddb.theglobeandmail.com/gishome/plsql/gis.fund_filter?pi_type=B  .........use this to find the fund id .. its dead now
# http://globefunddb.theglobeandmail.com/gishome/plsql/gis.analyser .                                 is still working you can get the id with it too
# once you find your fund click on the info table . the id is in the url as pi_fund_id=98881
# plug this number into the queery below and you'll get the last 30 days prices
#   FundTables = {  
#   'TML202':'https://www.theglobeandmail.com/investing/markets/funds/TML202.CF/performance', # this failed (barchart) 
#   'TML202-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=53895',
#   'MFC738-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=51396',
#   'BIP151-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=56107',
#   'FID281-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=60075',
#   'BMO471-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=94801',
#   'GOC309-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=38663',
#   'BNS344-T':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=57442'   
#   'BNS744':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=68435',
#   'BNS361':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=18254',
#   'BNS741':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=68432',
#   'BMO146':'http://globefunddb.theglobeandmail.com/gishome/plsql/gis.price_history?pi_fund_id=17696'
#   }
   
# just list the symbols that are not on the TSX
# used by BMO-Inv-new.py and Scotia-Inv-new.py
   SymbolTable = {  
   'KMB-T':'KMB-N', # Kimberly Clark is on the New York Exchange
   'MHYB-T':'MHYB-NEO',
   'VST-T':'VST-N',     # Vista Energy Corp
   'FCD-UN-T':'FCD-UN-X' # the venture exchange  
   }



   
# info from stockwatch site ->US mutual fund data is received from the Nasdaq feed, 
# therefore the symbols conform to the Nasdaq standard. 
# Each fund has a five letter symbol of which the last letter is always X. The exchange code is Q. 
# Canadian mutual fund Symbols
# info from stockwatch->Canadian mutual fund symbols are of the form GGG*FFF where GGG represents the fund group, and FFF represents the specific fund.
# the list below is the result of different companies using different symbols for the Canadian mutual funds.
# example TML202 (Fundserv Code) = BIF*CDN (Stockwatch) = id=53895 (GlobeInvestor)
# TML202 is recognized by many web sites but BIF*CDN seems to be only used by stockwatch 
# used by updateHistoryStockwatch.py and updateDaylyStockwatch.py to look up the fundserv ticker symbol given the name used by www.stockwatch.com
   StockwatchSymbols = { #mutual funds only.. used by updateHistoryStockwatch.py and updateDaylyStockwatch.py
   'TML202-T':'BIF*CDN',
   'MFC738-T':'CUN*SSC', 
   'BIP151-T':'BRN*GLO', # :'MUTF_CA:BIP151', this is how google is handling it https://finance.google.ca/finance?q=MUTF_CA:BIP151
   'FID281-T':'FSB*CAA', 
   'BNS744-T':'BNA*SAG',
   'BNS361-T':'BNS*MOR',
   'BNS741-T':'BNA*SIG',
   'BNS357-T':'BNS*MMF',
   'BMO146-T':'BOM*DIV', 
   'BMO471-T':'BME*TFP', 
   'GOC309-T':'Canoe Canadian Asset Allocation Class-Z'    # missing from stockwatch looks like stockwatch makes up their own names for Canadian mutual funds
   }
                       # Currency Exchange Rates to Canadian Dollars
   StockwatchIndexs = { # used for exchange rate update. used by updateDaylyStockwatch.py
   'AUD':'FX$AUD/CAD',  # Australia $  
   'BGN':'FX$BGN/CAD',  #? Bulgarian Lev     
   'BMD':'FX$BMD/CAD',  # Bermudian $     
   'BRL':'FX$BRL/CAD',  # Brazilian Real     
   'BSD':'FX$BSD/CAD',  # Bahamian $     
   'CHF':'FX$CHF/CAD',  # Swiss Franc   
   'CLP':'FX$CLP/CAD',  # Chilean Pesos   
   'CNH':'FX$CNY/CAD',  # Chinese YUAN Renminbi
   'CRC':'FX$CRC/CAD',  # Costa Rica Colon
   'DKK':'FX$DKK/CAD',  # Danish Krone
   'EGP':'FX$EGP/CAD',  # Egyption Pound
   'EUR':'FX$EUR/CAD',  # Euro 
   'FJD':'FX$FJD/CAD',  # Fijian Dollar 
   'GBP':'FX$GBP/CAD',  # British Pound    
   'HKD':'FX$HKD/CAD',  # Hong Kong $
   'IDR':'FX$IDR/CAD',  # Indonesian Rupiah
   'ILS':'FX$ILS/CAD',  # Israeli New Shekel
   'INR':'FX$INR/CAD',  # Indian Rupee
   'ISK':'FX$ISK/CAD',  # Icelandic Krona   
   'JMD':'FX$JMD/CAD',  # Jamaican Dollar   
   'JOD':'FX$JOD/CAD',  # Jordonian Dollar   
   'JPY':'FX$JPY/CAD',  # Japan YEN * 100 looks wrong but FX$CAD/JPY looks right
   'KPW':'FX$KPW/CAD',  # North Korean Won 
   'KRW':'FX$KRW/CAD',  # South Korean Won
   'LBP':'FX$LBP/CAD',  # Lebanese Pound 
   'MYR':'FX$MYR/CAD',  # Malaysian Ringgit 
   'MXN':'FX$MXN/CAD',  # Mexican Pesos 
   'NOK':'FX$NOK/CAD',  # Norwegian Kroner 
   'NZD':'FX$NZD/CAD',  # New Zealand $
   'PHP':'FX$PHP/CAD',  # Philippines Peso
   'PKR':'FX$PKR/CAD',  # Pakistani Rupee
   'RON':'FX$RON/CAD',  # Romanian Leu   
   'SAR':'FX$SAR/CAD',  # Saudi Arabian Riyal   
   'SDG':'FX$SDG/CAD',  # Sudan Pound   
   'SGD':'FX$SGD/CAD',  # Singapore Dollars      
   'SEK':'FX$SEK/CAD',  # Swedish Krona   
   'THB':'FX$THB/CAD',  # Thai Baht   
   'TRY':'FX$TRY/CAD',  # Turkish Lira 
   'TTD':'FX$TTD/CAD',  # Trinidad and Tobago Dollar  
   'TWD':'FX$TWD/CAD',  # Taiwan Dollars   
   'USD':'FX$USD/CAD',  # US $
   'VEF':'FX$VEF/CAD',  # Venezuelan Bolivar
   'ZAR':'FX$ZAR/CAD',  # South African RAND
   'ZMW':'FX$ZMW/CAD'   # Zambian Kwacha
     
   }


# the Yahoo financial interface is gone...
# but https://ca.finance.yahoo.com/quote/PKI.TO?p=PKI.TO&.tsrc=fin-srch may work to get quotes
# the interface moved to Alphavantage now .. Finding Canadian Mutual Funds on either of these databases (Yahoo or Alphavantage) is very difficult so this dictionary is no longer used.   
#   YahooSymbols = { 
#   'TML202':'F0CAN05OKY.TO',
#   'MFC738':'F0CAN05LW6.TO',
#   'BIP151':'F0CAN05NZE.TO', 
#   'FID281':'F0CAN05TEZ.TO', 
#   'BNS744':'F0CAN07204.TO',
#   'BNS361':'SCOTIAMORTGA.TO',
#   'BNS741':'F0CAN07205.TO',
#   'BNS357':'SCOTIAMONEYM.TO',
#   'BMO146':'BMODIVIDEND.TO', 
#   'BMO471':'F00000QVBL.TO', 
#   'GOC309':'Canoe Canadian Asset Allocation Class-Z'      # missing from Yahoo ,Alphavantage and Stockwatch. Globeinvestor has it.
#   }
 
   
#   tried to get quotes from these sites but they didn't work
#   https://web.tmxmoney.com/quote.php?qm_symbol=BR
#   https://web.tmxmoney.com/pricehistory.php?qm_symbol=BR
#   https://www.stockwatch.com/Quote/Detail.aspx?symbol=PKI&region=C   # this works ... not sure why it didn't work before . has date time and everything you need.
# http://www.quotemedia.com/portal/quote?qm_symbol=TML202%3ACA&searchBySymbol=symbol
# https://www.aequitasneo.com/en/single-security/MHYB                  this works if typed into the NEO exchange . looks like all the TSX symbols do
# NEO must be detecting my browser type
#    'MHYB-NEO':'https://www.aequitasneo.com/en/single-security/MHYB',   # failed
#    'MHYB-NEO':'https://www.aequitasneo.com/en/connect/fund-directory', # failed too NEO sucks
#   'MHYB-NEO':'https://www.theglobeandmail.com/investing/markets/stocks/MHYB-T/',    # failed globe and mail doesn't have NEO

# # MUTF:FPBFX this is what an american mutual fund looks like on google finance

# these Google queries still work Nov 22 2018  .. not the mutual funds or MHYB .. google seems to be getting out of Canadian Stock Markets..
# used by Stocks-fetchhtml-Google.py , Stock-html2csv-Google.py , Stock-update.py , Stock-up.py 
#   StockPriceHistoryGoogle = { 
#   'TML202':'https://finance.google.ca/finance?q=MUTF_CA:TML202',     # the canadian mutual fund data on Google is older than Globeinvestor 
#   'MFC738':'https://finance.google.ca/finance?q=MUTF_CA:MFC738',     # so should stick to GlobeInvestor or Stockwatch for Canadian Mutual Fund data
#   'BIP151':'https://finance.google.ca/finance?q=MUTF_CA:BIP151',     # the price and data info was in the html file but it was old
#   'FID281':'https://finance.google.ca/finance?q=MUTF_CA:FID281',     
#   'BNS744':'https://finance.google.ca/finance/historical?q=MUTF_CA:BNS744',  # had a nice table of values but was two days old.   
#   'BNS361':'https://finance.google.ca/finance?q=MUTF_CA:BNS361',     
#   'BNS741':'https://finance.google.ca/finance?q=MUTF_CA:BNS741',     
#   'BNS357':'https://finance.google.ca/finance?q=MUTF_CA:BNS357',     
#   'BMO471':'https://finance.google.ca/finance?q=MUTF_CA:BMO471',     
#   'GOC309':'https://finance.google.ca/finance?q=MUTF_CA:GOC309',        
#   'BR-T':'https://finance.google.ca/finance?q=TSE:BR',  # # Big Rock on TSX
#   'PKI-T':'https://finance.google.ca/finance?q=TSE:PKI',  # Parkland Fuel TSX
#   'MID-UN-T':'https://finance.google.ca/finance?q=TSE:MID-UN',  # Mint Income TSX
#   'GWO-PR-S-T':'https://finance.google.ca/finance?q=TSE:GWO-S', # Great West Life TSX
#   'CIQ-UN-T':'https://finance.google.ca/finance?q=TSE:CIQ-UN',  # Canadian Hi Income TSX
#   'CU-PR-F-T':'https://finance.google.ca/finance?q=TSE:CU-F',  # Canadian Utility TSX
#   'BPF-UN-T':'https://finance.google.ca/finance?q=TSE:BPF-UN', # Boston Pizza TSX
#   'RBN-UN-T':'https://finance.google.ca/finance?q=TSE:RBN-UN', # Blue Ribbon TSX
#   'KMB-N':'https://finance.google.ca/finance?q=NYSE:KMB' # Kimberly Clark on New York Exchange
#   }
   
   
   
   
# list below is used to get the current (real time) price of a stock from GlobeInvestor
# the date is now in the html page and the quote is in real time. 
# is hideing the historical data however /performance/ should have shown it.
# you can use your watchlist to find the stock tickers.
# was used by Stock-fetchhtml-Globe-Investor.py , Stock-html2csv-Globe-Investor.py to create Stock-Results.csv for Stock-update.py
# now only used by fetchhtml-Globe-Performance.py and txt2csv-Globe-Performance.py 
# this table controls how many symbols are pulled down from globe investor. each one has around 3 months of closing prices
# so a lot of data is generated . Libre Office Calc is started to give you an opportunity to trim the data before it is 
# fed to moneydance . make sure no historical screen is displayed in moneydance when you feed the data to moneydance. 
# above seems to be fixed in MD2019
# you can run uphst-Globe-Performance.py to import the data into moneydance.
# I don't use this anymore and consider it to be a backup to the stockwatch scripts.
# these scripts use the selenium.webdriver under python instead of jython making the screen scrapping very clean.

   StockPriceHistoryGlobeInvestor = { 
#   'BR-T':'https://www.theglobeandmail.com/investing/markets/stocks/BR-T/',  # Big Rock on TSX
#   'PKI-T':'https://www.theglobeandmail.com/investing/markets/stocks/PKI-T/',  # Parkland Fuel TSX
#   'VST-N':'https://www.theglobeandmail.com/investing/markets/stocks/VST-N/',   # Vista Energy
   'ALA-T':'https://www.theglobeandmail.com/investing/markets/stocks/ALA-T/',    # AltaGas Ltd
#   'MID-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/MID-UN-T/',  # Mint Income TSX
#   'GWO-PR-S-T':'https://www.theglobeandmail.com/investing/markets/stocks/GWO-PR-S-T/', # Great West Life TSX
#   'CIQ-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/CIQ-UN-T/',  # Canadian Hi Income TSX
#   'CU-PR-F-T':'https://www.theglobeandmail.com/investing/markets/stocks/CU-PR-F-T/',  # Canadian Utility TSX
#   'BPF-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/BPF-UN-T/', # Boston Pizza TSX
#   'RBN-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/RBN-UN-T/', # Blue Ribbon TSX
#   'KMB-N':'https://www.theglobeandmail.com/investing/markets/stocks/KMB-N/', # Kimberly Clark on New York Exchange
#   'BNE-T':'https://www.theglobeandmail.com/investing/markets/stocks/BNE-T/',
#   'DR-T':'https://www.theglobeandmail.com/investing/markets/stocks/DR-T/',
#   'EIT-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/EIT-UN-T/',
#   'FCD-UN-X':'https://www.theglobeandmail.com/investing/markets/stocks/FCD-UN-X/',
#   'FFI-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/FFI-UN-T/',
#   'FIG-T':'https://www.theglobeandmail.com/investing/markets/stocks/FIG-T/',
#   'HHL-T':'https://www.theglobeandmail.com/investing/markets/stocks/HHL-T/',
#   'IDR-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/IDR-UN-T/',
#   'INC-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/INC-UN-T/',
#   'JE-T':'https://www.theglobeandmail.com/investing/markets/stocks/JE-T/',
#   'KWH-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/KWH-UN-T/',
#   'MFR-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/MFR-UN-T/',
#   'MFT-T':'https://www.theglobeandmail.com/investing/markets/stocks/MFT-T/',
#   'MHYB-NEO':'https://www.theglobeandmail.com/investing/markets/stocks/MHYB-NE/',    # globe and mail has NEO too NE is the NEO exchange.
#   'MID-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/MID-UN-T/',
#   'MUB-T':'https://www.theglobeandmail.com/investing/markets/stocks/MUB-T/',
#   'PGI-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/PGI-UN-T/',
#   'UTE-UN-T':'https://www.theglobeandmail.com/investing/markets/stocks/UTE-UN-T/',
#   'TML202-T': 'https://www.theglobeandmail.com/investing/markets/funds/TML202.CF/',   # mutual funds work too
#   'MFC738-T': 'https://www.theglobeandmail.com/investing/markets/funds/MFC738.CF/',
#   'BIP151-T': 'https://www.theglobeandmail.com/investing/markets/funds/BIP151.CF/',
#   'FID281-T': 'https://www.theglobeandmail.com/investing/markets/funds/FID281.CF/',
#   'BMO471-T': 'https://www.theglobeandmail.com/investing/markets/funds/BMO471.CF/',
#   'GOC309-T': 'https://www.theglobeandmail.com/investing/markets/funds/GOC309.CF/',
#   'BNS344-T': 'https://www.theglobeandmail.com/investing/markets/funds/BNS344.CF/'    
   }
   
# I've switched  to stockwatch it does NEO and has date/time. 
# Does Canadian Mutual Funds and Stocks. Has USA stocks and funds too. 
# also has international currency/exchange rates.
# used by updateDaylyStockwatch.py and Stock-fetchhtml-Stockwatch.py 

   StockPriceHistoryStockwatch = { 
   'TML202':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BIF*CDN&region=C',
   'MFC738':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CUN*SSC&region=C',
   'BIP151':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BRN*GLO&region=C',
   'FID281':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FSB*CAA&region=C', 
   'BNS744':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNA*SAG&region=C',
   'BNS361':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNS*MOR&region=C',
   'BNS741':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNA*SIG&region=C',
   'BNS357':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNS*MMF&region=C',
   'BMO146':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BOM*DIV&region=C', 
   'BMO471':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BME*TFP&region=C', # ...............................end of the mutual funds
   'AI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AI&region=C',     
   'ARX-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ARX&region=C',
   'ABX-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ABX&region=C', # Barrick Gold    
   'AD-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AD&region=C',
   'ALA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ALA&region=C', # AltaGas Ltd
   'APR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=APR.UN&region=C', 
   'AW-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AW.UN&region=C', 
   'AX-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=AX.UN&region=C', 
   'BR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BR&region=C', # Big Rock on TSX
   'BTB-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BTB.UN&region=C', # Big Rock on TSX
   'BNE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BNE&region=C',   
   'BPF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=BPF.UN&region=C', # Boston Pizza TSX   
   'CCO-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CCO&region=C', # cameco
   'CHP-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CHP.UN&region=C', # choice REIT   
   'CRR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CRR.UN&region=C', # cameco
   'CNR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CNR&region=C',
   'CIQ-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CIQ.UN&region=C',  # Canadian Hi Income TSX
   'CJR-B-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CJR.B&region=C',  # Corus   
   'CU-PR-F-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=CU.PR.F&region=C',  # Canadian Utility TSX
   'DS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=DS&region=C', # Quadvest div select corp   
   'DR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=DR&region=C',
   'EIT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EIT.UN&region=C', # Canoe ETF
   'EIF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EIF&region=C', # Exchange Income Corp
   'ENB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ENB&region=C', # Enbridge
#   'ENF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ENF&region=C', # Enbridge Fund was ENF.UN now ENB
   'EXE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=EXE.UN&region=C', # Extendicare
   'FC-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FC&region=C',      # Firm Capital Mortgage Investment Corp 
   'FCD-UN-X':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FCD.UN&region=C', # Firm Capital Property Trust its on the venture exchange ?
   'FFN-PR-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FFN.PR.A&region=C',
   'FFI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FFI.UN&region=C',
   'FTN-PR-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FTN.PR.A&region=C',
   'FN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FN&region=C',   
   'FIG-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FIG&region=C',
   'FTS-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FTS&region=C',   
   'GDG-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=GDG.UN&region=C', 
   'G-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=G&region=C', # goldcorp
   'GWO-PR-S-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=GWO.PR.S&region=C', # Great West Life TSX   
   'HR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=HR.UN&region=C', # Hydro One
   'H-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=H&region=C', # Hydro One
   'HHL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=HHL&region=C',
#   'IDR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=IDR.UN&region=C',
   'IDR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=IDR.UN&region=C',
   'IPL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=IPL&region=C',
   'INC-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=INC.UN&region=C',
   'JE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=JE&region=C',
   'K-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=K&region=C', # Kinross
   'KEG-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KEG.UN&region=C',
   'KMB-N':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KMB&region=U', # Kimberly Clark on New York Exchange
   'KWH-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=KWH.UN&region=C',
   'LFE-PR-B-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=LFE.PR.B&region=C',   
   'MFR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MFR.UN&region=C',
   'MFT-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MFT&region=C',
   'MHYB-NEO':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MHYB&region=C',  
   'MID-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MID.UN&region=C',  # Mint Income TSX
   'MUB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MUB&region=C',
   'MR-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MR.UN&region=C',      
   'MRT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MRT.UN&region=C',   
   'MMP-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=MMP.UN&region=C',
   'NPF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=NPF.UN&region=C',
   'NWH-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=NWH.UN&region=C',
   'PEY-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PEY&region=C',   
   'PCD-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PCD.UN&region=C',   
   'PGI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PGI.UN&region=C',
   'PKI-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PKI&region=C',  # Parkland Fuel TSX
   'PLZ-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PLZ.UN&region=C',
   'PPL-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PPL&region=C',
   'PR-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PR&region=C',   
   'PGF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=PGF&region=C',
   'RBN-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=RBN.UN&region=C', # Blue Ribbon TSX     
   'REI-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=REI.UN&region=C',   
#   'REF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=REF.UN&region=C',   Canadian REIT now CHP.UN
   'RIT-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=RIT&region=C',   
   'SCW-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SCW.UN&region=C',
   'SIN-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SIN.UN&region=C',
   'SJR-B-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SJR.B&region=C',
   'SKG-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SKG.UN&region=C',   
   'SPB-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SPB&region=C',   
   'S-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=S&region=C', # Sherrit
   'SRU-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SRU.UN&region=C',
   'SRV-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SRV.UN&region=C',
   'SSF-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SSF.UN&region=C',
   'SU-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=SU&region=C', # Sun core
   'TECK-A-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TECK.A&region=C', # Teck
   'T-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=T&region=C', # Telus
   'TNT-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TNT.UN&region=C', # Telus
   'TF-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TF&region=C', #Timber creek Financial
   'TA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=TA&region=C', # TransAlta
   'UTE-UN-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=UTE.UN&region=C',
   'VET-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=VET&region=C', # Vermillion
   'VST-N':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=VST&region=N', # Vista Energy
   'WJA-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=WJA&region=C', # West Jet
   'ZWE-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ZWE&region=C',
   'ZWU-T':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=ZWU&region=C',
   'AUD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$AUD/CAD&region=U', # exchange rates start here ..only used as a filter to indicate which rate we're interested in
#   'BGN':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BGN/CAD&region=U', 
#   'BMD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BMD/CAD&region=U', 
#   'BRL':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BRL/CAD&region=U', 
#   'BSD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$BSD/CAD&region=U', 
#   'CHF':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CHF/CAD&region=U',     
#   'CLP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CLP/CAD&region=U',     
#   'CNH':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CNH/CAD&region=U',   
#   'CRC':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$CRC/CAD&region=U',   
#   'DKK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$DKK/CAD&region=U',   
#   'EGP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$EGP/CAD&region=U',   
   'EUR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$EUR/CAD&region=U',
#   'FJD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$FJD/CAD&region=U',
   'GBP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$GBP/CAD&region=U', 
#   'HKD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$HKD/CAD&region=U',   
#   'IDR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$IDR/CAD&region=U',   
#   'ILS':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ILS/CAD&region=U',   
#   'INR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$INR/CAD&region=U',   
#   'ISK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ISK/CAD&region=U',   
#   'JMD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$JMD/CAD&region=U', 
#   'JOD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$JOD/CAD&region=U', 
#   'JPY':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$JPY/CAD&region=U', 
#   'KPW':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$KPW/CAD&region=U', 
#   'KRW':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$KRW/CAD&region=U', 
#   'LBP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$LBP/CAD&region=U', 
#   'MYR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$MYR/CAD&region=U', 
#   'MXN':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$MXN/CAD&region=U',    
#   'NOK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$NOK/CAD&region=U',      
#   'NZD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$NZD/CAD&region=U',   
#   'PHP':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$PHP/CAD&region=U',   
#   'PKR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$PKR/CAD&region=U',   
#   'RON':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$RON/CAD&region=U',      
#   'SAR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SAR/CAD&region=U',
#   'SDG':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SDG/CAD&region=U',
#   'SGD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SGD/CAD&region=U',   
#   'SEK':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$SEK/CAD&region=U',
#   'THB':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$THB/CAD&region=U',
#   'TRY':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$TRY/CAD&region=U',
#   'TTD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$TTD/CAD&region=U',
#   'TWD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$TWD/CAD&region=U',
   'USD':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$USD/CAD&region=U',
#   'VEF':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$VEF/CAD&region=U',   
#   'ZAR':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ZAR/CAD&region=U',
   'ZMW':'https://www.stockwatch.com/Quote/Detail.aspx?symbol=FX$ZMW/CAD&region=U'
     
   }
   
 # fetch Alphavantage historical prices using the API
 # this table basily converts the Alphavantage Symbol to what is being used in moneydance.
 # it also defines which symbols to fetch because we own them or are just interested in tracking them.
 # used by stock-fetchhtmal-Alphavantage.py
 # I don't use Alphavantage anymore ... was inconsistent on Canadian stocks and Canadian Mutual funds 
   StockPriceHistoryAlphavantage = { 
   'AD-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:AD&apikey=01833J9F7164BSUN&datatype=csv',
   'ALA-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:ALA&apikey=01833J9F7164BSUN&datatype=csv', 
   'BR-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:BR&apikey=01833J9F7164BSUN&datatype=csv', # Big Rock on TSX
   'PKI-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:PKI&apikey=01833J9F7164BSUN&datatype=csv',  # Parkland Fuel TSX
   'MID-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:MID-UN&apikey=01833J9F7164BSUN&datatype=csv',  # Mint Income TSX
   'GWO-PR-S-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:GWO-PS&apikey=01833J9F7164BSUN&datatype=csv', # Great West Life TSX
   'CIQ-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:CIQ-UN&apikey=01833J9F7164BSUN&datatype=csv',  # Canadian Hi Income TSX
   'CU-PR-F-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:CU-PF&apikey=01833J9F7164BSUN&datatype=csv',  # Canadian Utility TSX
   'BPF-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:BPF-UN&apikey=01833J9F7164BSUN&datatype=csv', # Boston Pizza TSX
   'RBN-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:RBN-UN&apikey=01833J9F7164BSUN&datatype=csv', # Blue Ribbon TSX
   'KMB-N':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NYSE:KMB&apikey=01833J9F7164BSUN&datatype=csv', # Kimberly Clark on New York Exchange
   'BNE-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:BNE&apikey=01833J9F7164BSUN&datatype=csv',
   'DR-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:DR&apikey=01833J9F7164BSUN&datatype=csv',
   'EIT-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:EIT-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'FCD-UN-X':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=FCD-UN.V&apikey=01833J9F7164BSUN&datatype=csv', # its on the venture exchange ?
   'FFI-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:FFI-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'FIG-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:FIG&apikey=01833J9F7164BSUN&datatype=csv',
   'HHL-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:HHL&apikey=01833J9F7164BSUN&datatype=csv',
   'IDR-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:IDR-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'INC-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:INC-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'JE-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:JE&apikey=01833J9F7164BSUN&datatype=csv',
   'KWH-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:KWH-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'MFR-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:MFR-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'MFT-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:MFT&apikey=01833J9F7164BSUN&datatype=csv',
 #  'MHYB-NEO':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:MHYB&apikey=01833J9F7164BSUN&datatype=csv', # trouble not on Alphavantage
   'MID-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:MID-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'MUB-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:MUB&apikey=01833J9F7164BSUN&datatype=csv',
   'PGI-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:PGI-UN&apikey=01833J9F7164BSUN&datatype=csv',
   'UTE-UN-T':'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSX:UTE-UN&apikey=01833J9F7164BSUN&datatype=csv'
     
   }  
   
# used by Stock-fetchhtml-Bloomberg.py   
#   StockQuoteBloomberg = { 
#   'Test-T':'https://www.aequitasneo.com/en/single-security/PKI', 
#   'AD-T':'https://www.bloomberg.com/quote/AD:CN',
#   'ALA-T':'https://www.bloomberg.com/quote/ALA:CN', 
#   'BR-T':'https://www.bloomberg.com/quote/BR:CN',            # Big Rock on TSX
#   'PKI-T':'https://www.bloomberg.com/quote/PKI:CN',          # Parkland Fuel TSX
#   'MID-UN-T':'https://www.bloomberg.com/quote/MID-U:CN',     # Mint Income TSX
#   'GWO-PR-S-T':'https://www.bloomberg.com/quote/GWO-PS:CN',  # Great West Life TSX      .....Missing
#   'CIQ-UN-T':'https://www.bloomberg.com/quote/CIQ-U:CN',     # Canadian Hi Income TSX
#   'CU-PR-F-T':'https://www.bloomberg.com/quote/CU-PF:CN',    # Canadian Utility TSX  ........Missing
#   'BPF-UN-T':'https://www.bloomberg.com/quote/BPF-U:CN',     # Boston Pizza TSX
#   'RBN-UN-T':'https://www.bloomberg.com/quote/RBN-U:CN',     # Blue Ribbon TSX
#   'KMB-N':'https://www.bloomberg.com/quote/KMB:US',             # Kimberly Clark on New York Exchange
#   'BNE-T':'https://www.bloomberg.com/quote/BNE:CN',
#   'DR-T':'https://www.bloomberg.com/quote/DR:CN',
#   'EIT-UN-T':'https://www.bloomberg.com/quote/EIT-U:CN',
#   'FCD-UN-X':'https://www.bloomberg.com/quote/FCD-U:CN', # its on the venture exchange ?
#   'FFI-UN-T':'https://www.bloomberg.com/quote/FFI-U:CN',
#   'FIG-T':'https://www.bloomberg.com/quote/FIG:CN',
#   'HHL-T':'https://www.bloomberg.com/quote/HHL:CN',
#   'IDR-UN-T':'https://www.bloomberg.com/quote/IDR-U:CN',
#   'INC-UN-T':'https://www.bloomberg.com/quote/INC-U:CN',
#   'JE-T':'https://www.bloomberg.com/quote/JE:CN',
#   'KWH-UN-T':'https://www.bloomberg.com/quote/KWH-U:CN',
#   'MFR-UN-T':'https://www.bloomberg.com/quote/MFR-U:CN',
#   'MFT-T':'https://www.bloomberg.com/quote/MFT:CN',
#   'MHYB-NEO':'https://www.bloomberg.com/quote/MHYB:CN',
#   'MID-UN-T':'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending', # header test
#   'MID-UN-T':'https://manytools.org/http-html-text/http-request-headers/',                     # header test
#   'MUB-T':'https://www.bloomberg.com/quote/MUB:CN',
#   'PGI-UN-T':'https://www.bloomberg.com/quote/PGI-U:CN',
#   'UTE-UN-T':'https://www.bloomberg.com/quote/UTE-U:CN'
#     
#   }  
