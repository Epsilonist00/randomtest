import urllib.request
import time

ver_num=0.5
content='wow new content!!!'
repo_path='https://github.com/Epsilonist00/randomtest'
version_path='https://github.com/Epsilonist00/randomtest/blob/main/version.txt'


def update():
    try:
        with urllib.request.urlopen(version_path,timeout=5) as response:
            latest_version=response.read().decode('utf-8').strip()
        if str(ver_num) != str(latest_version):
            print("There is a update currently available.")
            print(f"Your Version: '{ver_num}' Lastest Version: '{latest_version}'")
            print(f"You can download the updated package from '{repo_path}' and uninstall this package, or continue using this version. (you will be notified everytime the program is launched)")
            print()
            print(f"UPDATE: Download the new package at {repo_path} or press Enter to continue using the current version")
            input(">>>")
    except Exception as e:
        print("oh.. shit..")
        print()
        time.sleep(2) 
        print("wait.. no??")
        print()
        time.sleep(3)
        print("nvm. yup... something fucked up.")
        print()
        time.sleep(2)
        print(f"uhh it says here quote: '{e}'")
        time.sleep(1)
        raise Exception(e)

def adding():
    print("Type the First Number to be added")
    num_1=int(input(">>>"))
    print()
    print("Type the Second Number to be added.")
    num_2=int(input(">>>"))
    sum=int(num_1)+int(num_2)
    print(sum)

if __name__=='__main__':
    update()
    adding()
    print(content)





