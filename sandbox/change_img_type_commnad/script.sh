# $ zsh script.sh sample output png jpg
# $1 : input-dir
# $2 : output-dir
# png -> jpg
# $3 : before file type
# $4 : after file type
I_PATH=$(cd $(dirname $1) && pwd)
I_NAME=$(basename $1)
I_FULL="$I_PATH/$I_NAME"
echo $I_NAME
echo $I_PATH
echo $I_FULL

O_PATH=$(cd $(dirname $2) && pwd)
O_NAME=$(basename $2)
O_FULL="$O_PATH/$O_NAME"
echo $O_NAME
echo $O_PATH
echo $O_FULL

for filepath in `find $I_FULL -type f | grep $3`
do
    TMP_FINE_NAME=$(basename $filepath)
    #echo $TMP_FINE_NAME | sed -e "s/$3/$4/g"
    TMP_FINE_NAME_OUT=`echo $TMP_FINE_NAME | sed -e "s/$3/$4/g"`
    echo $TMP_FINE_NAME "-->" $TMP_FINE_NAME_OUT
    convert $I_FULL/$TMP_FINE_NAME -quality 100 $O_FULL/$TMP_FINE_NAME_OUT
done

