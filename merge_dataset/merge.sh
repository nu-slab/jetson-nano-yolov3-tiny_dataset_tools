#!/bin/bash
array=("test" "train" "valid")
array2=("images" "labels")

# マージ元のパス
ORI_PATH="/data/design_contest_dataset/tmp_2022_06_01_v2.1"
# マージ先のパス(このパスにあるデータセットが更新される)
MERGE_PATH="/data/design_contest_dataset/2022_06_06_v2.2"

for i in "${array[@]}"
do
cat ${ORI_PATH}/${i}.txt >> ${MERGE_PATH}/${i}.txt
    for j in "${array2[@]}"
    do
    cp -rf ${ORI_PATH}/${i}/${j}/* ${MERGE_PATH}/${i}/${j}/.
    done
done
