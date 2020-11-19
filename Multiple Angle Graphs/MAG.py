###############
# This is the main program with GUI using PyQt5 with QT Designer.
# It uses mulitple files which are all listed below (includes unused as comments)
###### Python libs
#import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets # QtWidgets inherits Gui,Core
#import threading
#import multiprocessing as mp
# os,sys,csv,pathlib,shutil, re,math
import os,sys,time
import subprocess
import re,math
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.dates as mdates
###### Global: External vars and global vars management functions/classes
# from globals import settings,shares_dir,co_dir,co_dir_archive,co_dir_f,co_dir_archive_f,co_ASXlist_file,co_list_file
#import globals as g
###### External Classes

def sorry():
  print("sorry")
  QtWidgets.QMessageBox.information(None,"Sorry","Not implemented")

def help_about():
  'Provides information about the progrom'
  print("help_about")
  QtWidgets.QMessageBox.information(None,"About: "+g.settings.settings['prog_name'],  \
  """  This program plots maths fuctions
  to understand what is beautiful.

  Version 2020.11.0   
 Nov 2020
  
  Copywrite Raymond H Kiefer 2020
  """)

from win_main import Ui_win_main
class win_main(QtWidgets.QMainWindow,Ui_win_main):
  '''Main Window
  Debugging with VS Code debugger of QT Tread Class not possible 
  '''
  def __init__(self,*args, **kwargs):
    super(win_main,self).__init__(*args,**kwargs)
    time_start=time.time()
    print("Starting win_main")
    ###### Load/Setup GUI ######
    self.setupUi(self)
    # self.setGeometry(200,100,800,600)
    # window.setGeometry(200,100,1366,768)
    # PC&HD 1920x1080, Notebook 1366x768, 50%HD 960x540
    # Using Ui settings
    self.show() #show the GUI now so user can see initialiasation as can take several seconds
    ###### Class objects init ######
    #g.init() # Global


  def closeEvent(self, event):
    del self.help_help_thread
    print("Closing win_main and associated windows")

if __name__ == '__main__':
  print("This is a GUI application, starting GUI")
  app = QtWidgets.QApplication(sys.argv)
  window = win_main()
  #window.showFullScreen()
  window.showMaximized()
  sys.exit(app.exec_())
else:
  print("Run this file donot import it")