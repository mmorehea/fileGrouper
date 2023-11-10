import os
import glob
import re
import code


filepath = "./test/"

matches = {}

for root, dirs, files in os.walk(filepath, topdown=False):
	for name in dirs:
		print('processing folder: ' + name)
		basepath = root + '/' + name + '/'
		targetdirglob = basepath + '*.txt'
		filelist = glob.glob(targetdirglob)
		while(len(filelist) > 0):
			target = os.path.basename(filelist[0])
			##build regex matcher
			regString = ""
			
			isNumber = False
			for each in target:
				if each.isdigit():
					if isNumber:
						continue
					else:
						isNumber = True
						regString = regString + ("[0-9]+")
					
				else:
					regString = regString + (each)
					isNumber = False

			#look for matches, remove them from list, put them in group
			matches[target] = basepath + target
			#remove target from list
			filelist.remove(filelist[0])
			print('searching for target: ' + target)
			toRemove = []
			for each in filelist:
				bname = os.path.basename(each)
				#check each against regex, if match remove from list, then add to dict
				match = re.search(regString, bname)
				if match:
					print('matched ' + target + " and " + bname)
					if target in matches:
						if type(matches[target]) == list:
							l = matches[target]
						else:
							l = [matches[target]]
						
						l.append(each)
						matches[target] = l
					else:
						matches[target] = list(bname)
					toRemove.append(each)
			for each in toRemove:
				filelist.remove(each)


##print your matches

for key in matches:
	print(key)
	print(matches[key])
	print("---")

		


