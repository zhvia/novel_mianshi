import datetime
import jwt


class Token:
    salt = 'zhengwei'
    # def creat_token(self, password):
    #     token = {
    #         'exp': datetime.datetime.now() + datetime.timedelta(seconds=5),  # 过期时间
    #         'iat': datetime.datetime.now(),  # 开始时间
    #         'iss': 'zhengwei',  # 签名
    #         # 内容
    #         'data': {
    #             'username': self,
    #             'password': password
    #     },
    # }
    #     obj = jwt.encode(token, 'secret', algorithm='HS256')
    #     return obj
    def create_token(self, is_vip):
        # 构造header
        headers = {
            'typ': 'jwt',
            'alg': 'HS256'
        }
        # 构造payload
        payload = {
            'username': self,  # 自定义用户ID
            'is_vip': is_vip,  # 自定义用户名
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)  # 超时时间
        }
        token = jwt.encode(payload=payload, key='zhengwei', algorithm="HS256", headers=headers).decode('utf-8')
        return token

    def check_token(token):
        """
        根据token获取payload
        :param token:
        :return:
        """
        try:
            # 从token中获取payload【不校验合法性】
            # unverified_payload = jwt.decode(token, None, False)
            # print(unverified_payload)
            # 从token中获取payload【校验合法性】
            verified_payload = jwt.decode(token, 'zhengwei', True)
            return verified_payload
        except jwt.exceptions.ExpiredSignatureError:
            return 'token已失效'
        except jwt.DecodeError:
            return 'token认证失败'
        except jwt.InvalidTokenError:
            return '非法的token'

