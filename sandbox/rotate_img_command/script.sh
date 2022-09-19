# $ zsh script.sh sample output jpg
# $1 : input-dir
# $2 : output-dir
# $3 : img file type
I_PATH=$(cd $(dirname $1) && pwd)
I_NAME=$(basename $1)
I_FULL="$I_PATH/$I_NAME"
#echo $I_NAME
#echo $I_PATH
#echo $I_FULL

O_PATH=$(cd $(dirname $2) && pwd)
O_NAME=$(basename $2)
O_FULL="$O_PATH/$O_NAME"
#echo $O_NAME
#echo $O_PATH
#echo $O_FULL

#for filepath in $I_FULL/*.jpg;
for filepath in `find $I_FULL -type f | grep $3`
do
    TMP_FINE_NAME=$(basename $filepath)
    echo $TMP_FINE_NAME
    convert -rotate 90 $I_FULL/$TMP_FINE_NAME $O_FULL/$TMP_FINE_NAME
done
