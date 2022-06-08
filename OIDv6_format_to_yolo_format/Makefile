IN_DIR = '/home/users/yaraki/work/make_dataset/google-dataset/OIDv6/download_repo'
CLS_LIST = 'cls_list.txt'
## rename resize
convert: clean
	python yolo_convert.py --in_dir $(IN_DIR) --cls_list_file_name $(CLS_LIST) --resize_en --img_size 416 --rename_en

## rename
##convert: clean
##	python yolo_convert.py --in_dir $(IN_DIR) --cls_list_file_name $(CLS_LIST) --rename_en

clean:
	rm -rf ./output
	mkdir output
