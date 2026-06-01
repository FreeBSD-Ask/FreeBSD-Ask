import os

def replace_in_file(filepath, old, new):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old not in content:
        print(f"  [WARN] NOT FOUND: {repr(old[:60])}")
        return False
    content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f"  [OK] {repr(old[:40])} -> {repr(new[:40])}")
    return True

f1 = r'c:\Users\ykla\Documents\FreeBSD-Ask\hou-ji\wo-yu-freebsd-de-gu-shi.md'

# L15: 并没有 -> 并无, 然后 -> 随后
replace_in_file(f1,
    '去找 The C Programming Language 及其习题解答，但是很遗憾，并没有。这么多年过去了，我开始思索什么东西。Ubuntu Kylin 非常不稳定，于是我开始装原版 Ubuntu，然后我发现错怪了 Kylin，Ubuntu 也如此。',
    '去找 The C Programming Language 及其习题解答，但是很遗憾，并无。这么多年过去了，我开始思索什么东西。Ubuntu Kylin 非常不稳定，于是我开始装原版 Ubuntu，随后我发现错怪了 Kylin，Ubuntu 也如此。')

print("Done")