# 第一节 通过 freebsd-update 更新

>注意：只有一级架构的 release 版本才提供该源。也就是说 current 和 stable 是没有的。
关于架构的支持等级说明请看：
><https://www.freebsd.org/platforms>


> **前排提示**
>
>阿里云用户升级到 13.x 请看 第二章 第一节 “使用 virtio 技术半虚拟化的虚拟机” 部分。

## 更新系统

FreeBSD 提供了实用工具 `freebsd-update` 来安装系统更新，包括升级到大版本。

### 常规的安全更新：

```
# freebsd-update fetch
```
当出现类似于下列信息时：

```
usrlinclude/c++/vl/trllvector usrlinclude/c++/vl/trllversion usrlinclude/c++/v1/trl/wchar.h usr/include/c++/v1/tr1/wctype.h usrlinclude/c++/vllunwind-armh
usrlinclude/c++/v1/unwind-itaniumh usrlinclude/c++/vllunwindh
usr/include/crypto/ cryptodevh usrlinclude/crypto/cbcmac.h usr/include/crypto/deflate.h usrlinclude/crypto/gfmult.h usr/include/crypto/gmac.h
usr/include/crypto/rijndael.h usrlinclude/crypto/rmd160.h usr/include/crypto/xform.h
usr/include/crypto/xformauth.h usr/includecrypto/xformcomp.h usrlincludelcryptolxformenc.h
usr/include/crypto/xformpoly1305.h usrlincludelsys/ cscanatomic.h usrlincludelsys/ cscanbus.h usr/lib/clang/11.0.1
usr/lib/clang/11.0.1/include
:
```
 
你只需要输入`q`回车即可。然后：

```
# freebsd-update install
```

### 小版本或者大版本更新

> 例如 `13.1` 是要更新到的版本号：

```
# freebsd-update upgrade -r 13.1-RELEASE
```
当出现类似于下列信息时：

```
usrlinclude/c++/vl/trllvector usrlinclude/c++/vl/trllversion usrlinclude/c++/v1/trl/wchar.h usr/include/c++/v1/tr1/wctype.h usrlinclude/c++/vllunwind-armh
usrlinclude/c++/v1/unwind-itaniumh usrlinclude/c++/vllunwindh
usr/include/crypto/ cryptodevh usrlinclude/crypto/cbcmac.h usr/include/crypto/deflate.h usrlinclude/crypto/gfmult.h usr/include/crypto/gmac.h
usr/include/crypto/rijndael.h usrlinclude/crypto/rmd160.h usr/include/crypto/xform.h
usr/include/crypto/xformauth.h usr/includecrypto/xformcomp.h usrlincludelcryptolxformenc.h
usr/include/crypto/xformpoly1305.h usrlincludelsys/ cscanatomic.h usrlincludelsys/ cscanbus.h usr/lib/clang/11.0.1
usr/lib/clang/11.0.1/include
:
```
 
你只需要输入`q`回车即可。然后：

```
# freebsd-update install
```

安装后需要重启系统：

```
# reboot
```

然后再继续完成安装：

```
# freebsd-update install
```

## **故障排除**

### **FreeBSD 升级出错，没有 ntp 用户**

终端执行命令

```
# pw groupadd ntpd -g 123
# pw useradd ntpd -u 123 -g ntpd -h - -d /var/db/ntp -s /usr/sbin/nologin -c "NTP Daemon"
```
