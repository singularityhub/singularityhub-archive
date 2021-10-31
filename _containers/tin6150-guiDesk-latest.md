---
id: 13618
name: "tin6150/guiDesk"
branch: "master"
tag: "latest"
commit: "90837c31c21bbd5c44530a2e44f03b8fe283aa03"
version: "483b0f2caeaea5c944c3b28356c46cf11274b62b78624538bc079cc97a923f27"
build_date: "2020-07-18T01:18:23.519Z"
size_mb: 486.7109375
size: 510353408
sif: "https://datasets.datalad.org/shub/tin6150/guiDesk/latest/2020-07-18-90837c31-483b0f2c/483b0f2caeaea5c944c3b28356c46cf11274b62b78624538bc079cc97a923f27.sif"
url: https://datasets.datalad.org/shub/tin6150/guiDesk/latest/2020-07-18-90837c31-483b0f2c/
recipe: https://datasets.datalad.org/shub/tin6150/guiDesk/latest/2020-07-18-90837c31-483b0f2c/Singularity
collection: tin6150/guiDesk
---

# tin6150/guiDesk:latest

```bash
$ singularity pull shub://tin6150/guiDesk:latest
```

## Singularity Recipe

```singularity
# Singularity container definition for 
# guiDesk
# lightweight gui desktop (file manager, browser)
# centos  7 
# https://github.com/tin6150/guiDesk
# https://singularity-hub.org/collections/4551


BootStrap: docker
#From: centos:7.6.1810
From: centos:7
#From: centos:8

%help
	This container is a CentOS  with a light GUI desktop (file manager, firefox)
  Pull and run via singularity hub:
	singularity pull --name guiDesk.sif shub://tin6150/guiDesk
	Then run one of these commands:
	singularity exec guiDesk.sif thunar    # xfce file manager
	singularity exec guiDesk.sif ristretto # simple picture viewer
	singularity exec guiDesk.sif mousepad  # simple text editor


# copy files into the container 
# https://singularity.lbl.gov/docs-recipes#:~:text=If%20you%20want%20to%20copy,a%20path%20in%20the%20container.
# no destination means /
%files
	add_package.sh 

%runscript
	#echo "vim from inside the container..."
	xfe "$@"


%post
	#echo "Hello from inside the container"
	touch /THIS_IS_INSIDE_SINGULARITY
	#yum -ty update 
	#yum -ty install vim python2 zsh environment-modules
	#dnf --assumeyes --quiet install vim python2 zsh environment-modules
	pwd
	ls 
	bash -x ./add_package.sh | tee add_package.log

	echo "end"                  >> /THIS_IS_INSIDE_SINGULARITY
	date                        >> /THIS_IS_INSIDE_SINGULARITY

%labels
	MAINTAINER  Tin Ho tin'at'lbl.gov
```

## Collection

 - Name: [tin6150/guiDesk](https://github.com/tin6150/guiDesk)
 - License: None

