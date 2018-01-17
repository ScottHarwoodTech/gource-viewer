import os
import sys
mainD = input("Enter the start dir")
repos = os.listdir(mainD)
for repo in repos:
    os.system("gource "+os.path.join(mainD,repo))

