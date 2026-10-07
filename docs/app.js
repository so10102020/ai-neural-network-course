const $ = (id) => document.getElementById(id);
const inputs = ['x', 'w', 'b'];
function updateNeuron() {
  const values = Object.fromEntries(inputs.map((id) => [id, Number($(id).value)]));
  inputs.forEach((id) => { $(`${id}-value`).textContent = values[id].toFixed(1); });
  const z = values.x * values.w + values.b;
  const a = Math.max(0, z);
  $('formula').textContent = `${values.x.toFixed(1)} × ${values.w.toFixed(1)} + ${values.b.toFixed(1)} = ${z.toFixed(2)}`;
  $('activation').textContent = `ReLU を通した出力：${a.toFixed(2)}`;
  $('meter').style.width = `${Math.min(100, a / 10 * 100)}%`;
}
inputs.forEach((id) => $(id).addEventListener('input', updateNeuron));
updateNeuron();

const points = [-2, -1, 0, 1, 2].map((x) => ({ x, y: 2 * x + 1 }));
let weight = 0;
let bias = 0;
function mse() { return points.reduce((sum, p) => sum + (weight * p.x + bias - p.y) ** 2, 0) / points.length; }
function renderTraining() {
  $('train-params').textContent = `重み w = ${weight.toFixed(3)} / バイアス b = ${bias.toFixed(3)}`;
  $('train-loss').textContent = `平均二乗誤差（MSE） = ${mse().toFixed(3)}`;
  const toX = (x) => 160 + x * 55;
  const toY = (y) => 115 - y * 19;
  const target = points.map((p) => `<circle cx="${toX(p.x)}" cy="${toY(p.y)}" r="5" fill="#16997e"/>`).join('');
  const prediction = points.map((p) => `${toX(p.x)},${toY(weight * p.x + bias)}`).join(' ');
  $('train-chart').innerHTML = `<line x1="30" y1="115" x2="290" y2="115" class="axis"/><line x1="160" y1="15" x2="160" y2="215" class="axis"/><text x="294" y="119">x</text><text x="165" y="17">y</text><polyline points="${prediction}" fill="none" stroke="#e97742" stroke-width="3" stroke-linecap="round"/>${target}`;
}
function train() {
  const gradientW = points.reduce((sum, p) => sum + 2 * (weight * p.x + bias - p.y) * p.x, 0) / points.length;
  const gradientB = points.reduce((sum, p) => sum + 2 * (weight * p.x + bias - p.y), 0) / points.length;
  weight -= 0.05 * gradientW;
  bias -= 0.05 * gradientB;
  renderTraining();
}
$('train-step').addEventListener('click', train);
$('train-ten').addEventListener('click', () => { for (let i = 0; i < 10; i++) train(); });
$('train-reset').addEventListener('click', () => { weight = 0; bias = 0; renderTraining(); });
renderTraining();
