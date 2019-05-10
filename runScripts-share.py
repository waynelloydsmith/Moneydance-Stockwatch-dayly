#!/usr/bin/env python
# this script is auto started when the consoles jconsole270 or jython270 startup.
# if you change the name of an Investment Account you need to update this script in two places...


class runScripts:  

  import sys
  #from javax.swing import *
  #from java.awt import *
  from javax.swing.tree import DefaultMutableTreeNode
###  from com.moneydance.apps.md.model import AbstractTxn
###  from com.moneydance.apps.md.model import ParentTxn
###  from com.moneydance.apps.md.model import SplitTxn
  from com.infinitekind.moneydance.model import AbstractTxn
  from com.infinitekind.moneydance.model import ParentTxn
  from com.infinitekind.moneydance.model import SplitTxn

  from javax.swing import Timer
  from java.awt.event import ActionListener
  from javax.swing import JFrame
  from java.awt import BorderLayout
  from javax.swing import JTree
  from javax.swing import JScrollPane
  from java.awt import Dimension
  from javax.swing import JPanel
  from javax.swing import JButton
  from javax.swing import JLabel
  from javax.swing import WindowConstants
      
  accountName = None # used by Scotia-Inv-new.py and BMO-Inv-new.py
#  runScriptFile = ""
  infile = ""          # was used by Scotia-Inv-new.py and BMO-Inv-new.py .. now just use the bank default csv file names
 
  class WindowClose(ActionListener):
    def __init__(self):
        from javax.swing import Timer
        self.timer = Timer(5000, self)
        self.timer.start()
    def actionPerformed(self, e):
        self.timer.stop()
        mframe.dispose()  
  
  def showMessage (self,message) : 
    #  mframe = JFrame("Message")
    global mframe
    mframe = self.JFrame(message)
#    mframe.setSize(1000, 100)
    mframe.setSize(1000, 50)
    mframe.setDefaultCloseOperation(self.WindowConstants.DISPOSE_ON_CLOSE)
    mpnl = self.JPanel()
    mframe.add(mpnl)
    mlabel = self.JLabel(str(message))
    mpnl.add(mlabel)
    mframe.setVisible(True)
    self.WindowClose()


  def addLevel2Items(self,branch, branchData=None):
    '''  add data to tree branch
         requires branch and data to add to branch
    '''
    # this does not check to see if its a valid branch
    if branchData == None:
        branch.add(DefaultMutableTreeNode('No valid data'))
    else:
        for item in branchData:
          # add the data from the specified list to the branch
          branch.add(self.DefaultMutableTreeNode(item))

  def ItemSelect(self, event):
    import sys
    selected = self.tree.getLastSelectedPathComponent()
    if selected == None:
      xlabel.text = 'No script selected'
#      accountName = "none"
    else:
      self.xlabel.text = str(selected)
      print "Selected ", selected

#      if str(selected).count("Update Canadian Mutual Fund Prices Globe-Investor up.py"): 
#          mess = "Running Script "+ str(selected)
#          self.showMessage(mess)
#	  execfile("/opt/moneydance/scripts/up.py")
#      if str(selected).count("Import TMX portfolio csv file updateTMX.py"): 
#          mess = "Running Script "+ str(selected)
#          self.showMessage(mess)        
#	  execfile("/opt/moneydance/scripts/updateTMX.py")
#      if str(selected).count("Update Canadian Mutual Fund Price History Globe-Investor uphst.py"): 
#          mess = "Running Script "+ str(selected)
#          self.showMessage(mess)        
#	  execfile("/opt/moneydance/scripts/uphst.py") # the old Globe Mutual Fund tables
#      elif str(selected).count("Update Stock Prices Stock-up-Google.py"): 
#          mess = "Running Script "+ str(selected)
#          self.showMessage(mess)        
#	  execfile("/opt/moneydance/scripts/Stock-up-Google.py")  
#      elif str(selected).count("Update Stock Prices Stock-up-Globe-Investor.py"): 
#          mess = "Running Script "+ str(selected)
#          self.showMessage(mess)        
#	  execfile("/opt/moneydance/scripts/Stock-up-Globe-Investor.py")  	  
      if str(selected).count("Uphst-Globe-Performance.py"): 
          mess = "Running Script "+ str(selected)
          self.showMessage(mess)        
	  execfile("/opt/moneydance/scripts/uphst-Globe-Performance.py")  	  	  
      elif str(selected).count("Update Stock Prices Stock-up-Stockwatch.py"): 
          mess = "Running Script "+ str(selected)
          self.showMessage(mess)        
	  execfile("/opt/moneydance/scripts/Stock-up-Stockwatch.py")  	  	  
      elif str(selected).count("Misc Scripts"): 
          mess = "Error Please Select a Misc Script From the Dropdown list"
          self.showMessage(mess)   
      elif str(selected).count("Run Stockwatch Update Scripts"): 
          mess = "Error Please Select an Update Script From the Dropdown list"
          self.showMessage(mess)
      elif str(selected).count('Import History from Alphavantage Stock-up-Alphavantage.py'): 
          mess = "Running Script "+ str(selected)
          self.showMessage(mess)        
	  execfile("/opt/moneydance/scripts/Stock-up-Alphavantage.py")  	  	      
      elif str(selected).count('/opt/moneydance/scripts/updateHistoryStockwatch.py'): 
          mess = 'updateHistoryStockwatch.py Can Take a Long Time to Finish 6 minutes per Symbol'
          self.showMessage(mess)        
	  execfile(str(selected))  	  	      
      elif str(selected).count('Import ~/ScotiaBank/transactionHistory.csv to selected Investment Account'): 
          mess = "Error Please Select an Account From the Dropdown list"          
          self.showMessage(mess)          	      
#      elif str(selected).count('Import ~/BMO/TransactionHistory.csv to selected Investment Account'): 
#          mess = "Error Please Select an Account From the Dropdown list"
#          self.showMessage(mess)
#      elif str(selected).count('BMO RRSP TEST'): 
#          mess = "Updating Account "+ str(selected)
#          self.showMessage(mess)  
#          sys.argv = ['','runScripts',str(selected)]  #####
#	  execfile("/opt/moneydance/scripts/BMO-Inv-new.py")  	  	      
#      elif str(selected).count('BMO RRSP 2947'): 
#          mess = "Updating Account "+ str(selected)
#          self.showMessage(mess)  
#          sys.argv = ['','runScripts',str(selected)]
#	  execfile("/opt/moneydance/scripts/BMO-Inv-new.py")  
      elif str(selected).count('Scotia RRSP TEST'): 
          mess = "Updating Account "+ str(selected)
          self.showMessage(mess)  
          sys.argv = ['','runScripts','BMO RRSP TEST']
	  execfile("/opt/moneydance/scripts/Scotia-Inv-new.py")  
      elif str(selected).count('Scotia Rita Inv xxxx') or str(selected).count('Wayne TFSA xxxx') or str(selected).count('M&B RRSP xxxx'): 
          mess = "Updating Account "+ str(selected)
          self.showMessage(mess)  
          sys.argv = ['','runScripts',str(selected)]
	  execfile("/opt/moneydance/scripts/Scotia-Inv-new.py")  	  
      elif str(selected).count('Rita TFSA xxxx') or str(selected).count('Scotia Rita RRSP xxxx') or str(selected).count('Scotia LIF'): 
          mess = "Updating Account "+ str(selected)
          self.showMessage(mess)  
          sys.argv = ['','runScripts',str(selected)]
	  execfile("/opt/moneydance/scripts/Scotia-Inv-new.py") 
	  
      else:	   
          execfile(str(selected))
#          accountName = "none"
          
          "/opt/moneydance/scripts/updateHistoryStockwatch.py"
          
  def __init__(self):
      
    import sys
    
    from javax.swing import JEditorPane
    from javax.swing import JFrame
    from javax.swing import JPanel
    from javax.swing import JScrollPane
    from javax.swing import JSplitPane

    from java.awt import Color
    from javax.swing import ImageIcon
    from javax.swing.tree import DefaultTreeCellRenderer
    from javax.swing import JTree
    from javax.swing.tree import DefaultMutableTreeNode
    from javax.swing.tree import TreeSelectionModel
    from javax.swing.event import TreeSelectionEvent
    from javax.swing.event import TreeSelectionListener
    from javax.swing.plaf.metal import MetalIconFactory
#    from javax.swing import UIManager
#    from javax.swing.plaf.metal import MetalLookAndFeel
#    from javax.swing.plaf.metal import OceanTheme
#    from javax.swing.plaf.metal import DefaultMetalTheme
#    from com.sun.java.swing.plaf.gtk import GTKLookAndFeel
#    from com.sun.java.swing.plaf.motif import MotifLookAndFeel
#    from com.sun.java.swing.plaf.windows import WindowsLookAndFeel 
#    from javax.swing.plaf.nimbus import NimbusLookAndFeel
#    from javax.swing.plaf.multi import MultiLookAndFeel

    execfile("/opt/moneydance/scripts/definitions.py")
 
# the list of Misc Scripts test.py and dev.py are just for playing with dev.py has the testing for the Alphavantage yahoo replacement
    mMiscData = ["StockGlance75.py","jython_info.py" ,"test.py","dev.py"]
# these scripts process csv files downloaded from www.stockwatch.com and placed in /opt/moneydance/tmp/Stockwatch(years history for one symbol at a time) or StockwatchDay(all the days closing prices for that exchange)    
    sStockwatchData = ["updateDaylyStockwatch.py" ,"updateHistoryStockwatch.py","updatePortfolioStockwatch.py"]    
# THESE ARE THE SCRIPTS USED TO FETCH THE DAYS canadian MUTUAL FUNDS PRICES from the globeinvestor website                  
#    upPyData = ["/opt/moneydance/scripts/fetchhtml.py","/opt/moneydance/scripts/html2csv.py","/opt/moneydance/scripts/update.py"]     
# THESE ARE THE SCRIPTS USED TO FETCH A MONTHS WORTH OF Canadian MUTUAL FUND PRICES from the globeinvestor website   
#    uphstPyData = ["/opt/moneydance/scripts/fetchhtmlHistory.py","/opt/moneydance/scripts/html2txt.py","/opt/moneydance/scripts/html2csvHistory.py","/opt/moneydance/scripts/reversecsv.py","/opt/moneydance/scripts/updateHistory.py"]
# theses scripts scrape the current stock quote off the globeinvestor website or the google finance web site or the stockwatch web site    
#    upStockPyDataGoogle = ["/opt/moneydance/scripts/Stock-fetchhtml-Google.py","/opt/moneydance/scripts/Stock-html2csv-Google.py","/opt/moneydance/scripts/Stock-update.py"]
#    upStockPyDataGlobe = ["/opt/moneydance/scripts/Stock-fetchhtml-Globe-Investor.py","/opt/moneydance/scripts/Stock-html2csv-Globe-Investor.py","/opt/moneydance/scripts/Stock-update-Globe-Investor.py"]
    upStockPyDataGlobePerformance = ["fetchhtml-Globe-Performance.py","txt2csv-Globe-Performance.py","reversecsv-Globe-Perf.py","updateHistory-Globe-Performance.py","uphst-Globe-Performance-Help.py"] 
    upStockPyDataStockwatch = ["Stock-fetchhtml-Stockwatch.py","Stock-html2csv-Stockwatch.py","Stock-update-Stockwatch.py"]
# this script processes csv files created using a portfolio on wwww.TMX.com and placed in /opt/moneydance/tmp/TMX 
#    upTMXPyData = ["/opt/moneydance/scripts/updateTMX.py"]
# these scripts pull historical closing prices down from Alphavantage and put them in /scripts/tmp/Alphavantage and then load them into moneydance    
# to monitor progress check the number of files in /opt/moneydance/scripts/tmp/Alphavantage
    upAlphavantagePyData = ["Stock-fetchhtml-Alphavantage.py","updateHistoryAlphavantage.py"]
# this script reads a csv file placed in /home/wayne/Scotia/ and puts the transactions in a selected Investment Account  
    upScotiaInvestmentPyData = ["Scotia RRSP TEST",'Scotia Rita Inv xxxx','Wayne TFSA xxxx','M&B RRSP xxxx','Rita TFSA xxxx','Scotia Rita RRSP xxxx','Scotia LIF'] 
# this script reads a csv file placed in /home/wayne/BMO/ and puts the transactions in a selected Investment Account  
#    upBMOInvestmentPyData = ["BMO RRSP TEST","BMO RRSP 2947"] 

#    ALL of these UIManager calls caused changes in the Moneydance GUI too . so not a good idea to use them
#    UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName()) #worked great "Metal" has two flavors
#    MetalLookAndFeel.setCurrentTheme(OceanTheme())    both look the same
#    MetalLookAndFeel.setCurrentTheme(DefaultMetalTheme())
#    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName()) #worked great looks same as above
#    UIManager.setLookAndFeel("com.sun.java.swing.plaf.motif.MotifLookAndFeel") #worked great looks dark with + 
#    UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel") #this is what I was already running
#    UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel") # I like this one but it messes with moneydance too
#    UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel") # same as above
#    UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel") # not supported on this platform
#    UIManager.setLookAndFeel("javax.swing.plaf.multi.MultiLookAndFeel") # needs more code
    
    xframe = self.JFrame("runScripts.py")
#    xframe.setSize(500, 350)
    xframe.setSize(800, 350)
    xframe.setLayout(self.BorderLayout())

    # add level 0 item
    treeRoot = self.DefaultMutableTreeNode('Jython Scripts')
    
    mMisc = self.DefaultMutableTreeNode('Misc Scripts')
    sStockwatch = self.DefaultMutableTreeNode('Run Stockwatch Update Scripts')
#    upPy = self.DefaultMutableTreeNode('Update Canadian Mutual Fund Prices Globe-Investor up.py')
#    uphstPy = self.DefaultMutableTreeNode('Update Canadian Mutual Fund Price History Globe-Investor uphst.py')
#    upStockPyGoogle = self.DefaultMutableTreeNode('Update Stock Prices Stock-up-Google.py')
#    upStockPyGlobe = self.DefaultMutableTreeNode('Update Stock Prices Stock-up-Globe-Investor.py')
    upStockPyGlobePerformance = self.DefaultMutableTreeNode('uphst-Globe-Performance.py')
    
    upStockPyStockwatch = self.DefaultMutableTreeNode('Update Stock Prices Stock-up-Stockwatch.py')
#    upTMXPy = self.DefaultMutableTreeNode('Import TMX portfolio csv file updateTMX.py')
    upAlphavantagePy = self.DefaultMutableTreeNode('Import History from Alphavantage Stock-up-Alphavantage.py')
    upScotiaInvestmentPy = self.DefaultMutableTreeNode('Import ~/ScotiaBank/transactionHistory.csv to selected Investment Account')
#    upBMOInvestmentPy = self.DefaultMutableTreeNode('Import ~/BMO/TransactionHistory.csv to selected Investment Account')
    
    
    
    # add the level 1 items
    treeRoot.add(mMisc)
    treeRoot.add(sStockwatch)
#    treeRoot.add(upPy)
#    treeRoot.add(uphstPy) # old Glode tables
#    treeRoot.add(upStockPyGoogle)
#    treeRoot.add(upStockPyGlobe) 
    treeRoot.add(upStockPyGlobePerformance)
    treeRoot.add(upStockPyStockwatch)     
#    treeRoot.add(upTMXPy)
    treeRoot.add(upAlphavantagePy)
    treeRoot.add(upScotiaInvestmentPy)
#    treeRoot.add(upBMOInvestmentPy)

    #add the level 2 items to level 1
    self.addLevel2Items(mMisc, mMiscData)
    self.addLevel2Items(sStockwatch, sStockwatchData)
#    self.addLevel2Items(upPy, upPyData)
#    self.addLevel2Items(uphstPy, uphstPyData)
#    self.addLevel2Items(upStockPyGoogle, upStockPyDataGoogle)
#    self.addLevel2Items(upStockPyGlobe, upStockPyDataGlobe)
    self.addLevel2Items(upStockPyGlobePerformance, upStockPyDataGlobePerformance)
    self.addLevel2Items(upStockPyStockwatch, upStockPyDataStockwatch)    
#    self.addLevel2Items(upTMXPy, upTMXPyData)
    self.addLevel2Items(upAlphavantagePy, upAlphavantagePyData)
    self.addLevel2Items(upScotiaInvestmentPy, upScotiaInvestmentPyData)
#    self.addLevel2Items(upBMOInvestmentPy, upBMOInvestmentPyData)
    
    #build the tree
    self.tree = self.JTree(treeRoot)

#    leafIcon = ImageIcon(sys.registry["user.home"]+"/moneydance/scripts/image/new_document-24x24.png")
    leafIcon = MetalIconFactory.getTreeLeafIcon()    
#    openIcon = ImageIcon(sys.registry["user.home"]+"/moneydance/scripts/image/folder-open-32x32.png")
    openIcon = MetalIconFactory.getFileChooserNewFolderIcon()
#    closedIcon = ImageIcon(sys.registry["user.home"]+"/moneydance/scripts/image/folder-closed-32x32.png")
    closedIcon = MetalIconFactory.getTreeFolderIcon()

    renderer = DefaultTreeCellRenderer()
    renderer.setLeafIcon(leafIcon)
    renderer.setOpenIcon(openIcon)
    renderer.setClosedIcon(closedIcon)
    self.tree.setCellRenderer(renderer)
   
        
    scrollPane = self.JScrollPane()  # add a scrollbar to the viewport
    scrollPane.setPreferredSize(self.Dimension(700,250))
    scrollPane.getViewport().setView(self.tree)

    xpanel = self.JPanel()
    xpanel.add(scrollPane)
    xframe.add(xpanel, self.BorderLayout.CENTER)

    btn = self.JButton('Run Script', actionPerformed = self.ItemSelect)
    xframe.add(btn,self.BorderLayout.SOUTH)
    self.xlabel = self.JLabel('Select Script')
    xframe.add(self.xlabel, self.BorderLayout.NORTH)
    xframe.setDefaultCloseOperation(self.WindowConstants.DISPOSE_ON_CLOSE)
    xframe.setVisible(True)
    #print "stdout1",sys.stdout
    self.addLevel2Items # initalize the addLevel2Items function
    #print "stdout2",sys.stdout

if __name__ == '__main__':
  runScripts()
  
