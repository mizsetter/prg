import tkinter as tk
import tkinter.ttk as ttk
import cv2
from PIL import Image, ImageTk

SPLIT_BLUE      = 1
SPLIT_GREEN     = 2
SPLIT_RED       = 3

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # フレーム
        self.frame_img = tk.Frame(self.master, bd = 2, relief = "ridge")
        self.frame_img.pack(side = "left", fill = "y")   # 左詰め、縦に広げる

        # メインのフレーム
        self.frame_main = tk.Frame(self.master)
        self.frame_main.pack(side = "left", fill = "y")  # 左詰め、縦に広げる

        # 画像表示
        self.frame_path = tk.Frame(self.frame_main)
        self.frame_path.pack(side = "top", fill = "x")  # 縦詰め、横に広げる

        # ラベル
        self.label_file_path = tk.Label(self.frame_path, text = u'パス：')
        self.label_file_path.pack(side = "left", anchor = "nw")

        # テキストボックス
        self.text_file_path = tk.Entry(self.frame_path, width = 50)
        self.text_file_path.insert(tk.END, 'G:\\python\\opencv\\o1080081114366959770.jpg')
        self.text_file_path.pack(side = "left", anchor = "nw")

        # ボタン
        self.button_file_path = tk.Button(self.frame_path, text = u'表示', command = self.btn_show_img)
        self.button_file_path.pack(side = "left", anchor = "nw")
        
        # グレースケールに変換
        self.frame_gray = tk.Frame(self.frame_main)
        self.frame_gray.pack(side = "top", fill = "x")  # 縦詰め、横に広げる

        self.label_gray = tk.Label(self.frame_gray, text = u'グレースケール：')
        self.label_gray.pack(side = "left", anchor = "nw")

        self.button_gray = tk.Button(self.frame_gray, text = u'変換', command = self.btn_gray)
        self.button_gray.pack(side = "left")

        # 色成分を取り出す
        self.frame_split = tk.Frame(self.frame_main)
        self.frame_split.pack(side = "top", fill = "x")  # 縦詰め、横に広げる

        self.label_split = tk.Label(self.frame_split, text = u'色成分の取り出し：')
        self.label_split.pack(side = "left", anchor = "nw")
        self.button_split_blue = tk.Button(self.frame_split, text = u'青成分', command = self.btn_split_blue)
        self.button_split_blue.pack(side = "left")
        self.button_split_green = tk.Button(self.frame_split, text = u'緑成分', command = self.btn_split_green)
        self.button_split_green.pack(side = "left")
        self.button_split_red = tk.Button(self.frame_split, text = u'赤成分', command = self.btn_split_red)
        self.button_split_red.pack(side = "left")

        # ぼかし処理
        self.frame_blur = tk.Frame(self.frame_main)
        self.frame_blur.pack(side = "top", fill = "x")  # 縦詰め、横に広げる

        self.label_blur = tk.Label(self.frame_blur, text = u'ぼかし処理(ブラー：平滑化)：')
        self.label_blur.pack(side = "left", anchor = "nw")
        self.button_blur = tk.Button(self.frame_blur, text = u'ブラー', command = self.btn_blur)
        self.button_blur.pack(side = "left")

        # 画像
        self.canvas = tk.Canvas(self.frame_img, height = 600, width = 800, bg = "black")
        self.canvas.pack()

    # 画像を読み込む
    def read_image(self):
        img_path = self.text_file_path.get()
        img_bgr = cv2.imread(img_path)

        return img_bgr

    # PhotoImageを取得
    def get_photoimage(self, img_rgb):
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        return img_tk

    # 画像を表示エリアに
    def show_image(self, img_tk):
        self.canvas.photo = img_tk
        self.canvas.create_image(0, 0, image = img_tk, anchor = 'nw')

    # 画像を表示
    def btn_show_img(self):
        # パスにある画像を読み込む
        img_bgr = self.read_image()

        # BGR ⇢ RGBに
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        # PhotoImageを取得
        img_tk = self.get_photoimage(img_rgb)

        # 画像を表示エリアに
        self.show_image(img_tk)

    # グレースケールに変換
    def btn_gray(self):
        # パスにある画像を読み込む
        img_bgr = self.read_image()

        # グレースケールに
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        # PhotoImageを取得
        img_tk = self.get_photoimage(img_rgb)

        # 画像を表示エリアに
        self.show_image(img_tk)

        # img_path = self.text_file_path.get()
        # img_bgr = cv2.imread(img_path)
        # img_pil = Image.fromarray(img_rgb)
        # img_tk = ImageTk.PhotoImage(img_pil)
        # self.canvas.photo = img_tk
        # self.canvas.create_image(0, 0, image = img_tk, anchor = 'nw')

    # 色成分の取り出し
    def split_image(self, img_bgr, split_color):
        blue, green, red = cv2.split(img_bgr)

        # 青成分
        if split_color == SPLIT_BLUE:
            return blue
        # 緑成分
        elif split_color == SPLIT_GREEN:
            return green
        # 赤成分
        else:
            return red
    # 青成分
    def btn_split_blue(self):
        # パスにある画像を読み込む
        img_bgr = self.read_image()

        # 色成分を取り出す
        img_blue = self.split_image(img_bgr, SPLIT_BLUE)

        # PhotoImageを取得
        img_tk = self.get_photoimage(img_blue)

        # 画像を表示エリアに
        self.show_image(img_tk)
    # 緑成分
    def btn_split_green(self):
        # パスにある画像を読み込む
        img_bgr = self.read_image()

        # 色成分を取り出す
        img_green = self.split_image(img_bgr, SPLIT_GREEN)

        # PhotoImageを取得
        img_tk = self.get_photoimage(img_green)

        # 画像を表示エリアに
        self.show_image(img_tk)
    # 赤成分
    def btn_split_red(self):
        # パスにある画像を読み込む
        img_bgr = self.read_image()

        # 色成分を取り出す
        img_red = self.split_image(img_bgr, SPLIT_RED)

        # PhotoImageを取得
        img_tk = self.get_photoimage(img_red)

        # 画像を表示エリアに
        self.show_image(img_tk)

    # ぼかし処理
    def btn_blur(self):
        # パスにある画像を読み込む
        img_bgr = self.read_image()

        # ぼかし処理(ブラー：平滑化)
        img_blur = cv2.blur(img_bgr, (5, 5))

        # PhotoImageを取得
        img_tk = self.get_photoimage(img_blur)

        # 画像を表示エリアに
        self.show_image(img_tk)

root = tk.Tk()
root.title(u"test")
root.geometry(str(1200) + "x" + str(600))
app = Application(master=root)
app.mainloop()