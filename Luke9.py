from hashlib import md5

def decode(data, first_hash='julekalender'):
    
    # Initialize
    message = ''
    previous_hash = md5(first_hash.encode('utf-8')).hexdigest()

    # Iteratively find next part of message by searching through data
    while data:
        for entry in data:
            
            # Extract information and compute hash
            letter = entry['ch']
            letter_hash = entry['hash']
            new_hash = md5((str(previous_hash) + letter).encode('utf-8')).hexdigest()

            # Compare computed hash by hash from input-data
            if new_hash == letter_hash:
                message += letter
                previous_hash = letter_hash
                data.remove(entry)
                break

    return message

data = [{ "ch": "e", "hash": "758b9a55adaa1e7ea7c2c47420af06e1" },
        { "ch": "m", "hash": "98c0aab7006c1032c4199ec291691377" },
        { "ch": "I", "hash": "3b4608ccc221acb6baa6d9249f66a2cf" },
        { "ch": ",", "hash": "6e04980f15a4c783a6c45eaeac9a567f" },
        { "ch": "p", "hash": "11ad23b1bdbf9180ddb710cd91b4d805" },
        { "ch": "a", "hash": "efbe982cf2135f455623291243b3719d" },
        { "ch": "1", "hash": "acfa6f658a379a037def3bbed661d5f7" },
        { "ch": ",", "hash": "48deb682d80da88d8192a4f8048ed244" },
        { "ch": "e", "hash": "883a020b4e9f61bc7e40d06fe2bddb7b" },
        { "ch": "i", "hash": "857768072f446b6c8646cb650be50d9c" },
        { "ch": "n", "hash": "04186880ea63761e083a1dd969bb4ed4" },
        { "ch": "k", "hash": "8a0629b058c0a428294091efba3756e4" },
        { "ch": "v", "hash": "c8909d7e93e9b21d041d389ececffe88" },
        { "ch": " ", "hash": "bcaf653ac0deea6d4d0b0a2d1c553dfe" },
        { "ch": "s", "hash": "fba0b9ac4c237982bbd5d60002ec8859" },
        { "ch": "t", "hash": "0b4bcd9b83bca4ea44c5927e7cca5d8c" },
        { "ch": " ", "hash": "63e9087833b6ed2e926c70abe25a1ff4" },
        { "ch": "0", "hash": "496d780665794c923d60b4a3a9cba5b6" },
        { "ch": " ", "hash": "ae07f300e0a4dc848ff168a6d9af2583" },
        { "ch": "r", "hash": "4794155c02c99f1a191cac83dab68294" },
        { "ch": " ", "hash": "9b5e41b14b1a3e701531c4f9a5f80dd5" },
        { "ch": ")", "hash": "177b123bb8cd17ad0dec2df48a335415" },
        { "ch": "n", "hash": "4929a87a6d133f6d81ccd26a1b9f49c8" },
        { "ch": " ", "hash": "7eeb6a49352bbbe9214b6723c1bb6be8" },
        { "ch": "a", "hash": "18b4c7bfcde08a7c162423e05afc845c" },
        { "ch": "H", "hash": "14e5e859d836afd512ab06e71978c1fe" },
        { "ch": ":", "hash": "844891de49b2e4b64171d0c2586d1c3d" },
        { "ch": "a", "hash": "5eedc289128b74b52a1b75f7adc2d55a" },
        { "ch": ".", "hash": "d0813c95a34627d63dc2368b852973b1" },
        { "ch": "D", "hash": "0eb77cdd627ae856d2f4053f6666238d" },
        { "ch": "v", "hash": "cb1e11fe8841bb47262e567c9f341145" },
        { "ch": " ", "hash": "6283e00bac0641ac1eec55b26c0d4f11" },
        { "ch": "1", "hash": "c197ebe58ddf4d8aa4a5e97ac5e12648" },
        { "ch": "S", "hash": "3e3227614cd7b031281bfcc1c636273d" },
        { "ch": ".", "hash": "3a3fa49c0b80841fb163f3835c0f75df" },
        { "ch": "]", "hash": "69ca4e8bbcf72bd70bfe476964817e48" },
        { "ch": "p", "hash": "9b748d4ee5c3fa97fa279d8af3545f83" },
        { "ch": "e", "hash": "239564deec76b412c11d425004581f41" },
        { "ch": "s", "hash": "83e02d8dcb8e137576e8ea357e0a3f9d" },
        { "ch": "N", "hash": "ded3f29af731cdb795bbec1ab73adc54" },
        { "ch": "e", "hash": "f5353af3390889b3dc8c3c0ebd46322d" },
        { "ch": "0", "hash": "4f9feeeb8e6cb472c042d80bd8a4226a" },
        { "ch": ":", "hash": "b8ded9a118fff0bfffd62d2ec1037a14" },
        { "ch": "(", "hash": "539478a7b27567c24e6f55699f0a6e00" },
        { "ch": " ", "hash": "72fcaeeb3593f587c6e49655e37bf4f2" },
        { "ch": "0", "hash": "f15d63c0285d6b8f24f96986dd947aef" },
        { "ch": "N", "hash": "c51408c692cd224be019f16f20488223" },
        { "ch": "[", "hash": "269f3c2603bfdd5f4e37776ca160f7c5" },
        { "ch": "l", "hash": "ac0d9f479f5892c80551bca9175f2128" },
        { "ch": "J", "hash": "151d0841cd30878032c51fcb042b545a" },
        { "ch": "a", "hash": "42c77a01e52ca762bcfb34b8c108bdab" },
        { "ch": "?", "hash": "625af19720d86f1f3227f18c5417eed6" },
        { "ch": " ", "hash": "99d8387ffba49e74ebfab566efc83e14" },
        { "ch": "e", "hash": "285498ca33213a0d14fdb0214e6ae6ab" },
        { "ch": "r", "hash": "76d53254279c7b357a50ccbb77088293" },
        { "ch": "1", "hash": "bb48a8b09d2a2162f0cf1f1ef9babf9c" },
        { "ch": "s", "hash": "3d31154eca37bfa46588c4339e111773" }] 

message = decode(data)
print(message)

