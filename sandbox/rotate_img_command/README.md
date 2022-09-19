# 画像を時計周りに90度回転させる例
~~~bash
$ find -type f | grep jpg | xargs -i convert -rotate 90 {} {}
~~~