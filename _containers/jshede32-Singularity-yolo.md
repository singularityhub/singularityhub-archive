---
id: 6584
name: "jshede32/Singularity"
branch: "master"
tag: "yolo"
commit: "726b5db20498fab3734c6694d18e3d84d87bbe7d"
version: "3c29136da02941209736d414717a363a"
build_date: "2019-01-26T22:48:03.223Z"
size_mb: 3736
size: 1778446367
sif: "https://datasets.datalad.org/shub/jshede32/Singularity/yolo/2019-01-26-726b5db2-3c29136d/3c29136da02941209736d414717a363a.simg"
url: https://datasets.datalad.org/shub/jshede32/Singularity/yolo/2019-01-26-726b5db2-3c29136d/
recipe: https://datasets.datalad.org/shub/jshede32/Singularity/yolo/2019-01-26-726b5db2-3c29136d/Singularity
collection: jshede32/Singularity
---

# jshede32/Singularity:yolo

```bash
$ singularity pull shub://jshede32/Singularity:yolo
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: caffe2/caffe2:snapshot-py2-cuda9.0-cudnn7-ubuntu16.04
  %labels
       MAINTAINER Jacob Shedenhelm jshede@iastate.edu
   %post
		
		sudo apt-get install python-opencv

       echo "Cloning Darknet"
       git clone https://github.com/pjreddie/darknet
       cd darknet
       # update darknet makefile to use correct specifications
       sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/1' Makefile
       sed -i 's/GPU=0/GPU=1/1' Makefile
       sed -i 's/OPENCV=0/OPENCV=1/1' Makefile
       sed -i 's/CUDNN=0/CUDNN=1/1' Makefile
       sed -i 's/DEBUG=0/DEBUG=1/1' Makefile
       sed -i 's/OPENMP=0/OPENMP=1/1' Makefile
       make
       cd ..
       echo "Deleting the example output images darknet provides"
       chmod 777 output_images
       rm -rf output_images
```

## Collection

 - Name: [jshede32/Singularity](https://github.com/jshede32/Singularity)
 - License: None

