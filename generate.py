import os

os.system("ls")
os.system("touch f1.txt")
os.system("echo \"TEST1\" > f1.txt")

os.system("touch f2.txt")
os.system("echo \"TEST2\" > f1.txt")

os.system("touch f3.cpp")
os.system("echo \"int main(){}\" > f1.txt")

os.system("wget https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg")

os.system("mkdir victimFolder")
os.system("cd victimFolder")

os.system("touch testing")
os.system("echo \"end of test. this is the last file generated\" > testing")

print("done!")