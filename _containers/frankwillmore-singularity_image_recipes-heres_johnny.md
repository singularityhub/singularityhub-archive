---
id: 9659
name: "frankwillmore/singularity_image_recipes"
branch: "master"
tag: "heres_johnny"
commit: "1ed2dc400328e229944ff7465a9049616f5865b1"
version: "bc6a2187c22369f68fecaea1c3a90296"
build_date: "2019-06-07T11:19:42.501Z"
size_mb: 601
size: 196354079
sif: "https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/heres_johnny/2019-06-07-1ed2dc40-bc6a2187/bc6a2187c22369f68fecaea1c3a90296.simg"
url: https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/heres_johnny/2019-06-07-1ed2dc40-bc6a2187/
recipe: https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/heres_johnny/2019-06-07-1ed2dc40-bc6a2187/Singularity
collection: frankwillmore/singularity_image_recipes
---

# frankwillmore/singularity_image_recipes:heres_johnny

```bash
$ singularity pull shub://frankwillmore/singularity_image_recipes:heres_johnny
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

 - Name: [frankwillmore/singularity_image_recipes](https://github.com/frankwillmore/singularity_image_recipes)
 - License: None

