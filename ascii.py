from PIL import Image
import argparse

# 首先，构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符宽度
parser.add_argument('--height', type=int, default=80)  # 输出字符高度

# 解析并获取参数
args = parser.parse_args()

# 输入的图片文件路径
IMG = args.file

# 输出字符画的宽度
WIDTH = args.width

# 输出字符画的高度
HEIGHT = args.height

# 字符画使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char = list("1234567890")

# RGB转字符函数
def get_char(r, g, b, alpha=265):
    # 判断alpha值
    if alpha == 0:
        return ' '

    # RGB转灰度值公式
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    length = len(ascii_char)

    # 根据length长度计算从字符集中取哪个字符
    return ascii_char[int(gray / (256 + 1) * length)]


if __name__ == '__main__':       # 表示如果 ascii.py 被当作 python 模块 import 的时候，这部分代码不会被执行
    im = Image.open(IMG)         # 使用PIL打开图片
    # im = im.resize((WIDTH, HEIGHT), Image.NEAREST)   # 调整图片的宽和高

    ratio = im.width/im.height          # 计算图片的宽高比
    HEIGHT = int(WIDTH * ratio)         # 重新计算图片高度
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)   # 调整图片的宽和高

    # 初始化输出字符串
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

