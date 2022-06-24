# 第一节 安装 Xorg

## 安装xorg 

### 可选包：

xorg 完整包: xorg 

xorg 最小化包: org-minimal（不建议）

### 安装

通过pkg安装

`# pkg install xorg`

通过ports安装

```
# cd /usr/ports/x11/xorg
# make install clean
```


## 故障排除

**总有人试图手动生成`xorg.conf`这个文件，这是非常错误的行为！你打不开桌面很大概率不是因为这个文件的配置有问题！你应该去检查显卡驱动或者桌面本身的问题。Xorg 几乎是不会出问题的！**
