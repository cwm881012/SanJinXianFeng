'''
解析用户配置文件
'''

#密码加密
from Crypto.Cipher import AES
import base64
#配置文件解析'
import configparser

class EncryptData:
    def __init__(self):
        self.key = "sanjinxianfengya".encode("utf8")  # 初始化密钥
        # self.key = "1111111111111111".encode("utf8")  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


class SanJinXianFengLoginInfo:
    # __login_name = ''
    # __login_password = ''

    def __init__(self, Path="sjxf_user.conf"):
        self.__UserConfPath = Path
        self.__GetUserNameFromConf(Path)
    
    def __GetUserNameFromConf(self, Path):
        login_msg = configparser.ConfigParser()
        login_msg.read(self.__UserConfPath)
        self.__login_name = login_msg["login"]["login_name"]
        self.__login_password = login_msg["login"]["login_password"]
    
    def LoginName(self) -> str:
        return self.__login_name

    def LoginPassword(self) -> str:
        return self.__login_password

    def LoginPasswordEncrypt(self) -> str:
        Encrypto = EncryptData()
        return Encrypto.encrypt(self.__login_password)

#    def LoginPasswordDecrypt(self):
#        return 
