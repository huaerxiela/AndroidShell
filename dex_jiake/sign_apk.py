import shutil
import subprocess
import os
import pathlib


#  ValueError: ZIP does not support timestamps before 1980
#  touch `find . -type f`

def rcmd(cmd):
    if type(cmd) is str:
        cmd = cmd.split(" ")
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, check=False)
    if p.returncode > 0:
        print(p.stdout.decode("utf8"))
        print(p.stderr.decode("utf8"))


JARSIGNER = shutil.which("jarsigner")
ADB       = shutil.which("adb")
KEYSTORE  = "keystore.jks"
dex = "classes.dex"

workingdir = pathlib.Path(".")  / "ke"



# Copy the hook library
print(f"[+] Copying {dex} in the APK")
shutil.copy(dex, workingdir)

# Remove old signature
try:
    shutil.rmtree(os.path.join(workingdir, "META-INF"))
except:
    pass

# Zip
print(f"[+] APK Building...")
shutil.make_archive("new", 'zip', workingdir)
shutil.move("new.zip", "new.apk")

cmd_sign = [
    JARSIGNER,
    "-verbose",
    "-sigalg", "SHA1withRSA",
    "-digestalg", "SHA1",
    "-keystore", KEYSTORE,
    "-storepass", "123456",
    "new.apk",
    "huaerxiela"]

print(f"[+] Signing the APK")
rcmd(cmd_sign)


