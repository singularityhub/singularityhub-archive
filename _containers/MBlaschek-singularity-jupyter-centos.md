---
id: 11706
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "centos"
commit: "c37762d6117a004a467b7764fbbc128b8c77f001"
version: "b4a441dbfbaf223b78e205385438c2b6c899e05baa346c3045b0f4c7a6db3fc4"
build_date: "2020-12-27T09:52:29.749Z"
size_mb: 96.625
size: 101318656
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/centos/2020-12-27-c37762d6-b4a441db/b4a441dbfbaf223b78e205385438c2b6c899e05baa346c3045b0f4c7a6db3fc4.sif"
url: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/centos/2020-12-27-c37762d6-b4a441db/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/centos/2020-12-27-c37762d6-b4a441db/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:centos

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:centos
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.10
#From: centos:latest

%help
	Container Centos 6.10 (docker)
	Glibc: 2.12-1.212.el6.x86_64
	Installed: wget, git, curl, bzip2 ca-certificates

%labels
	Container.OS CentOS 6.10
	Container.Glibc 2.12-1.212.el6.x86_64
	Definition.Author  M. Blaschek
	Definition.Author.Email michael.blaschek@univie.ac.at
	Definition.File.Version 1.0
	Definition.File.Date 5.11.2019

%files
	run.sh /usr/bin

%runscript
	exec /usr/bin/run.sh "$@"

%post
	yum check-update && yum -y update
	yum install -y wget bzip2 ca-certificates curl git
	yum clean all
	cat > /etc/locale.conf <<EOF
LANG="C.UTF-8"
LC_CTYPE="C.UTF-8"
EOF
	cat > /etc/sysconfig/i18n <<EOF
LANG="C.UTF-8"
SYSFONT="latarcyrheb-sun16"
EOF
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

