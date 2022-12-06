import os
from fractions import Fraction
from PIL import Image, ImageDraw
import math

def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def input_num():
    os.system('cls')
    while True:
        num = input("2より大きい有理数を入力してください。(n/m>2):")
        # print(type(num))
        if not(is_num(num)):
            os.system('cls')
            print("※数字を入力して下さい。")
        elif float(num) <= 2.0 :
            os.system('cls')
            print("※2より大きい値を入力してください。")
        else :
            break
    return num

def poly_info(num):
    frac = Fraction(num)

    print("正\t" + num + "\t角形")
    print("頂点\t" + str(frac.numerator) + "\t個")
    print("内角約\t" + str(180*(float(num)-2.0)/float(num)) + "\t度")


# 正n/m角形
# 1. 実数（浮動小数点ではなく文字列で受け取る）を分数の形に変換
# 2.  n/m > 2 であるかの判定
# 3. 円周上に等間隔のn個の点を打つ
# 4. 今いる点とm個先の点を線で結ぶ（n回繰り返す）
def main():
    num = input_num()
    poly_info(num)

    frac = Fraction(num)
    n    = frac.numerator   #分子
    m    = frac.denominator #分母

    # カラーの画像データ（Imageオブジェクト）の作成
    img = Image.new("RGB", (1024,1024),(255,255,255))
    # ImageDrawオブジェクトの作成
    draw = ImageDraw.Draw(img)

    # 直線の描画
    # draw.line([(0,1024), (1024,0)], fill = (0,0,255), width = 5)

    xy = []
    for i in range(n+1):
        theta = 360/n
        # print(str((i*m)%n))
        xy.append(img.width/2 + (img.width/4) * math.cos((i*m)%n * theta * math.pi / 180))  #x
        xy.append(img.height/2 + (img.height/4) * math.sin((i*m)%n * theta * math.pi / 180)) #y

    draw.point(xy, fill=(255,0,0))
    draw.line(xy, fill=(0,0,255), width= 5 , joint="curve")

    # 画像の保存
    img.save("image.png")

    # 画像の表示
    img.show()

if __name__ == "__main__":
    main()