import hashlib


def HashSecret(secret, targetLeadingString):
    testHash = 1
    while True:
        m = hashlib.md5()
        m.update(secret + str(testHash))
        hexMD5 = m.hexdigest()
        if str(hexMD5).startswith(targetLeadingString):
            return str(testHash)
        testHash += 1

print 'Lowest number that produces hexMD5 starting with 6 0s: ', HashSecret('bgvyzdsv', '000000')
