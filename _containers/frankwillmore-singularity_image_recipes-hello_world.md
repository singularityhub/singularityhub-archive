---
id: 9655
name: "frankwillmore/singularity_image_recipes"
branch: "master"
tag: "hello_world"
commit: "c61255a4ee45f938b60fbdbbc7bff3cb89fcff82"
version: "a41d740da10b6c97cea473da5dd92112"
build_date: "2019-06-07T11:19:42.506Z"
size_mb: 601
size: 196354079
sif: "https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/hello_world/2019-06-07-c61255a4-a41d740d/a41d740da10b6c97cea473da5dd92112.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/frankwillmore/singularity_image_recipes/hello_world/2019-06-07-c61255a4-a41d740d/
recipe: https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/hello_world/2019-06-07-c61255a4-a41d740d/Singularity
collection: frankwillmore/singularity_image_recipes
---

# frankwillmore/singularity_image_recipes:hello_world

```bash
$ singularity pull shub://frankwillmore/singularity_image_recipes:hello_world
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

