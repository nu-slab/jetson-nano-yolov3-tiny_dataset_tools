IN_DIR = 'sample'
CLS_CHANGE_LIST = 'cls_change_list.txt'

convert: clean
	python change_class.py --in_dir $(IN_DIR) --cls_change_list_file_name $(CLS_CHANGE_LIST)

clean:
	rm -rf ./output
	mkdir output
