---
id: 4027
name: "colinsauze/xkcd1425-with-yolo"
branch: "master"
tag: "gpu"
commit: "9b02ee8833e4195537d9503d1c04d3a0b3911be2"
version: "65aa03e551e1aadd8cc5cb14fa305568"
build_date: "2021-02-26T12:35:05.157Z"
size_mb: 2865
size: 1713102879
sif: "https://datasets.datalad.org/shub/colinsauze/xkcd1425-with-yolo/gpu/2021-02-26-9b02ee88-65aa03e5/65aa03e551e1aadd8cc5cb14fa305568.simg"
url: https://datasets.datalad.org/shub/colinsauze/xkcd1425-with-yolo/gpu/2021-02-26-9b02ee88-65aa03e5/
recipe: https://datasets.datalad.org/shub/colinsauze/xkcd1425-with-yolo/gpu/2021-02-26-9b02ee88-65aa03e5/Singularity
collection: colinsauze/xkcd1425-with-yolo
---

# colinsauze/xkcd1425-with-yolo:gpu

```bash
$ singularity pull shub://colinsauze/xkcd1425-with-yolo:gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-devel

%help
    Container for XKCD 1425 with Yolo demo using a GPU.
    To install run: 
	sudo singularity build xkcd1425.img Singularity
    To run (replace /home/user/output_images with the directory where you want the output and /home/user/input_images with the directory containing the images you want to process)
	singularity run --nv -B /home/user/input_images:/opt/xkcd1425-with-yolo/test_images,/home/user/output_images:/opt/xkcd1425-with-yolo/output_images xkcd1425.img

%labels
    MAINTAINER Colin Sauze

%environment


%post  
    pwd
    apt-get update
    apt-get -y install unzip wget build-essential git gdal-bin python-numpy python-opencv python-matplotlib python-matplotlib-data python-mpltoolkits.basemap python-mpltoolkits.basemap-data python-pil python-shapely python-pyshp

    mkdir /usr/lib/nvidia
    apt-get -y install libcuda1-390

    cd /opt
    if [ ! -d "xkcd1425-with-yolo" ] ; then
	git clone https://github.com/colinsauze/xkcd1425-with-yolo.git
	cd xkcd1425-with-yolo
	#git checkout test
	#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
	./setup.sh

	#rebuild with GPU support
        cd darknet
	sed -i 's/GPU=0/GPU=1/1' Makefile
	sed -i 's/NVCC=nvcc/NVCC=\/usr\/local\/cuda\/bin\/nvcc/' Makefile
        make
	cd ..

	chmod 777 output_images
        #delete the example output images	
        rm output_images/*

	#we don't actually need the cuda libraries and the gigabyte of dependencies they installed if we run the container with the --nv option.
	apt-get -y purge libcuda1-390
	apt-get -y clean
	apt-get -y autoclean
	apt-get -y --purge autoremove

    fi


%runscript
    cd /opt/xkcd1425-with-yolo
    python detector.py
```

## Collection

 - Name: [colinsauze/xkcd1425-with-yolo](https://github.com/colinsauze/xkcd1425-with-yolo)
 - License: [MIT License](https://api.github.com/licenses/mit)

