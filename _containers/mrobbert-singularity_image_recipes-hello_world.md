---
id: 7639
name: "mrobbert/singularity_image_recipes"
branch: "master"
tag: "hello_world"
commit: "6beb630d2e25911679cdd2d045a4cb3443d18ac4"
version: "cd4566a63358be0d693176b66d324f00"
build_date: "2019-03-07T01:18:17.761Z"
size_mb: 585
size: 189927455
sif: "https://datasets.datalad.org/shub/mrobbert/singularity_image_recipes/hello_world/2019-03-07-6beb630d-cd4566a6/cd4566a63358be0d693176b66d324f00.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mrobbert/singularity_image_recipes/hello_world/2019-03-07-6beb630d-cd4566a6/
recipe: https://datasets.datalad.org/shub/mrobbert/singularity_image_recipes/hello_world/2019-03-07-6beb630d-cd4566a6/Singularity
collection: mrobbert/singularity_image_recipes
---

# mrobbert/singularity_image_recipes:hello_world

```bash
$ singularity pull shub://mrobbert/singularity_image_recipes:hello_world
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

 - Name: [mrobbert/singularity_image_recipes](https://github.com/mrobbert/singularity_image_recipes)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

