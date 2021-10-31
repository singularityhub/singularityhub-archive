---
id: 9798
name: "szaman19/singularity_containers"
branch: "master"
tag: "latest"
commit: "adaba7c01ffc886e398eb74c20ce845833ef78ca"
version: "4712505afd8d41446f1e82a3d5db7a45"
build_date: "2019-06-14T05:35:10.329Z"
size_mb: 780
size: 253370399
sif: "https://datasets.datalad.org/shub/szaman19/singularity_containers/latest/2019-06-14-adaba7c0-4712505a/4712505afd8d41446f1e82a3d5db7a45.simg"
url: https://datasets.datalad.org/shub/szaman19/singularity_containers/latest/2019-06-14-adaba7c0-4712505a/
recipe: https://datasets.datalad.org/shub/szaman19/singularity_containers/latest/2019-06-14-adaba7c0-4712505a/Singularity
collection: szaman19/singularity_containers
---

# szaman19/singularity_containers:latest

```bash
$ singularity pull shub://szaman19/singularity_containers:latest
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
	pip3.6 install --no-cache-dir numpy
	
%environment 
	
%test
```

## Collection

 - Name: [szaman19/singularity_containers](https://github.com/szaman19/singularity_containers)
 - License: None

