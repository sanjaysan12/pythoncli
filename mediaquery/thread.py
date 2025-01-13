import threading
import os

def downloadFile(url,output):
    os.system('wget -o {output} {url}'.format(output=output,url=url))

if __name__ == "__main__":
    try:
        while True:
            threading.Thread(target=downloadFile, args=(input("Enter the url to download"),input("Enter a file name"))).start()
            
    except KeyboardInterrupt as e:
        print("Quitting.....")