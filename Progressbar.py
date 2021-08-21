import sys
import time
import os
def progressBar():
	animation     = ["[----------]","[>--------]","[>>--------]", "[>>>-------]", "[>>>>------]", "[>>>>>-----]", "[>>>>>>----]", "[>>>>>>>---]", "[>>>>>>>>--]", "[>>>>>>>>>-]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\rDownload ...  " + save_anim + f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.075)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Download Complete [>>>>>>>>>>] 100%")
			break

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("")
	sys.stdout.write(f"\r{progressBar()}")
	sys.stdout.flush()
	break
	
os.system('cls' if os.name == 'nt' else 'clear')
