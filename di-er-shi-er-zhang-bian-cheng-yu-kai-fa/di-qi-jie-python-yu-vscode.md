# 第七节 Python 与 VScode

## Prerequisites

You may either choose to install binary packages, or build them from source from the ports system.
However, in this chapter we only introduce to you how to install the binary packages.

In order to utilize the package management system of FreeBSD, some manual set-ups is required. For details,
please refer to the Section 4, Chapter 3 of this book.

## Install Python on your FreeBSD system

In FreeBSD's official repo, Python is separately packaged for every different version. Doing so has several
advantages, for example, `powerline-status` is originally written with `python3.8` while other Python package is not.
Treating everyone has a dependency of `python3` or even `python` (yes, I'm bitching you, Arch Linux) is clearly problematic.

That being said, you can issue `pkg search python` to fetch a full list of Python versions currently available for FreeBSD.
For example, if you want to have the latest version of Python 3, simply issue:

```
# pkg install -y python311
```

## Install VSCode on your FreeBSD system

Before VSCode was brought to the ports system, and furtherer included in pkg repo, the user may either choose to build the
application from source if you want a native run, or utilize the linux kernel module to seek for compatible run. But luckily
for the new users, you don't have to do so any longer. Issue:

```
# pkg install -y vscode
```

and you are ready to roll.

Be advised, the one currently maintained in official repo is the OSS version of VSCode. Differences between this and the Microsoft-branded
release are not going to be detailed in this section, but just for a quick reference, both the MS C++ extension and MS SSH extension are
working fine on the OSS build, while setting sync service seems to be disabled.

