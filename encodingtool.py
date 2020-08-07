import hashlib
import base64
import time
print("INSTAGRAM:{}".format('y.xi4'))
while True:
    print("""
1>for urllib
2>for base64
3>to know hash_type
4>exit


""")
    choos=input('>')
    if choos=='1':
        def encoding():
            hash1=input('hash : ')
            wordlist=input('word list :')
            op=open(wordlist,'r')
            for i in op.readlines():
                i=i.rstrip('\n')
                enc=i.encode('utf-8')
                if len(hash1)==32:
                    has=hashlib.new('md5')
                    has.update(enc.strip())
                    hashing=has.hexdigest()
                    if hashing==hash1:
                        print('hash found!')
                        print('{0} is {1}'.format(hash1,i))
                elif len(hash1)==40:
                    has=hashlib.new('sha1')
                    has.update(enc.strip())
                    hashing=has.hexdigest()
                    if hashing==hash1:
                        print('hash found!')
                        print('{0} is {1}'.format(hash1,i))
                elif len(hash1)==96:
                    has=hashlib.new('sha384')
                    has.update(enc.strip())
                    hashing=has.hexdigest()
                    if hashing==hash1:
                        print('hash found!')
                        print('{0} is {1}'.format(hash1,i))
                elif len(hash1)==56:
                    has=hashlib.new('sha224')
                    has.update(enc.strip())
                    hashing=has.hexdigest()
                    if hashing==hash1:
                        print('hash found!')
                        print('{0} is {1}'.format(hash1,i))
                if len(hash1)==64:
                    has=hashlib.new('sha256')
                    has.update(enc.strip())
                    hashing=has.hexdigest()
                    if hashing==hash1:
                        print('hash found!')
                        print('{0} is {1}'.format(hash1,i))
                elif len(hash1)==128:
                     has=hashlib.new('sha512')
                     has.update(enc.strip())
                     hashing=has.hexdigest()
                     if hashing==hash1:
                         print('hash found!')
                         print('{0} is {1}'.format(hash1,i))
        encoding()


    elif choos=='2':
        def bas():
            thash=input('the hash :')
            wlist=input('wordlist :')
            op=open(wlist,'r')
            for i in op.readlines():
                i=i.rstrip('\n')
                enc=i.encode('utf-8')
                base=base64.b64encode(enc)
                base=base.decode('utf-8')
                if base==thash:
                    print('hash found!')
                    time.sleep(1)
                    print('{0} is {1}'.format(thash,i))
                else:
                    print(i,'wrong...')
        bas()
    elif choos=='3':
        def le():
            print('if you entered wrong value the program will break already\n')
            has=input('put the hash here :')
            if len(has)==32:
                print('hash_type is [md5]')
            if len(has)==40:
                print('hash_type is [sha1]')
            if len(has)==96:
                print('hash_type is [sha384]')
            if len(has)==56:
                print('hash_type is [sha224]')
            if len(has)==64:
                print('hash_type is [sha256]')
            if len(has)==128:
                print('hash_type is [sha512]')
        le()

    elif choos>='4':
        break
