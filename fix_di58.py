
# 修复 di-5.8 文件中的链接格式问题
file_path = r"c:\Users\ykla\Documents\FreeBSD-Ask\di-5-zhang-bao-guan-li-qi\di-5.8-jie-shi-yong-pkgbase-geng-xin.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换 &lt; 为 &lt; 和 &gt; 为 &gt;，但要小心只替换链接部分
# 第 621 行和第 622 行
old1 = '- FreeBSD Project. BootEnvironments[EB/OL]. [2026-03-25]. &lt;https://wiki.freebsd.org/BootEnvironments&gt;. FreeBSD 官方关于启动环境的 Wiki'
new1 = '- FreeBSD Project. BootEnvironments[EB/OL]. [2026-03-25]. &lt;https://wiki.freebsd.org/BootEnvironments&gt;. FreeBSD 官方关于启动环境的 Wiki'

old2 = '- FreeBSD Project. bectl(8)[EB/OL]. [2026-03-25]. &lt;https://man.freebsd.org/cgi/man.cgi?bectl&gt;. ZFS 启动环境管理工具的官方技术规范'
new2 = '- FreeBSD Project. bectl(8)[EB/OL]. [2026-03-25]. &lt;https://man.freebsd.org/cgi/man.cgi?bectl&gt;. ZFS 启动环境管理工具的官方技术规范'

modified = False

if old1 in content:
    content = content.replace(old1, new1)
    print("修复了第 1 个参考文献")
    modified = True

if old2 in content:
    content = content.replace(old2, new2)
    print("修复了第 2 个参考文献")
    modified = True

if modified:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已更新文件: {file_path}")
else:
    print("文件已经是正确格式，无需修改")
