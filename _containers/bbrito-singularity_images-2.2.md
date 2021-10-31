---
id: 2760
name: "bbrito/singularity_images"
branch: "master"
tag: "2.2"
commit: "fa77fd9800cdd1d203d3ff702f19f65293329d51"
version: "904ffd640d7202d62bae33617d4093f2"
build_date: "2018-07-03T09:02:32.017Z"
size_mb: 5778
size: 1793388575
sif: "https://datasets.datalad.org/shub/bbrito/singularity_images/2.2/2018-07-03-fa77fd98-904ffd64/904ffd640d7202d62bae33617d4093f2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bbrito/singularity_images/2.2/2018-07-03-fa77fd98-904ffd64/
recipe: https://datasets.datalad.org/shub/bbrito/singularity_images/2.2/2018-07-03-fa77fd98-904ffd64/Singularity
collection: bbrito/singularity_images
---

# bbrito/singularity_images:2.2

```bash
$ singularity pull shub://bbrito/singularity_images:2.2
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: bbrito/singularity_images:2.1

%post
    echo "Hello from inside the container"
    mkdir -p /home/bdebrito_sing/catkin_ws
    mkdir -p /home/bdebrito_sing/catkin_ws/src
    apt-get update
    apt-get install -y \
        python-wstool \
        ros-kinetic-moveit-msgs \
        ros-kinetic-jsk-recognition-msgs \
        ros-kinetic-moveit-ros \
        ros-kinetic-moveit \
        ssh
        
    cd /home/bdebrito_sing/
    git clone https://github.com/acado/acado.git -b stable ACADOtoolkit
    cd ACADOtoolkit
	mkdir build
	cd build
	cmake ..
	make
        
    cd /home/bdebrito_sing/catkin_ws/src
    wstool init .
    wstool merge https://raw.githubusercontent.com/bbrito/predictive_control/master/predictive_control.rosinstall
    wstool update

%runscript
    echo "This is what happens when you run the container..."
```

## Collection

 - Name: [bbrito/singularity_images](https://github.com/bbrito/singularity_images)
 - License: None

