---
id: 9799
name: "szaman19/singularity_containers"
branch: "master"
tag: "tensorflow"
commit: "8c0117223d50cb4880908fbb3ee936c9cfa91001"
version: "6d46a69b5afcf882d093f58b75da14ea"
build_date: "2019-06-14T05:36:18.368Z"
size_mb: 1224
size: 357216287
sif: "https://datasets.datalad.org/shub/szaman19/singularity_containers/tensorflow/2019-06-14-8c011722-6d46a69b/6d46a69b5afcf882d093f58b75da14ea.simg"
url: https://datasets.datalad.org/shub/szaman19/singularity_containers/tensorflow/2019-06-14-8c011722-6d46a69b/
recipe: https://datasets.datalad.org/shub/szaman19/singularity_containers/tensorflow/2019-06-14-8c011722-6d46a69b/Singularity
collection: szaman19/singularity_containers
---

# szaman19/singularity_containers:tensorflow

```bash
$ singularity pull shub://szaman19/singularity_containers:tensorflow
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7


%post 
	yum -y update
	yum -y install yum-utils
	yum -y groupinstall development
	yum -y install https://centos7.iuscommunity.org/ius-release.rpm
	yum -y install python36u
	yum -y install python36u-devel
	yum -y install python36u-pip	
	echo "Installed system dependencies"
	
	pip3.6 install --upgrade pip	
	pip3.6 install --no-cache-dir numpy tensorflow
	
%environment 
	
%test
```

## Collection

 - Name: [szaman19/singularity_containers](https://github.com/szaman19/singularity_containers)
 - License: None

