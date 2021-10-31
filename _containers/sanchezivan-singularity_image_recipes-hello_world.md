---
id: 9319
name: "sanchezivan/singularity_image_recipes"
branch: "master"
tag: "hello_world"
commit: "838665c3185212b4e6516ceb326dcc5587c5b931"
version: "17aae7a5dffdf7fc6b5fac629d2a9028"
build_date: "2019-05-25T06:40:09.488Z"
size_mb: 601
size: 196292639
sif: "https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/hello_world/2019-05-25-838665c3-17aae7a5/17aae7a5dffdf7fc6b5fac629d2a9028.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sanchezivan/singularity_image_recipes/hello_world/2019-05-25-838665c3-17aae7a5/
recipe: https://datasets.datalad.org/shub/sanchezivan/singularity_image_recipes/hello_world/2019-05-25-838665c3-17aae7a5/Singularity
collection: sanchezivan/singularity_image_recipes
---

# sanchezivan/singularity_image_recipes:hello_world

```bash
$ singularity pull shub://sanchezivan/singularity_image_recipes:hello_world
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   # setup is run after the base 'centos' image is
   # downloaded and upacked but before entering the 
   # container environment
   
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

 - Name: [sanchezivan/singularity_image_recipes](https://github.com/sanchezivan/singularity_image_recipes)
 - License: None

