---
id: 2301
name: "ISU-HPC/ros"
branch: "master"
tag: "kinetic"
commit: "49f3330e6c5e2d0fe9001d1fcb7eaf59b9ad58f6"
version: "4cdc94401e33e092b656d0c3c78c3331"
build_date: "2020-12-05T12:54:02.447Z"
size_mb: 3510
size: 1101832223
sif: "https://datasets.datalad.org/shub/ISU-HPC/ros/kinetic/2020-12-05-49f3330e-4cdc9440/4cdc94401e33e092b656d0c3c78c3331.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/ros/kinetic/2020-12-05-49f3330e-4cdc9440/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ros/kinetic/2020-12-05-49f3330e-4cdc9440/Singularity
collection: ISU-HPC/ros
---

# ISU-HPC/ros:kinetic

```bash
$ singularity pull shub://ISU-HPC/ros:kinetic
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ros:kinetic-robot

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%environment

        ROS_ROOT=/opt/ros/kinetic/share/ros
        export ROS_ROOT
        ROS_PACKAGE_PATH=/opt/ros/kinetic/share:/opt/ros/kinetic/stacks
        export ROS_PACKAGE_PATH
        ROS_MASTER_URI=http://localhost:11311
        export ROS_MASTER_URI
        LD_LIBRARY_PATH=/opt/ros/kinetic/lib:/.singularity.d/libs
        export LD_LIBRARY_PATH
        CPATH=/opt/ros/kinetic/include
        export CPATH
        PATH=/opt/ros/kinetic/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        export PATH
        PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages
        export PYTHONPATH
        PKG_CONFIG_PATH=/opt/ros/kinetic/lib/pkgconfig
        export PKG_CONFIG_PATH
        CMAKE_PREFIX_PATH=/opt/ros/kinetic
        export CMAKE_PREFIX_PATH
        ROS_ETC_DIR=/opt/ros/kinetic/etc/ros
        export ROS_ETC_DIR





%post

    sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
    apt-get update
    apt-get install -y ros-kinetic-desktop-full
```

## Collection

 - Name: [ISU-HPC/ros](https://github.com/ISU-HPC/ros)
 - License: None

