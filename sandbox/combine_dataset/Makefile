IN_DIR = '/home/users/yaraki/work/make_dataset/git/design_contest_dataset_tools/OIDv6_format_to_yolo_format/output'
CLS_LIST = 'cls_list.txt'
FILE_TYPE = 'jpg'

convert: clean
	python combine.py --in_dir $(IN_DIR) --cls_list_file_name $(CLS_LIST) --file_type $(FILE_TYPE)


clean:
	rm -rf ./output
	mkdir ./output
	mkdir ./output/images
	mkdir ./output/labels
