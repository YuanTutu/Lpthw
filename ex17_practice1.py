from sys import argv
from os.path import exists

script,from_file,to_file = argv
#将不必要的输出给屏蔽
#print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exists? {exists(to_file)}")
#print(f"Ready,hit RETURN to continue,CTRL-C to abort.")
#input()

out_file = open(to_file,'w')
out_file.write(indata)
#其实也可以屏蔽
#print("Alright,all done.")

out_file.close()
in_file.close()
