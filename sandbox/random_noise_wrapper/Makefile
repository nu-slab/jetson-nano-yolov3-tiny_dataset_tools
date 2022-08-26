DIR='./sample'
IMG_TYPE='jpg'
WIDTH_OF_CHANGE=0.9
SET_COUNT=3

all:clean
	python random_noise.py --dir $(DIR) --img_type $(IMG_TYPE) --width_of_change $(WIDTH_OF_CHANGE) --set_count $(SET_COUNT)

clean:
	rm -rf ./output
	mkdir ./output
