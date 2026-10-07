"""演習02：1個のニューロンを勾配降下法で学習させる。

課題：LEARNING_RATE を 0.01 と 0.2 に変え、最終MSEを比較しよう。
なぜ更新の速さが変わるか、自分の言葉で説明しよう。
"""

DATA = [(-2, -3), (-1, -1), (0, 1), (1, 3), (2, 5)]  # 正解は y = 2x + 1
LEARNING_RATE = 0.05
STEPS = 100


def mse(weight: float, bias: float) -> float:
    return sum((weight * x + bias - y) ** 2 for x, y in DATA) / len(DATA)


weight = 0.0
bias = 0.0
for step in range(STEPS + 1):
    if step % 10 == 0:
        print(f"step={step:3d}  w={weight:7.4f}  b={bias:7.4f}  MSE={mse(weight, bias):9.6f}")
    if step == STEPS:
        break
    # MSEをwとbで微分した値。全データの平均を取る。
    gradient_w = sum(2 * (weight * x + bias - y) * x for x, y in DATA) / len(DATA)
    gradient_b = sum(2 * (weight * x + bias - y) for x, y in DATA) / len(DATA)
    weight -= LEARNING_RATE * gradient_w
    bias -= LEARNING_RATE * gradient_b
