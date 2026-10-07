"""演習01：1個のニューロンを動かす。

課題：下の examples の重みとバイアスを変え、ReLU の出力が0になる
組み合わせを2つ見つけよう。なぜ0になるか、式で説明しよう。
"""


def relu(value: float) -> float:
    return max(0.0, value)


def neuron(x: float, weight: float, bias: float) -> tuple[float, float]:
    z = x * weight + bias
    return z, relu(z)


examples = [
    (2.0, 0.7, 0.1),
    (-2.0, 0.7, 0.1),
    (2.0, -0.7, 0.1),
]

for x, weight, bias in examples:
    z, output = neuron(x, weight, bias)
    print(f"x={x:4.1f}, w={weight:4.1f}, b={bias:4.1f} → z={z:5.2f}, ReLU={output:5.2f}")
