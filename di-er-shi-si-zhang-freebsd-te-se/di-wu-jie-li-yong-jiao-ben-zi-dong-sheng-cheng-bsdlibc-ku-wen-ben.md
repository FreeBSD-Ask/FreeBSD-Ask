# 第五节 利用脚本自动生成 BSDlibc 库文本

>此部分来自 FreeBSD 论坛，作者 mrclksr。原文地址 <https://forums.freebsd.org/threads/wheres-bsd-libc-documentation.63107/>。


首先安装依赖：

```
# pkg install  netpbm groff ghostscript9-base
```

```
#!/bin/sh

pstarget="/tmp/$$.libcdoc.ps"
pdftarget="libcdoc.pdf"
pdftarget_noidx="/tmp/$$.$pdftarget"
pdfindex="/tmp/$$.pdfindex.info"
index="/tmp/$$.index"
sorted_index="$index.sorted"
flist="/tmp/$$.flist"
tocin="/tmp/$$.toc.mdoc"
keywords="/tmp/$$.keywords"
mandir="/usr/share/man"
paths="$mandir/man2 $mandir/man3"
content_offset=0

mkidx()
{
   for i in `find $paths -name "*.gz"`; do
       if zgrep -q '.Lb libc' $i && zgrep -q '.Sh LIBRARY' $i; then
           for j in `gettitles $i`; do
               echo "$j:$i" >> $index
           done
       fi
   done
   cat $index | sort -n | uniq | awk -F: 'BEGIN { prev = "" } {
       if ($1 != prev) {
           print $0;
       }
       prev = $1;
   }' > $index.tmp
   mv $index.tmp $index

   for i in `cat $index`; do
       fname=`echo $i | cut -d: -f2`
       grep $fname $index | sort -n | awk -F: 'BEGIN {n = 0} {
           if (n++ > 0)
               printf ",";
           printf "%s", $1;
       }'
       echo ":$fname"
   done | sort -n | uniq > $index.tmp
   mv $index.tmp $index

   currp=1
   for i in `cat $index`; do
       fname=`echo $i  | cut -d: -f2`
       kwords=`echo $i | cut -d: -f1`
       nextp=`mandoc -T ps $fname|egrep '%%Pages: [0-9]+'|cut -d: -f2`
       echo "$kwords:$currp:$fname" >> $index.tmp
       currp=`expr $currp + $nextp`
   done
   mv $index.tmp $index
   for i in `cat $index | sed -E 's/(^[^:]+):.*/1/' | tr ',' ' '`; do
       echo $i
   done | sort -n > $keywords
   
   for i in `cat $keywords`; do
       page=`grep -w $i $index | tail -1 | cut -d: -f 2`
       echo $i:$page
   done > $sorted_index
}

mkpsdoc()
{
   for i in `cat $index`; do
       fname=`echo $i | cut -d: -f3`
       zcat $fname | sed -e 's/^.Dd.*$/.Dd __PAGENO__/' 
                 -e '/.Os.*/d' | mandoc -T ps >> $pstarget
   done
}

mktoc()
{
   echo ".XS 1" > $tocin
   echo "Table of Contents" >> $tocin
   for i in `cat $sorted_index`; do
       kword=`echo $i | cut -d: -f 1`
       page=`echo $i | cut -d: -f 2`
       page=`expr $content_offset + $page`
       printf ".XA $pagen$kwordn" >> $tocin
   done
   echo ".XE" >> $tocin
   echo ".PX" >> $tocin
}

get_content_offset()
{
   mktoc
   content_offset=`groff -T ps -ms $tocin | egrep '%%Pages: [0-9]+' | 
       cut -d: -f2`
   content_offset=`expr $content_offset + 0`
}

prepend_toc()
{
   in=$1
   tmp=$in.tmp

   groff -T ps -ms $tocin > $tmp
   cat $in >> $tmp
   mv $tmp $in
}

mkpdfidx()
{
   printf "[/Page 1 /View [/XYZ null null null] " > $pdfindex
   printf "/Title (Table of Contents) /OUT pdfmarkn" >> $pdfindex

   for i in `cat $sorted_index`; do
       kword=`echo $i | cut -d: -f 1`
       page=`echo $i | cut -d: -f 2`
       page=`expr $page + $content_offset`
       printf "[/Page $page /View "       >> $pdfindex
       printf "[/XYZ null null null] "       >> $pdfindex
       printf "/Title ($kword) /OUT pdfmarkn" >> $pdfindex
   done
}

gettitles()
{
   zcat $1 | sed -n '/.Sh NAME/,/.Sh LIBRARY/p' | 
       egrep '^.Nm [^ ]+' | cut -d" " -f 2 | sort -n | uniq
}

mkidx
mkpsdoc
get_content_offset
mktoc
prepend_toc $pstarget
mkpdfidx

cat $pstarget | awk -v p=$content_offset '{
   if ($0 ~ /(__PAGENO__)/) {
        t = sprintf("(%s)", ++p);
        sub(/(__PAGENO__)/, t);
   }
   print $0;
 }' > $pstarget.tmp

mv $pstarget.tmp $pstarget

ps2pdf $pstarget $pdftarget_noidx

gs -sDEVICE=pdfwrite -q -dBATCH -dNOPAUSE -sOutputFile=$pdftarget $pdfindex 
   -f $pdftarget_noidx

rm -f $tocin
rm -f $pstarget
rm -f $index
rm -f $pdftarget_noidx
rm -f $pdfindex
rm -f $sorted_index
```

运行脚本即可在同路径文件夹下找到 PDF 文档。现成的文档请看：

<https://github.com/FreeBSD-Ask/BSDlibc>
