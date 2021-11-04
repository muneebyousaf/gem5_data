import subprocess

mystring = "hello";
subprocess.call("/home/muneeb/gem5/build/X86/gem5.opt /home/muneeb/gem5/configs/learning_gem5/part1/argu.py /home/muneeb/gem5/tests/test-progs/hello/bin/x86/linux/"+mystring, shell=True)




