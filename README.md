# Moneydance-Stockwatch-dayly
Pulls the end of day Canadian/US stock prices from Stockwatch and updates Moneydance. 
does canadian mutual fund and exchange rates too. 
You need to be logged into stockwatch and have an account with them. 
# description of each script.
  runScripts-shared.py .. run this script with moneydance->window->"Show MoneyBot Console"
  It runs many scripts via a tree menu system.
  open the "Run Stockwatch Update Scripts" folder.
  select updateDaylyStockWatch.py.
  hit the "Run Script Button" at the bottom.
  scripts will run in this order.
updateDaylyStockWatch.py -- runs the fetch scripts and processes the results.
fetchhtmlDaylyStockwatch.py -- gets the csv file from stockwatch with all the closing prices by exchange.
fetch-Stockwatch-ID.py  -- uses python and sqlite to get the stockwatch cookie with user ID in it.(stockwatchID.txt)
fetchhtmlDaylyStockwatchIndexs.py  --- gets the exchange rates for all the currencies
fetch-Stockwatch-ID.py -- uses python and sqlite to get the stockwatch cookie with ID in it. 
finish up back in updateDaylyStockWatch.py -- process all the csv files in StockwatchDay and move them to Done.
directories in use (you need to create these manually)
/opt/moneydance/scripts/tmp/StockwatchDay.
/opt/moneydance/scripts/tmp/Done.
files in use 
/opt/moneydance/scripts/tmp/stockwatchID.txt
/opt/moneydance/scripts/tmp/StockwatchDay/indexs.csv
/opt/moneydance/scripts/tmp/StockwatchDay/stoclwatch.csv
Progress in reported on the "MoneyBot Conosle"
also check the Message Console for Errors / Crashes.
definitions.py is used to filter the large amount of data provided by www.stockwatch.com
so that only securities and exchange rates we are interested in get saved in moneydance.
you will need to edit this file to reflect the stocks / currencies you are interested in.
the dictionary to change is StockPriceHistoryStockwatch = { 
Run this script every day after the markets close (30 minutes later).
It only takes a 30 seconds to run it.

