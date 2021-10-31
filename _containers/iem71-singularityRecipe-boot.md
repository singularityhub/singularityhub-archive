---
id: 9166
name: "iem71/singularityRecipe"
branch: "master"
tag: "boot"
commit: "78e616a4424b801e07240a1cd768d8fc862805ed"
version: "b2d91e90fd893661cac969779eca4706"
build_date: "2019-05-19T19:55:29.274Z"
size_mb: None
size: 244338719
sif: "https://datasets.datalad.org/shub/iem71/singularityRecipe/boot/2019-05-19-78e616a4-b2d91e90/b2d91e90fd893661cac969779eca4706.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iem71/singularityRecipe/boot/2019-05-19-78e616a4-b2d91e90/
recipe: https://datasets.datalad.org/shub/iem71/singularityRecipe/boot/2019-05-19-78e616a4-b2d91e90/Singularity
collection: iem71/singularityRecipe
---

# iem71/singularityRecipe:boot

```bash
$ singularity pull shub://iem71/singularityRecipe:boot
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
    pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl
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

