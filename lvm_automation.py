import os

TGREEN =  '\033[32m'
TWHITE = '\033[37m'
TYELLOW = '\033[33m'
TBLUE = '\033[34m'
TRED = '\033[31m'


def createPV(diskName):
    print(TYELLOW ,'Creating Physical volume')
    print(TBLUE)
    os.system('pvcreate  {}'.format(diskName))

def createVG(diskName, d1, d2, d3):
    print(TYELLOW ,'Creating Volume Group ')
    print(TBLUE)
    os.system('vgcreate  {} {} {} {}'.format(diskName, d1, d2, d3))

def displayAllPV():
    print(TYELLOW, 'Displaying all the physical volumes available ')
    print(TWHITE)
    os.system('pvs ')

def displayAllVG():
    print(TYELLOW, 'Displaying all the  volume groups available ')
    print(TWHITE)
    os.system('vgdisplay ')

def displayPV(pvName):
    print(TYELLOW, 'Displaying the physical volume {} '.format(diskName))
    print(TWHITE)
    os.system('pvdisplay  {}'.format(pvName))
    
def displayVG(vgName):
    print(TYELLOW, 'Displaying the volume group {} '.format(vgName))
    print(TWHITE)
    os.system('vgdisplay  {}'.format(diskName))

def displayLV(vgName, lvName):
    print(TYELLOW, 'Displaying the Logical volume {}/{} '.format(vgName,lvName))
    print(TWHITE)
    os.system('lvdisplay  {}/{}'.format(vgName,lvName))

def createLV(lvName, vgName, size):
    print(TYELLOW, 'Creating the logical volume ')
    print(TWHITE)
    os.system('lvcreate {} --size {} --name {}'.format(vgName, size, lvName))

def formatt(vgName, lvName):
    print(TYELLOW, 'Formating the logical volume ')
    print(TWHITE)
    os.system('mkfs.ext4 /dev/{}/{} '.format(vgName, lvName))

def extend(size , vgName, lvName):
    print(TYELLOW, 'Extending the logical volume ')
    print(TWHITE)
    os.system('lvextend --size {} /dev/{}/{}'.format(size,vgName,lvName))

def resize(vgName, lvName):
    print(TYELLOW, 'Reformatting the logical volume ')
    print(TWHITE)
    os.system('resize2fs /dev/{}/{}'.format(vgName,lvName))
    
def displayBlocks():
    print(TYELLOW, 'Showing the blocks available ')
    print(TWHITE)
    os.system('lsblk ')

def mounting(vgName,lvName, direc):
    print(TYELLOW, 'mounting the partition to the given directory ')
    print(TWHITE)
    os.system('mount /dev/{}/{} /{}'.format(vgName,lvName,direc))

def makingDirectory(diskName):
    print(TYELLOW, 'Making a new directory ')
    print(TWHITE)
    os.system('mkdir {} '.format(diskName))

def disks():
    print(TYELLOW, 'Showing available disks ')
    print(TWHITE)
    os.system('fdisk -l ')

def spec_disks(diskName):
    print(TYELLOW, 'Showing disk information of {}'.format(diskName))
    print(TWHITE)
    os.system('fdisk -l {} '.format(diskName))

def deletelv(vgName,lvName):
    print(TYELLOW, 'Removing lv {}'.format(lvName))
    print(TWHITE)
    os.system('lvchange -an /dev/{}/{} '.format(vgName,lvName))
    os.system('lvremove /dev/{}/{} '.format(vgName,lvName))

def deletevg(vgName):
    print(TYELLOW, 'Removing vg {}'.format(vgName))
    print(TWHITE)
    os.system('vgchange -an {} '.format(vgName))
    os.system('vgremove {} '.format(vgName))

def deletepv(pvName):
    print(TYELLOW, 'Removing pv {}'.format(pvName))
    print(TWHITE)
    os.system('pvremove {} '.format(pvName))

def unmount():
    print(TBLUE)
    direc = input('''Enter the directory name on which partition is been unmounted :''')
    print(TYELLOW, 'Unmounting the partition from the given directory ')
    print(TWHITE)
    os.system('umount {}'.format(direc))
    print('Successfully Unmounted')

def check_menu():
    print(TGREEN,"Follow the menu, to perform tasks : ")
    print(TWHITE, 'Press # : To print MENU',TGREEN,'''
          -> To see the storage devices available : Press 1
          -> To see specific storage device details : Press 2
          -> To display the Physical Volumes available : Press 3
          -> To create a Physical volume : Press 4
          -> To display a specific Physical volume : Press 5
          -> To create a Volume group : Press 6
          -> To display the volume group available : Press 7
          -> To display a specific Volume group : Press 8
          -> To create a logical volume as per the storage requirements : Press 9
          -> To display a logical volume groups available : Press 10	
          -> To format the logical volume partition : Press 11
          -> To extend the space of the logical volume : Press 12
          -> To format the unformatted part : Press 13
          -> To see the block devices along with their mount point : Press 14
          -> To mount/unmount the logical volume to/from some directory, : Press 15
          -> To create a directory : Press 16
          -> To delete logical volume : Press 17
          -> To delete volume group : Press 18
          -> To delete physical volume : Press 19
          -> To exit the program : Press 0  
    ''')

if __name__ == "__main__" :
	print(TGREEN ,"\t \t \t Welcome to the LVM " )
	check_menu()
	while (True) :
		print(TYELLOW,"Choose b/w 0 to 18 or # ")
		print(TBLUE)
		option = input('Enter your option here : ')
		try:
			if option == '0' or option == ' ':
				print(TYELLOW, 'Exiting from the program ....')
				break
        
			elif option == '#':
				check_menu()
			elif (int(option) > 0 and  int(option) < 20 ):
				print(TYELLOW, 'processing request.....')
				if int(option) == 1 :
					disks()

				elif int(option) == 2:
					print(TBLUE)
					diskName = input('''Enter the name of storage device you want details of : ''')
					spec_disks(diskName)
            
				elif int(option) == 3 :
					displayAllPV()

				elif int(option) == 4 :
					print(TBLUE)
					diskName = input('''Enter the name of disk that you need to make a physical volume : ''')
					createPV(diskName)
            
				elif int(option) == 5 :
					print(TWHITE)				
					print("Available PVS:")
					print(TBLUE)
					os.system('pvs ')
					pvName = input('''Enter the physical volume name that you wants to retrieve  : ''')
					displayPV(pvName)
			
				elif int(option) == 6 :
					print(TRED)
					print("Minimum to be added : 1\nMaximum to be added : 3\nLeave blank for not to be added")		
					print(TBLUE)
					d1 = input('Required,enter the physical volume to be added : ')
					d2 = input('Optional,enter the physical volume to be added : ')
					d3 = input('Optional,enter the physical volume to be added : ')
					diskName = input('''Enter the name that you wants to give to your Volume group : ''')
				
					createVG(diskName,d1,d2,d3)

				elif int(option) == 7 :
					displayAllVG()

				elif int(option) == 8 :
					print(TBLUE)
					vgName = input('''Enter the volume group name that you wants to retrieve  : ''')
					displayVG(vgName)

				elif int(option) == 9 :
					print(TBLUE)
					vgName = input('Enter the volume group name : ')
					size = input('''Enter the size of logical device you want : ''')
					lvName = input('''Enter the name of your choice for Logical volume : ''')
					createLV(lvName, vgName, size)

				elif int(option) == 10 :
					print(TBLUE)
					vgName = input('Enter the volume group name : ')
					lvName = input('Enter the Logical volume name : ')
					displayLV(vgName, lvName)
				elif int(option) == 11 :
					print(TBLUE)
					vgName = input('Enter the volume group name : ')
					lvName = input('Enter the Logical volume name : ')
					formatt(vgName, lvName)

				elif int(option) == 12 :
					print(TBLUE)
					vgName = input('Enter the volume group name : ')
					size = input('Enter the size to be extended : ')
					lvName = input('Enter the Logical volume name : ')
					extend(size , vgName, lvName)

				elif int(option) == 13 :
					print(TBLUE)
					vgName = input('Enter the volume group name : ')
					lvName = input('Enter the Logical volume name : ')
					resize(vgName, lvName)

				elif int(option) == 14 :
					displayBlocks()

				elif int(option) == 15 :
					print(TBLUE)
					choose = input('mount/unmount (m/u) : ')
					if choose == 'm':
						vgName = input('Enter the volume group name : ')
						lvName = input('Enter the Logical volume name : ')
						direc = input('''Enter the directory name to be linked with this Logical volume :''')
						mounting(vgName,lvName, direc)
					elif choose == 'u':
						unmount()
					else:
						continue
				elif int(option) == 16 :
					print(TBLUE)
					diskName = input('''Enter the name for the directory that you wants to create : ''')
					makingDirectory(diskName)

				elif int(option) == 17 :
					print(TBLUE)
					print('Be Sure that you have unmounted the associated Partition')
					choose = input('Mounted/Unmounted, Choose (m/u) : ')
					if choose == 'm':
						unmount()
					elif choose == 'u':
						vgName = input('Enter the volume group name : ')
						lvName = input('Enter the Logical volume name : ')
						deletelv(vgName,lvName)
					else :
						continue

				elif int(option) == 18 :
					print(TBLUE)
					print('Be Sure that you have removed the associated LV')
					choose = input('LV removed/not-removed Choose (r/n)')
					if choose == 'n':
						print('Please got to STEP 16 to remove LV')
					elif choose == 'r':
						vgName = input('Enter the volume group name : ')
						deletevg(vgName)
					else :
						continue

				elif int(option) == 19 :
					print(TBLUE)
					print('Be Sure that you have removed the associated VG')
					choose = input('LV removed/not-removed Choose (r/n)')
					if choose == 'n':
						print('Please got to STEP 16 to remove VG')
					elif choose == 'r':
						print('Tip: If more than one then put them space separated..')
						pvName = input('Enter the physical volume name : ')
						deletepv(pvName)
					else :
						continue

				else :
					print(TRED, 'Enter valid options only !!!')
					continue
				
			else :
				print(TRED, 'Enter valid options only !!!')
				continue

		except Exception as e :
			print(TRED, 'Enter valid options only !!!')
			continu
	print(TYELLOW,'Execution done!!!!',TWHITE)
