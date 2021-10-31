---
id: 3406
name: "colinsauze/xkcd1425-with-yolo"
branch: "master"
tag: "latest"
commit: "9b02ee8833e4195537d9503d1c04d3a0b3911be2"
version: "ad085cd0192a5888e12e605fe192d533"
build_date: "2018-08-17T18:19:55.217Z"
size_mb: 1567
size: 806219807
sif: "https://datasets.datalad.org/shub/colinsauze/xkcd1425-with-yolo/latest/2018-08-17-9b02ee88-ad085cd0/ad085cd0192a5888e12e605fe192d533.simg"
url: https://datasets.datalad.org/shub/colinsauze/xkcd1425-with-yolo/latest/2018-08-17-9b02ee88-ad085cd0/
recipe: https://datasets.datalad.org/shub/colinsauze/xkcd1425-with-yolo/latest/2018-08-17-9b02ee88-ad085cd0/Singularity
collection: colinsauze/xkcd1425-with-yolo
---

# colinsauze/xkcd1425-with-yolo:latest

```bash
$ singularity pull shub://colinsauze/xkcd1425-with-yolo:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:bionic

%help
    Container for XKCD 1424 with Yolo demo. 
    To install run: 
	sudo singularity build xkcd1425.img Singularity
    To run (replace /home/user/output_images with the directory where you want the output and /home/user/input_images with the directory containing the images you want to process)
	singularity run -B /home/user/input_images:/opt/xkcd1425-with-yolo/test_images,/home/user/output_images:/opt/xkcd1425-with-yolo/output_images xkcd1425.img

%labels
    MAINTAINER Colin Sauze

%environment


%post  
    pwd
    apt-get update
    apt-get -y install unzip wget build-essential git gdal-bin python-numpy python-opencv python-matplotlib python-matplotlib-data python-mpltoolkits.basemap python-mpltoolkits.basemap-data python-pil python-shapely 

    cd /opt
    git clone https://github.com/colinsauze/xkcd1425-with-yolo.git
    cd xkcd1425-with-yolo
    ./setup.sh

    chmod 777 output_images
    #delete the example output images
    rm output_images/*

%runscript
    cd /opt/xkcd1425-with-yolo
    python detector.py
```

## Collection

 - Name: [colinsauze/xkcd1425-with-yolo](https://github.com/colinsauze/xkcd1425-with-yolo)
 - License: [MIT License](https://api.github.com/licenses/mit)

