import subprocess


import shutil

for i in range(20):
    subprocess.run(["curl", "-LO", "https://www.gov.kr/nlogin/captcha"])
    shutil.move("captcha", "./assets/ex_{}.png".format(i))