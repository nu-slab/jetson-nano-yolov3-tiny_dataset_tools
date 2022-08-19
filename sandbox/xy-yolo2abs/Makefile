IN_DIR = './sample'
IMG_TYPE = 'jpg'

xy2abs: clean
	python xy2abs.py --in_dir $(IN_DIR) --img_type $(IMG_TYPE)

clean:
	rm -rf ./output
	mkdir output
	mkdir output/images
	mkdir output/labels
