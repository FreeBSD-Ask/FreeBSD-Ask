# 第五节 科研与专业工具

## 工具与软件

科学计算软件 GNU Octave： `#pkg install octave`

计算机代数系统 wxMaxima： `#pkg install wxmaxima`

Python 及其相关模块：

pyhton 安装：`#pkg install python`

模块安装：

```sh
#pkg install py38-scipy py38-pandas py38-matplotlib py38-sympy
```

或者

```sh
#pkg install py38-pip
pip install scipy
pip install pandas
pip install matplotlib
pip install sympy
```

## 统计学

## 分析学

## 统筹学

上一节我们使用 GLPK 求解线性规划问题，本节我们使用功能更为强大的 wxMaxima 来解决问题。以下代码仅供参考，想深入了解，可查看[官方文档](https://maxima.sourceforge.io/docs/manual/index.html)。

```maxima
load("simplex")$
maximize_lp(0.026 * x1 + 0.0509 * x2 + 0.0864 * x3 + 0.06875 * x4 + 0.78 * x5,
[x1 + x2 + x3 + x4 + x5 <= 1200,
x4 + x5 <= 0.4 * (x1 + x2 + x3 + x4 + x5),
x3 >= 0.5 * (x1 + x2 + x3),
0.1 * x1 + 0.07 * x2 + 0 * 03 * x3 + 0.05 * x4 + 0.02 * x5 <= 0.04 * (x1 + x2 + x3 + x4 + x5)]),
epsilon_lp = 0, nonnegative_lp = true; 
```
软件给出的答案为：`[436.608,[x5=480.0,x4=0,x3=720.0,x2=0,x1=0]]`，可知与 GLPK 求得的答案相同。问题解决。
