"""演習03：隠れ層のあるネットワークで XOR を学ぶ。

Python標準ライブラリだけを使用。構造は 2入力 → 4個の隠れニューロン → 1出力。
課題：HIDDEN を 1 または 2 に変え、同じ学習回数で結果を比べよう。
結果が変わらない・悪化する場合もあります。初期値と学習回数を記録しよう。
"""

import math
import random

random.seed(7)
DATA = [([0.0, 0.0], 0.0), ([0.0, 1.0], 1.0), ([1.0, 0.0], 1.0), ([1.0, 1.0], 0.0)]
HIDDEN = 4
LEARNING_RATE = 0.5
EPOCHS = 10000


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


weights1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(HIDDEN)]
bias1 = [0.0] * HIDDEN
weights2 = [random.uniform(-1, 1) for _ in range(HIDDEN)]
bias2 = 0.0


def forward(inputs: list[float]) -> tuple[list[float], float]:
    hidden = [sigmoid(sum(w * x for w, x in zip(row, inputs)) + b) for row, b in zip(weights1, bias1)]
    output = sigmoid(sum(w * h for w, h in zip(weights2, hidden)) + bias2)
    return hidden, output


for epoch in range(EPOCHS):
    for inputs, target in DATA:
        hidden, output = forward(inputs)
        # 二乗誤差に対する出力層と隠れ層の勾配（逆伝播）。
        delta2 = 2 * (output - target) * output * (1 - output)
        delta1 = [delta2 * weights2[i] * hidden[i] * (1 - hidden[i]) for i in range(HIDDEN)]
        for i in range(HIDDEN):
            weights2[i] -= LEARNING_RATE * delta2 * hidden[i]
            for j in range(2):
                weights1[i][j] -= LEARNING_RATE * delta1[i] * inputs[j]
            bias1[i] -= LEARNING_RATE * delta1[i]
        bias2 -= LEARNING_RATE * delta2
    if epoch in (0, 99, 999, EPOCHS - 1):
        loss = sum((forward(inputs)[1] - target) ** 2 for inputs, target in DATA) / len(DATA)
        print(f"epoch={epoch + 1:5d}  MSE={loss:.6f}")

print("入力 → 予測 (正解)")
for inputs, target in DATA:
    print(f"{inputs} → {forward(inputs)[1]:.3f} ({target:.0f})")
