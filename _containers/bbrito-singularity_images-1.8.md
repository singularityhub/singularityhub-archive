---
id: 2698
name: "bbrito/singularity_images"
branch: "master"
tag: "1.8"
commit: "023ae5aa3eb4c476c34e7e3c84ecf22cd3965010"
version: "1d3c8b638037e31519e82d6b13013ef3"
build_date: "2018-05-02T13:59:14.785Z"
size_mb: 6963
size: 2062479391
sif: "https://datasets.datalad.org/shub/bbrito/singularity_images/1.8/2018-05-02-023ae5aa-1d3c8b63/1d3c8b638037e31519e82d6b13013ef3.simg"
url: https://datasets.datalad.org/shub/bbrito/singularity_images/1.8/2018-05-02-023ae5aa-1d3c8b63/
recipe: https://datasets.datalad.org/shub/bbrito/singularity_images/1.8/2018-05-02-023ae5aa-1d3c8b63/Singularity
collection: bbrito/singularity_images
---

# bbrito/singularity_images:1.8

```bash
$ singularity pull shub://bbrito/singularity_images:1.8
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: bbrito/singularity_images:1.7


%post
    echo "Hello from inside the container"
    apt-get update
    apt-get install -y \
        wget \
        lsb-release \
        sudo \
        man \
        less \
        locales \
        vim \
        git \
        mercurial \
        make \
        htop \
        terminator
    apt-get clean

    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
    echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list

    wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -
    echo "deb http://packages.osrfoundation.org/gazebo/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list
    apt-get update

    apt-get install -q -y ros-kinetic-desktop-full 
    apt-get install -q -y ros-kinetic-opencv3 ros-kinetic-pcl-ros ros-kinetic-fake-localization
    apt-get install -q -y ros-kinetic-ros-control ros-kinetic-control-toolbox
    apt-get install -q -y ros-kinetic-vision-msgs
    apt-get install -q -y gazebo9=9.0.0-1*
    apt-get install -q -y libgazebo9-dev ros-kinetic-gazebo9-plugins ros-kinetic-gazebo9-ros

%runscript
    echo "This is what happens when you run the container..."
```

## Collection

 - Name: [bbrito/singularity_images](https://github.com/bbrito/singularity_images)
 - License: None

