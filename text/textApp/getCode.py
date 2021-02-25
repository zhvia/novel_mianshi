
from PIL import ImageDraw, ImageFont, Image
from io import BytesIO
import random


def get():
    image = Image.new('RGB', (100, 50), color='#606479')
    draw = ImageDraw.Draw(image, 'RGB')
    # 可以在C:\Windows\Fonts中找需要的字体
    font = ImageFont.truetype("simsun.ttc", 30, encoding="utf-8")

    strings = "qwertyuipasdfghjkzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM23456789"
    web_str = []
    code = ''
    # for i in range(0, 100):
    #     xy = (random.randrange(0, width), random.randrange(0, height))
    #     fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    #     draw.point(xy, fill=fill)
    for i in range(4):
        web_str.append(strings[random.randint(0, len(strings)-1)])
        code = ''.join(web_str)
    draw.text(xy=(random.randint(10, 20), random.randint(0, 10)), text=code, fill='black', font=font)
    f = BytesIO()
    image.save(f, format='PNG')
    data = f.getvalue()
    # datas = base64.b64encode(data).decode()
    return data, code



