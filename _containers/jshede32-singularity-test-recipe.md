---
id: 8016
name: "jshede32/singularity-test"
branch: "master"
tag: "recipe"
commit: "ac38a1bf6aec0ceccdb5accfb807ace1a9b9a435"
version: "57281986b74d91eb81cf60c08a76b123"
build_date: "2019-03-28T19:02:13.907Z"
size_mb: 3074
size: 1411510303
sif: "https://datasets.datalad.org/shub/jshede32/singularity-test/recipe/2019-03-28-ac38a1bf-57281986/57281986b74d91eb81cf60c08a76b123.simg"
url: https://datasets.datalad.org/shub/jshede32/singularity-test/recipe/2019-03-28-ac38a1bf-57281986/
recipe: https://datasets.datalad.org/shub/jshede32/singularity-test/recipe/2019-03-28-ac38a1bf-57281986/Singularity
collection: jshede32/singularity-test
---

# jshede32/singularity-test:recipe

```bash
$ singularity pull shub://jshede32/singularity-test:recipe
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: marcc-hpc/tensorflow:1.8.0-gpu


%post
	su
	apt-get install sudo
	exit
	sudo apt-get install vim
	sudo apt-get install git
	sudo apt-get install wget
	sudo apt-get install ffmpeg
	pip install pymongo
	pip install geopy
	pip install pandas
	pip install keras
	pip install PIL
	pip install numpy
	pip install scipy
	pip install azure
	pip install python-opencv
	wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
	wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb
	wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb
	wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl2_2.1.4-1+cuda9.0_amd64.deb
	wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl-dev_2.1.4-1+cuda9.0_amd64.deb
	sudo dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
	sudo dpkg -i libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb
	sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb
	sudo dpkg -i libnccl2_2.1.4-1+cuda9.0_amd64.deb
	sudo dpkg -i libnccl-dev_2.1.4-1+cuda9.0_amd64.deb
	sudo apt-get update
	sudo apt-get install cuda=9.0.176-1
	sudo apt-get install libcudnn7-dev
	sudo apt-get install libnccl-dev
	export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
	export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
	sudo apt-get install build-essential
	sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
	sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
	git clone https://github.com/opencv/opencv.git
	cd opencv/
	git checkout 3.4.0
	cd ..
	git clone https://github.com/opencv/opencv_contrib.git
	cd opencv_contrib/
	git checkout 3.4.0
	cd ../opencv/
	mkdir build
	cd build
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
		-D CMAKE_INSTALL_PREFIX=/usr/local \
		-D INSTALL_PYTHON_EXAMPLES=ON \
		-D INSTALL_C_EXAMPLES=OFF \
		-D CMAKE_LIBRARY_PATH=/usr/local/cuda/lib64/stubs \
		-D OPENCV_ENABLE_NONFREE=ON \
		-D ENABLE_FAST_MATH=ON \
		-D CUDA_FAST_MATH=ON \
		-D CUDA_GENERATION=Pascal \
		-D WITH_FFMPEG=1 \
		-D WITH_CUDA=ON \
		-D WITH_CUBLAS=1 \
		-D WITH_OPENGL=ON \
		-D WITH_TBB=ON \
		-D WITH_LAPACK=OFF \
		-D OPENCV_EXTRA_MODULES_PATH="../../opencv_contrib/modules" \
		-D PYTHON3_EXECUTABLE=$(which python) \
		-D BUILD_EXAMPLES=ON ..
	make -j4
	sudo make install
```

## Collection

 - Name: [jshede32/singularity-test](https://github.com/jshede32/singularity-test)
 - License: None

