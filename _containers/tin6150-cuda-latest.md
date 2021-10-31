---
id: 1160
name: "tin6150/cuda"
branch: "master"
tag: "latest"
commit: "3e88e471fcc7054a4a6867b9ba42778f6d413d66"
version: "42f01be831f681a8e3ed655f6068be61"
build_date: "2017-12-22T18:52:48.994Z"
size_mb: 2371
size: 1080889375
sif: "https://datasets.datalad.org/shub/tin6150/cuda/latest/2017-12-22-3e88e471-42f01be8/42f01be831f681a8e3ed655f6068be61.simg"
url: https://datasets.datalad.org/shub/tin6150/cuda/latest/2017-12-22-3e88e471-42f01be8/
recipe: https://datasets.datalad.org/shub/tin6150/cuda/latest/2017-12-22-3e88e471-42f01be8/Singularity
collection: tin6150/cuda
---

# tin6150/cuda:latest

```bash
$ singularity pull shub://tin6150/cuda:latest
```

## Singularity Recipe

```singularity
# Singularity container definition 
# Cuda 8.0 run time on CentOS 6
# 

# ref https://hub.docker.com/r/nvidia/cuda/
# ref https://gitlab.com/nvidia/cuda/blob/centos6/9.0/runtime/Dockerfile
# ref http://singularity-hub.org/containers/712


BootStrap: docker
From: nvidia/cuda:8.0-runtime-centos6
#From: nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04


%help
This container is a CentOS 6 with nvidia cuda runtime 

%runscript
	echo "zsh from inside the container..."
	/bin/zsh


%post
	#echo "Hello from inside the container"
	touch /THIS_IS_INSIDE_SINGULARITY
	yum -ty install vim bash zsh wget curl tar coreutils which util-linux-ng man \
			environment-modules telnet nc \
			ipmitool \
			pciutils \
			epel-release  # sl6 may need diff mech to enable epel
			#libpng libpng-devel libpng-static \
			#openmotif openmotif-devl openmotif22 \
			# telnet client for troubleshooting license manager connection

	yum -ty install dkms \
			cuda-nvidia-kmod-common nvidia-kmod \
			pcp-pmda-nvidia-gpu \
			xorg-x11-drv-nvidia xorg-x11-drv-nvidia-gl xorg-x11-drv-nvidia-devel \
		 	xorg-x11-drv-nvidia-libs 
			# xorg-x11-drv-nvidia-diagnostic  
			# nvidia-settings nvidia-uvm-kmod nvidia-xconfig nvidia-modprobe # obsolete
			#xorg-x11-drv-nvidia-libs-387.26-1
			# org-x11-drv-nvidia-libs should provide /usr/lib64/libcuda.so.1
			# from cuda repo ::
			# name=cuda
			# baseurl=http://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64
			# enabled=1
			# gpgcheck=1
			# gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA

	echo "end"                  >> /THIS_IS_INSIDE_SINGULARITY
	date                        >> /THIS_IS_INSIDE_SINGULARITY

%labels
MAINTAINER  Tin Ho tin'at'lbl.gov


## sudo    /opt/singularity-2.4.2/bin/singularity build -w ./perf_tools.simg ./Singularity
## sudo    /opt/singularity-2.4.2/bin/singularity build -w ./sl6_lbl.simg ./sl6_lbl.def
```

## Collection

 - Name: [tin6150/cuda](https://github.com/tin6150/cuda)
 - License: None

