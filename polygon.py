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
    n    = frac.numerator   #分子

    print("正\t"      + num                                            + "\t角形")
    print("頂点\t"    + str(n)                                         + "\t個")
    print("内角約\t"  + str( 180 * ( float(num) - 2.0 ) / float(num) ) + "\t度")

def poly_draw(num):
    frac = Fraction(num)
    n    = frac.numerator   #分子
    m    = frac.denominator #分母

    # カラーの画像データ（Imageオブジェクト）の作成
    img = Image.new("RGB", (1024,1024),(255,255,255))
    # ImageDrawオブジェクトの作成
    draw = ImageDraw.Draw(img)

    # 直線の描画
    # draw.line([(0,1024), (1024,0)], fill = (0,0,255), width = 5)

    # 円の中心と円周の半径
    cx = img.width  * 0.5
    cy = img.height * 0.5
    if( img.height < img.width ):
        r = img.height * 0.375
    else:
        r = img.width  * 0.375

    # 円周上に等間隔のn個の点をm個飛ばしてで打つ
    xy = []
    for i in range( n + 1 ):
        theta = 360 / n
        # print(str((i*m)%n))
        xy.append(cx + r * math.cos( ( i * m ) % n * theta * math.pi / 180 ) )  #x
        xy.append(cy + r * math.sin( ( i * m ) % n * theta * math.pi / 180 ) )  #y

    # draw.point(xy, fill=(255,0,0))
    # 点と点の間を線で結んでいく
    draw.line( xy , fill = ( 0 , 0 , 255 ) , width = 1 , joint = "curve" )

    # 画像の保存
    img.save("image.png")

    # 画像の表示
    img.show()


# 正n/m角形
# 1. 有理数（浮動小数点数ではなく文字列で受け取る）を分数の形に変換する
# 2.  n/m > 2 であるかの判定
# 3. 円周上に等間隔のn個の点を打つ
# 4. 今いる点とm個先の点を線で結ぶ（n回繰り返す）
def main():
    num = input_num()
    poly_info(num)
    poly_draw(num)



if __name__ == "__main__":
    main()
