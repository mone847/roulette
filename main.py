import random
from pyscript import document
from js import setTimeout

# 要素を取得
disp = document.getElementById("disp")
roullete = document.getElementById("roulette")

def start(event):
    # dispの前回内容の消去
    disp.innerHTML = ""
    # ルーレット画像の回転アニメーション開始
    roullete.style.animation = "spin 1s linear infinite"
    # 1秒後にslow1関数を呼び出す
    setTimeout(slow1, 1000)

def slow1():
    # ルーレット画像の回転アニメーションを少し遅くする
    roullete.style.animation = "spin 2s linear infinite"
    # 1秒後にslow2関数を呼び出す
    setTimeout(slow2, 1000)

def slow2():
    # ルーレット画像の回転アニメーションをさらに遅くする
    roullete.style.animation = "spin 4slinear infinite"
    # 1秒後に停止処理を呼び出す
    setTimeout(stop, 1000)

# ルーレット停止処理
def stop():
    # 0から36の乱数を得る
    r=random.randint(0, 36)
    # ルーレットの色判定
    if r == 0:
        color = "green"
    elif r % 2 == 0:
        color = "black"
    else:
        color = "red"
    #　id属性dispの取得
    disp = document.getElementById("disp")
    #　dispのテキスト更新
    disp.innerHTML = f"<div style='background-color:{color}'>{r}</div>"
    # ルーレット画像の回転アニメーション停止
    roullete.style.animation = "none"
