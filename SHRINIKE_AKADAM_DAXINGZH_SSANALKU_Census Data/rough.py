# Import numpy and any other required packages here:
import numpy as np
import pandas as pd
import csv
import warnings
import sys

#############################################
########### Removing of Warnings ############
########## Refered from Stackflow ###########
warnings.filterwarnings("ignore", category=FutureWarning)

if not sys.warnoptions:
    warnings.simplefilter("ignore")
