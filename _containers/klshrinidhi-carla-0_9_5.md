---
id: 8901
name: "klshrinidhi/carla"
branch: "master"
tag: "0_9_5"
commit: "5218580f750409dd6d773de9ec276f6724d8563a"
version: "256089bcfaa97a788fa318b4338e7445"
build_date: "2019-05-08T15:10:10.733Z"
size_mb: 4448
size: 1338691615
sif: "https://datasets.datalad.org/shub/klshrinidhi/carla/0_9_5/2019-05-08-5218580f-256089bc/256089bcfaa97a788fa318b4338e7445.simg"
url: https://datasets.datalad.org/shub/klshrinidhi/carla/0_9_5/2019-05-08-5218580f-256089bc/
recipe: https://datasets.datalad.org/shub/klshrinidhi/carla/0_9_5/2019-05-08-5218580f-256089bc/Singularity
collection: klshrinidhi/carla
---

# klshrinidhi/carla:0_9_5

```bash
$ singularity pull shub://klshrinidhi/carla:0_9_5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get --yes update
	apt-get install --yes wget ffmpeg libjpeg-dev libsdl2-dev libosmesa6-dev \
			patchelf xvfb unzip zlib1g-dev x11vnc net-tools sudo
	useradd --no-create-home --groups sudo kowshika
	echo 'kowshika:kowshika' | chpasswd
	wget -q https://repo.continuum.io/archive/Anaconda2-2018.12-Linux-x86_64.sh
	bash Anaconda2-*.sh -b
	rm Anaconda2-*.sh
	export PATH="/root/anaconda2/bin:${PATH}"
	pip install --upgrade pip
	conda install --yes geos shapely pybind11 scikit-image pillow tqdm imageio \
		  pyopengl-accelerate
	conda install --yes -c conda-forge ipdb scipy fire opencv boost-cpp pyglet \
		  pyopengl
	conda install --yes -c CogSci pygame 
	conda clean --yes --all
    apt-get clean && rm -rf /var/lib/apt/lists/* &&  pip install tox 

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [klshrinidhi/carla](https://github.com/klshrinidhi/carla)
 - License: None

