---
id: 2298
name: "ISU-HPC/ros"
branch: "master"
tag: "latest"
commit: "956739b4e1709c5af4d356812a04b2e7fd553d2e"
version: "32ec43bb1313fe0653b64b220ad11033"
build_date: "2019-09-27T11:37:52.591Z"
size_mb: 3510
size: 1101832223
sif: "https://datasets.datalad.org/shub/ISU-HPC/ros/latest/2019-09-27-956739b4-32ec43bb/32ec43bb1313fe0653b64b220ad11033.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/ros/latest/2019-09-27-956739b4-32ec43bb/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ros/latest/2019-09-27-956739b4-32ec43bb/Singularity
collection: ISU-HPC/ros
---

# ISU-HPC/ros:latest

```bash
$ singularity pull shub://ISU-HPC/ros:latest
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

