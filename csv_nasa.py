from scipy.io import loadmat
import pandas as pd

data = loadmat(r".\Nasa\1. BatteryAgingARC-FY08Q4\B0005.mat")
data = {k: v for k, v in data.items() if not k.startswith('_')}
myData = {k:{'t':[], 'v':[], 'a':[], 'T':[]} for k in data}

print(data["B0005"])