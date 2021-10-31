---
id: 14373
name: "w-bonelli/plant-image-analysis"
branch: "master"
tag: "latest"
commit: "af468abc6d6b92188a9a365c2dd96d48acbf4223"
version: "be42332c0902effe07302234074d9d53"
build_date: "2020-11-21T14:37:22.636Z"
size_mb: 1225.0
size: 557387807
sif: "https://datasets.datalad.org/shub/w-bonelli/plant-image-analysis/latest/2020-11-21-af468abc-be42332c/be42332c0902effe07302234074d9d53.sif"
url: https://datasets.datalad.org/shub/w-bonelli/plant-image-analysis/latest/2020-11-21-af468abc-be42332c/
recipe: https://datasets.datalad.org/shub/w-bonelli/plant-image-analysis/latest/2020-11-21-af468abc-be42332c/Singularity
collection: w-bonelli/plant-image-analysis
---

# w-bonelli/plant-image-analysis:latest

```bash
$ singularity pull shub://w-bonelli/plant-image-analysis:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
	Maintainer: Suxing Liu, Wes Bonelli

%post
	apt update && \
	apt install -y \
		build-essential \
		python3-setuptools \
		python3-pip \
		python3-numexpr \
		libgl1-mesa-glx \
		libsm6 \
		libxext6 \
		libfontconfig1 \
		libxrender1

	pip3 install --upgrade pip && \
	pip3 install numpy \
		Pillow \
		scipy \
		scikit-build \
		scikit-image \
		scikit-learn \
		matplotlib \
		opencv-python \
		openpyxl \
		seaborn \
		imutils && \
	pip3 install numpy --upgrade
	mkdir /lscratch /db /work /scratch
```

## Collection

 - Name: [w-bonelli/plant-image-analysis](https://github.com/w-bonelli/plant-image-analysis)
 - License: None

