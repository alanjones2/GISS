import pandas as pd

files = ['data/GLB.Ts+dSST.csv','data/NH.Ts+dSST.csv','data/SH.Ts+dSST.csv']

def read_GLB():
    return read_file(0)
def read_NH():
    return read_file(1)
def read_SH():
    return read_file(2)

def read_file(i):
    
    df = pd.read_csv(files[i], skiprows=1)
    with open(files[i]) as file:
        title = file.readline().rstrip()
    return title, df
