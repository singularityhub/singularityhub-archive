---
id: 9170
name: "iem71/singularityRecipe"
branch: "master"
tag: "py"
commit: "d411d9bb5779725eb92029d63afac3e3fa8fcbd5"
version: "b7e3ab6ce2045b0d2cfdd62e42b10e65"
build_date: "2019-05-19T23:23:12.175Z"
size_mb: None
size: 334159903
sif: "https://datasets.datalad.org/shub/iem71/singularityRecipe/py/2019-05-19-d411d9bb-b7e3ab6c/b7e3ab6ce2045b0d2cfdd62e42b10e65.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iem71/singularityRecipe/py/2019-05-19-d411d9bb-b7e3ab6c/
recipe: https://datasets.datalad.org/shub/iem71/singularityRecipe/py/2019-05-19-d411d9bb-b7e3ab6c/Singularity
collection: iem71/singularityRecipe
---

# iem71/singularityRecipe:py

```bash
$ singularity pull shub://iem71/singularityRecipe:py
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget
# best to build up container using kickstart mentality. 
# ie, to add more packages to image,
# re-run bootstrap command again. 
# bootstrap on existing image will build on top of it, not overwriting it/restarting from scratch
# singularity .def file is like kickstart file
# unix commands can be run, but if there is any error, the bootstrap process ends
%setup
   # commands to be executed on host outside container during bootstrap
%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum -y install vim wget python epel-release
    yum -y install python-pip
     # install tensorflow
    pip install --upgrade pip
    pip install tensorflow==1.2.1
    pip install numpy==1.14
    pip install opencv-python
     # create bind points for storage.
     mkdir /extra
     mkdir /xdisk
     exit 0
 %runscript
   # commands to be executed when the container runs
   echo "Arguments received: $*"
   exec /usr/bin/python "$@"
 %test
   # commands to be executed within container at close of bootstrap process
   python --version
```

## Collection

 - Name: [iem71/singularityRecipe](https://github.com/iem71/singularityRecipe)
 - License: None

