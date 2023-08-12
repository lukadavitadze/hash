

def hash():
    import random
    hash1 = ''
    key = input('one_letter key:')
    name = input('name:')
    abc = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9']
    if key in abc:
        #print(abc.index(key))
        for i in name:
            #print(abc.index(i) + abc.index(key),end=' ')
            if abc.index(i) + abc.index(key) > 72:
                print('EEEEErrrroooorrrrrr')
            else:
                # print(ord(abc[abc.index(i) + abc.index(key)]))     '@','!','$','%','*','1','2','3','4','5','6','7','8','9'
               hash1 = hash1 + abc[abc.index(i) + abc.index(key)]
    print('your hash is:',hash1)
    print(' ')

def anhash():
    hash2 = ''
    key = input('key: ')
    hash1 = input('hash: ')
    abc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '@', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2',
           '3', '4', '5', '6', '7', '8', '9']

    if key in abc:
        # print(abc.index(key))
        for i in hash1:
            hash2 = hash2 + abc[abc.index(i) - abc.index(key)]
    print('your hash means',hash2)
hash()
anhash()