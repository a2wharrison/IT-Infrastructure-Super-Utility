def HealthCheck(verbose):
	import os
	from sys import argv
	from modules.pinger import *
	while True:
		os.system('cls')
		print "\n"
		print "Welcome to the Health Check Scanner"
		print "\n"
		print "Press 1 to run a full environment scan."
		print "Press 2 to run a scan against an specific environment."
		print "Press 3 to Exit."
		print "\n"

		choice = raw_input("Enter your choice: ")
		if choice == "1":
			if "v" in verbose:
				flag = "v"
			else:
				flag =""

			ConfigFiles = []
			for file in os.listdir("./InfrastructureItems"):
			    if file.endswith(".txt"):
			    	ConfigFiles.append("InfrastructureItems/"+file) 

			print "Testing All Core Systems...\n"

			for i in range(len(ConfigFiles)):
				print systemname % ConfigFiles[i]
				devices = open(ConfigFiles[i], "r")
				lines = devices.readlines()
				pinger(lines, flag)
				devices.close() 
			print "\n\033[1;37mScan Completed Successfully.\033[1;m\n"
			raw_input("Press enter to continue...")
			os.system("cls")


		elif choice == "2":
			if "v" in verbose:
					flag = "v"
			else:
				flag =""

			options = []
			for file in os.listdir("./InfrastructureItems"):
			    if file.endswith(".txt"):
			    	options.append(file)
			nums_and_files = zip(range(len(options)),options)
			os.system("cls")
			print "\nAvailable lists to modify: \n"
			for x in nums_and_files:
				print x
			choice = raw_input("Please type number of desired environment to scan or type 'exit' to quit: ")

			if choice.isdigit() == False:
				os.system("cls")
				break
			elif int(choice) in range(len(options)):
				filelocation = "./InfrastructureItems/" + options[int(choice)]
				selectedfile = open(filelocation, "r")
				ConfigFiles = [0]
				print "\nTesting selected System...\n"
				for i in range(len(ConfigFiles)):
					devices = selectedfile
					lines = devices.readlines()
					pinger(lines, flag)
					devices.close() 
				print "\n\033[1;37mScan Completed Successfully.\033[1;m\n"
				selectedfile.close()
				raw_input("Press enter to continue...")
				os.system("cls")

			else:
				os.system('cls')
				break
							

		elif choice == "3":
			os.system('cls')
			break


def SystemImporter():
	import os
	import sys
	import glob
	os.system('cls')
	while True:
		os.chdir("C:/users/stewart.olson/desktop/stuff/code/python/HealthCheck")
		print "\n"
		print "Welcome to the Abraxas.io HealthCheck Configuration Manager"
		print "\n"
		print "Press 1 to add addresses to config files."
		print "Press 2 to search for addresses in config files."
		print "Press 3 to view config files."
		print "Press 4 to remove an entry from a config file."
		print "Press 5 to remove an entry from all config files."
		print "Press 6 to create a new config file."
		print "Press 7 to remove a configuration file."
		print "Press 8 to exit the configuration manager."
		print "\n"
		choice = raw_input("Enter your selection: ")
		os.system("cls")

		lastSearch = []
		
		if choice == "1":
			options = []
			for file in os.listdir("./InfrastructureItems"):
			    if file.endswith(".txt"):
			    	options.append(file)

			nums_and_files = zip(range(len(options)),options)
			print "\nAvailable lists to modify: \n"
			for x in nums_and_files:
				print x
			choice = raw_input("Please type desired number to edit or 'exit' to quit: ")
			if choice == "exit":
				os.system('cls')
				print "\n\nThanks for keeping your files up to date!"
				break
			elif choice.isdigit() == False:
				os.system('cls')
				print "\n\nThanks for keeping your files up to date!"
				break
			else:
				choice = int(choice)

			while True:
				filelocation = "./InfrastructureItems/" + options[choice]
				selectedfile = open(filelocation, "a+")
				morehosts = raw_input("\n\nWould you like to add an IP/Hostname to this file? yes/no : ")
				if morehosts == "yes":
					hostname = raw_input("\nPlease enter IP/Hostname to add to selected file: ")
					selectedfile.write("\n"+hostname)
					print "IP added Successfully"
				elif morehosts != "no":
					print "Please enter 'yes' or 'no'"
				else:
					print "IP added Successfully"
					selectedfile.close()
					os.system("cls")
					break

		elif choice == "2":
			searchresult = []
			os.system("cls")
			search = raw_input("Please enter IP/Hostname to search: ")
			os.chdir( "C:/users/stewart.olson/desktop/stuff/code/Python/HealthCheck/InfrastructureItems")
			print "\n"
			print "Searching files..."
			for file in glob.glob('*.txt'):
				with open(file) as f:
					contents = f.read()
				if search in contents:
					searchresult += contents
					print "IP or hostname has been found in " + file
			print "\n"
			clean = raw_input("Press (1) to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")
			else: continue

		elif choice == "3":
			os.system("cls")
			print "Configuration Viewer"
			options = []
			for file in os.listdir("./InfrastructureItems"):
			    if file.endswith(".txt"):
			    	options.append(file)
			nums_and_files = zip(range(len(options)),options)
			for x in nums_and_files:
				print x
			print "\nAvailable lists to modify: \n"
			choice = raw_input("Please type desired number to edit or 'exit' to quit: ")
			if choice == "exit":
				os.system('cls')
				print "\n\nThanks for keeping your files up to date!"
			else:
				choice = int(choice)
			filelocation = "./InfrastructureItems/" + options[choice]
			selectedfile = open(filelocation, "r")
			closefile = selectedfile
			selectedfile = selectedfile.readlines()
			stuff = []
			for things in selectedfile:
				stuff.append(things)
			nums_and_lines = zip(range(len(stuff)),stuff)
			for x in nums_and_lines:
				print x
			print "\nEnd of File.\n"
			clean = raw_input("Press (1) to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")
			else: continue
			closefile.close()

		elif choice == "4":
			os.system("cls")
			print "Configuration Line Editor"
			options = []
			for file in os.listdir("./InfrastructureItems"):
			    if file.endswith(".txt"):
			    	options.append(file)
			nums_and_files = zip(range(len(options)),options)
			for x in nums_and_files:
				print x
			print "\nAvailable lists to modify: \n"
			choice = raw_input("Please type desired number to edit or 'exit' to quit: ")
			if choice == "exit":
				os.system('cls')
				print "\n\nThanks for keeping your files up to date!"
			else:
				choice = int(choice)
			filelocation = "./InfrastructureItems/" + options[choice]
			selectedfile = open(filelocation, "r")
			closefile = selectedfile
			selectedfile = selectedfile.readlines()
			stuff = []
			editfile = selectedfile
			for things in selectedfile:
				stuff.append(things)
			nums_and_lines = zip(range(len(stuff)),stuff)
			for x in nums_and_lines:
				print x
			print "\nEnd of File.\n"
			closefile.close()

			deleteit = raw_input("Enter number of line to be removed: ")
			modifyfile = open(filelocation, "w")
			count = 0
			for line in selectedfile:
				if str(count) != deleteit:
					count += 1
					modifyfile.write(line)
				else:
					count +=1
			clean = raw_input("Press (1) to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")
			else: continue
			modifyfile.close()

		elif choice == "8":
			os.system("cls")
			break
		else:
			continue


def NetworkTools():
	import os
	os.system("cls")
	while True:
		print "\n"
		print "Welcome to the Network Tools menu."
		print "\n"
		print "Press 1 to run the ping utility."
		print "Press 2 to run nslookup."
		print "Press 3 to run tracert."
		print "Press 4 to run pathping."
		print "Press 5 to Exit"
		print "\n"

		choice = raw_input("Please make a selection: ")

		if choice == "1":
			target = raw_input("Enter IP or hostname to ping: ")
			os.system("ping " + target)
			clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")
			else: continue

		elif choice =="2":
			os.system("nslookup")
			clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")
			else: continue

		elif choice == "3":
			target = raw_input("Enter IP or hostname to trace: ")
			os.system("tracert " + target)
			clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")

		elif choice == "4":
			target = raw_input("Enter IP or hostname to pathping: ")
			os.system("pathping " + target)
			clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
			if clean == "1":
				continue
			elif clean == "2":
				os.system("cls")
			else: continue
		elif choice == "5":
			os.system("cls")
			break
		else:
			continue


def PowershellTools():
	import os
	import time
	import Tkinter as tk
	import tkFileDialog as filedialog
	while True:
		os.system("cls")
		print "\n"
		print "Welcome to the PowerShell Tools menu."
		print "\n"
		print "Press 1 to run a Powershell CLI."
		print "Press 2 to start a New-PSSession with a remote machine."
		print "Press 3 to get MD5 hash of object."
		print "Press 4 to unlock an AD account."
		print "Press 5 to exit"
		print "\n"

		choice = raw_input("Enter your choice: ")

		if choice == "1":
			os.system("powershell -NoProfile")

		elif choice =="2":
			target = raw_input("Enter your target hostname: ")
			print "Creating target.ps1 file to establish connection"
			pstarget = open("pstarget.ps1", "w")
			pstarget.write("$target = New-Pssession " + target + "\n")
			pstarget.write("Enter-PSSession $target" + "\n")
			pstarget.close()
			print "File created. Initiating Connection to remote host..."
			os.system("powershell -noexit -ExecutionPolicy Unrestricted C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\pstarget.ps1")


		elif choice == "3":
			raw_input("Press enter to select a file...")
			root = tk.Tk()
			root.focus_force()
			hash_path = filedialog.askopenfilename()
			hashtarget = open("hashtarget.ps1", "w")
			root.destroy()
			hashtarget.write('$target = "' + hash_path +'"\n')
			hashtarget.write("Get-FileHash -Algorithm MD5 $target | fl" + "\n")
			hashtarget.close()
			
			os.system("powershell -noexit -ExecutionPolicy Unrestricted C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\hashtarget.ps1")

		elif choice == "4":
			username = raw_input("Unlock AD User (Input username): ")
			print "Creating target.ps1 file to unlock AD account"
			psunlock = open("unlocktarget.ps1", "w")
			psunlock.write("$unlock = Unlock-ADAccount " + username + "\n")
			psunlock.close()
			print "File created. Unlocking User Account."
			os.system("powershell -ExecutionPolicy Unrestricted C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\unlocktarget.ps1")
			print "%s's account has been unlocked. Press enter to continue." % username
			raw_input("Press enter to continue...")
			os.system("cls")

		elif choice == "5":
			os.system("cls")
			break
		else:
			continu