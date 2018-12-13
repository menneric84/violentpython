import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('supportingfiles/CH1/dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptword = crypt.crypt(word, salt)
        if ( cryptword == cryptPass):
            print("[+] Found the password: " + word + "\n")
            return
    print ("[-] Password not found. \n")

def main():
    passFile = open('supportingfiles/CH1/passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptpass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For: " + user
            testPass(cryptpass)
if __name__ == "__main__":
    main()
