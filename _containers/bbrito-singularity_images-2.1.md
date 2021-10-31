---
id: 2759
name: "bbrito/singularity_images"
branch: "master"
tag: "2.1"
commit: "eadcc810212ba3ed651f786dcf4490c6cf877ef6"
version: "3efafde8d824c37f492e078137362414"
build_date: "2018-07-02T15:53:09.692Z"
size_mb: 5521
size: 1724440607
sif: "https://datasets.datalad.org/shub/bbrito/singularity_images/2.1/2018-07-02-eadcc810-3efafde8/3efafde8d824c37f492e078137362414.simg"
url: https://datasets.datalad.org/shub/bbrito/singularity_images/2.1/2018-07-02-eadcc810-3efafde8/
recipe: https://datasets.datalad.org/shub/bbrito/singularity_images/2.1/2018-07-02-eadcc810-3efafde8/Singularity
collection: bbrito/singularity_images
---

# bbrito/singularity_images:2.1

```bash
$ singularity pull shub://bbrito/singularity_images:2.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: bbrito/singularity_images:2.0

%post
    echo "Hello from inside the container"
    mkdir -p /home/bdebrito_sing
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
        terminator \
        python-wstool \
        ssh
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

%runscript
    echo "This is what happens when you run the container..."
```

## Collection

 - Name: [bbrito/singularity_images](https://github.com/bbrito/singularity_images)
 - License: None

