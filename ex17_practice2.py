from sys import argv
script,from_file,to_file = argv
open(to_file,'w').write(open(from_file).read())
#宇宙无敌究极蛇皮精简版
#最先open（from_file)然后把里面的内容read出来
#随后写入到to_file里面
"""
in_file = open(from_file)
indata = in_file.read()
out_file = open(to_file,'w')
out_file.write(indata)
"""
#精简上述四行合为一行
