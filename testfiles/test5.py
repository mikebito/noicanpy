# -*- coding: utf-8 -*-
import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


a = 1     #振幅
fs = 96 * (10**3) #サンプリング周波数
f0 =  20 #周波数
sec = 0.005  #秒
tpi = 2 * np.pi
la = 10 #波長
T = 2 #周期
time = 1 #時刻

def _update(frame, x, y):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # データを更新 (追加) する
    x.append(frame)
    y.append(a * np.sin(2 * np.pi * (time / T - frame / la )))
    # 折れ線グラフを再描画する
    plt.plot(x, y)


def main():
    # 描画領域
    fig = plt.figure(figsize=(10, 6))
    # 描画するデータ (最初は空っぽ)
    x = []
    y = []

    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'fargs': (x, y),  # 関数の引数 (フレーム番号を除く)
        'interval': 10,  # 更新間隔 (ミリ秒)
        'frames': np.arange(0, 1000000, 0.1),  # フレーム番号を生成するイテレータ
        'repeat': False,  # 繰り返さない
    }
    anime = animation.FuncAnimation(**params)

    # グラフを表示する
    plt.show()


if __name__ == '__main__':
    main()