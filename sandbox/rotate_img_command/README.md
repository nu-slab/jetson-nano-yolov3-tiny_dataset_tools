# 画像を時計周りに90度回転させる例
~~~bash
$ find -type f | grep jpg | xargs -i convert -rotate 90 {} {}
~~~

# shell script
~~~
# $ zsh script.sh sample output jpg
# $1 : input-dir
# $2 : output-dir
# $3 : img file type
~~~