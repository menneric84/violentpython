import zipfile
from threading import Thread
import optparse
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except Exception as inst:
        return
def main():
    parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help ='specify zip file')

    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args)= parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname) 
    zFile = zipfile.ZipFile('supportingfiles/CH1/evil.zip')
    passFile = open('supportingfiles/CH1/dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
        guess = extractFile(zFile, str(password))
        if guess:
            print('[+] Password cracked ' + password + '\n')
            exit(0)
    print('[+] Password not cracked \n')
if __name__ == '__main__':
    main()