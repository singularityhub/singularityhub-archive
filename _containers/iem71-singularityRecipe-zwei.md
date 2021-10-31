---
id: 9203
name: "iem71/singularityRecipe"
branch: "master"
tag: "zwei"
commit: "5bf2c07dc78faa41f7cb327ae5b1515d01be3c9e"
version: "9f4d1f84817783279f083295bdf3ee4f"
build_date: "2019-05-21T15:12:30.946Z"
size_mb: None
size: 336027679
sif: "https://datasets.datalad.org/shub/iem71/singularityRecipe/zwei/2019-05-21-5bf2c07d-9f4d1f84/9f4d1f84817783279f083295bdf3ee4f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iem71/singularityRecipe/zwei/2019-05-21-5bf2c07d-9f4d1f84/
recipe: https://datasets.datalad.org/shub/iem71/singularityRecipe/zwei/2019-05-21-5bf2c07d-9f4d1f84/Singularity
collection: iem71/singularityRecipe
---

# iem71/singularityRecipe:zwei

```bash
$ singularity pull shub://iem71/singularityRecipe:zwei
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
    yum -y update
    yum -y install libXext libSM libXrender
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

