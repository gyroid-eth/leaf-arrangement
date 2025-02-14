import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Phyllotaxis Pattern Simulation")

# データポイント数（葉の数）をスライダーで指定（10～1000、初期値200）
n_points = st.slider("Number of data points (leaves)", min_value=10, max_value=1000, value=200, step=10)

# ハイライトする螺旋の数をスライダーで指定（1～300、初期値34）
num_spirals = st.slider("Number of spirals", min_value=1, max_value=300, value=34, step=1)

# データポイントの大きさをスライダーで指定（10～500、初期値300）
point_size = st.slider("Data point size", min_value=10, max_value=500, value=300, step=10)

# 黄金角（約137.5°）をラジアンに変換
golden_angle = np.deg2rad(137.5)

# 1からn_pointsまでの整数配列（各葉を表す）
n = np.arange(1, n_points + 1)

# 葉の半径: √nを使うことで自然な螺旋形状に
r = np.sqrt(n)

# 各点の角度: 黄金角を用いる
theta = n * golden_angle

# 極座標をデカルト座標に変換
x = r * np.cos(theta)
y = r * np.sin(theta)

# 螺旋ごとのグループ化
spirals = [[] for _ in range(num_spirals)]
for i in range(n_points):
    spirals[i % num_spirals].append(i)

# 螺旋の色を定義
colors = plt.cm.tab10(np.linspace(0, 1, num_spirals))

# 図の作成
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x, y, s=point_size, color='gray', alpha=0.3)  # データポイントのサイズをpoint_sizeに変更

# 各点に番号を表示
for i in range(n_points):
    ax.text(x[i], y[i], str(i+1), fontsize=6, ha='center', va='center', color='black')

# 螺旋を描画
for i, indices in enumerate(spirals):
    ax.plot([x[j] for j in indices], [y[j] for j in indices],
            color=colors[i % len(colors)], linewidth=1.5, alpha=0.5)

ax.set_title("Fibonacci Spirals in a Phyllotaxis Pattern")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.axis("equal")
ax.grid(True)

# Streamlit上に図を表示
st.pyplot(fig)
