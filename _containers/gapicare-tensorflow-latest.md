---
id: 6168
name: "gapicare/tensorflow"
branch: "master"
tag: "latest"
commit: "b99e7f570092c0ddd4ea11e92199b363aee22300"
version: "439f2f70dca02ca8d76a89d6b81809b4"
build_date: "2019-01-22T21:59:06.281Z"
size_mb: 2628
size: 1262026783
sif: "https://datasets.datalad.org/shub/gapicare/tensorflow/latest/2019-01-22-b99e7f57-439f2f70/439f2f70dca02ca8d76a89d6b81809b4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gapicare/tensorflow/latest/2019-01-22-b99e7f57-439f2f70/
recipe: https://datasets.datalad.org/shub/gapicare/tensorflow/latest/2019-01-22-b99e7f57-439f2f70/Singularity
collection: gapicare/tensorflow
---

# gapicare/tensorflow:latest

```bash
$ singularity pull shub://gapicare/tensorflow:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-base-ubuntu16.04

%environment
	export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
	export PATH=/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:
	export LC_ALL=C

%post
	apt-get update && apt-get install -y --no-install-recommends \
		build-essential \
		cuda-command-line-tools-9-0 \
		cuda-cublas-9-0 \
		cuda-cufft-9-0 \
		cuda-curand-9-0 \
		cuda-cusolver-9-0 \
		cuda-cusparse-9-0 \
		curl \
		libcudnn7=7.2.1.38-1+cuda9.0 \
		libncc12=2.2.13-1+cuda9.0 \
		libfreetype6-dev \
		libhdf5-serial-dev \
		libpng12-dev \
		libzmq3-dev \
		pkg-config \
		python \
		python-dev \
		python3 \
		python3-dev \
		rsync \
		software-properties-common \
		unzip \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

	apt-get update && \
	apt-get install nvinfer-runtime-trt-repo-ubuntu1604-4.0.1-ga-cuda9.0 && \
	apt-get update && \
	apt-get install -y libnvinfer4=4.1.2-1+cuda9.0

	apt-get install -y python3-pip

	pip3 --no-cache-dir install \
		Pillow \
		h5py \
		ipykernel \
		jupyter \
		keras_applications \
		keras_preprocessing \
		matplotlib \
		numpy \
		pandas \
		scipy \
		sklearn

	pip3 install tensorflow-gpu==1.10.1
	pip3 install keras==2.1.6
```

## Collection

 - Name: [gapicare/tensorflow](https://github.com/gapicare/tensorflow)
 - License: None

