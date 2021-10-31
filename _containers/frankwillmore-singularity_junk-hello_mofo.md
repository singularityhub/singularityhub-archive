---
id: 9660
name: "frankwillmore/singularity_junk"
branch: "master"
tag: "hello_mofo"
commit: "7b01e2946ae041d4a91291b0aad62c37061fa721"
version: "d16c8cbd572c73f785b3a990c8a83b5a"
build_date: "2019-06-07T11:19:42.581Z"
size_mb: 601
size: 196354079
sif: "https://datasets.datalad.org/shub/frankwillmore/singularity_junk/hello_mofo/2019-06-07-7b01e294-d16c8cbd/d16c8cbd572c73f785b3a990c8a83b5a.simg"
url: https://datasets.datalad.org/shub/frankwillmore/singularity_junk/hello_mofo/2019-06-07-7b01e294-d16c8cbd/
recipe: https://datasets.datalad.org/shub/frankwillmore/singularity_junk/hello_mofo/2019-06-07-7b01e294-d16c8cbd/Singularity
collection: frankwillmore/singularity_junk
---

# frankwillmore/singularity_junk:hello_mofo

```bash
$ singularity pull shub://frankwillmore/singularity_junk:hello_mofo
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # setup is run after the base 'centos' image is
   # downloaded and upacked but before entering the 
   # container environment
   
   # Frank wuz here
   
   # this is the path on the local system to 
   # what will become your container's root directory
   echo ${SINGULARITY_ROOTFS}
   # create a directory for your application
   mkdir ${SINGULARITY_ROOTFS}/myapp
   # copy the hello world example from the github to 
   # the app directory
   cp example_codes/hello_world.cpp ${SINGULARITY_ROOTFS}/myapp/

%post
   # post is run after entering the container env. 
   
   # need to install some development tools to
   # build our code
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc g++
   
   # enter directory where source file was copied
   cd /myapp
   
   # build
   g++ -o hello_world hello_world.cpp

%runscript
   # run script
   /myapp/hello_world

%environment
   # can define runtime environment variables here
   # these vars will be set during calls to 'shell'
   # or 'exec' or 'run' but will not be set during
   # the previous 'post' section of the recipe file
   # so, if you need them, define them there as well
   export PATH=$PATH:/myapp
```

## Collection

 - Name: [frankwillmore/singularity_junk](https://github.com/frankwillmore/singularity_junk)
 - License: None

