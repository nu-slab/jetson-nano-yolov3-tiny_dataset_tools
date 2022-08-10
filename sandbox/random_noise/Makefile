DIR='./sample'
IMG_TYPE='jpg'
WIDTH_OF_CHANGE=0.9
RENAME_STR='noise_0.9_'
color_jitter:clean
	python random_noise.py --dir $(DIR) --img_type $(IMG_TYPE) --width_of_change $(WIDTH_OF_CHANGE) --rename_str $(RENAME_STR) --color_jitter_en
random_equalize:clean
	python random_noise.py --dir $(DIR) --img_type $(IMG_TYPE) --width_of_change $(WIDTH_OF_CHANGE) --rename_str $(RENAME_STR) --random_equalize_en
random_auto_contrast:clean
	python random_noise.py --dir $(DIR) --img_type $(IMG_TYPE) --width_of_change $(WIDTH_OF_CHANGE) --rename_str $(RENAME_STR) --random_auto_contrast_en
clean:
	rm -rf ./output
	mkdir ./output
