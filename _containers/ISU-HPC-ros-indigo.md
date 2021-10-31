---
id: 2300
name: "ISU-HPC/ros"
branch: "master"
tag: "indigo"
commit: "f2ea85c7494f0f06857b15e72a39329aae2dcf73"
version: "b76233f6266c3a87f51583e73442af3f"
build_date: "2020-07-24T20:35:01.551Z"
size_mb: 2223
size: 675516447
sif: "https://datasets.datalad.org/shub/ISU-HPC/ros/indigo/2020-07-24-f2ea85c7-b76233f6/b76233f6266c3a87f51583e73442af3f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/ros/indigo/2020-07-24-f2ea85c7-b76233f6/
recipe: https://datasets.datalad.org/shub/ISU-HPC/ros/indigo/2020-07-24-f2ea85c7-b76233f6/Singularity
collection: ISU-HPC/ros
---

# ISU-HPC/ros:indigo

```bash
$ singularity pull shub://ISU-HPC/ros:indigo
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ros:indigo-robot

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%environment

        ROS_ROOT=/opt/ros/indigo/share/ros
        export ROS_ROOT
        ROS_PACKAGE_PATH=/opt/ros/indigo/share:/opt/ros/indigo/stacks
        export ROS_PACKAGE_PATH
        ROS_MASTER_URI=http://localhost:11311
        export ROS_MASTER_URI
        LD_LIBRARY_PATH=/opt/ros/indigo/lib:/.singularity.d/libs
        export LD_LIBRARY_PATH
        CPATH=/opt/ros/indigo/include
        export CPATH
        PATH=/opt/ros/indigo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        export PATH
        PYTHONPATH=/opt/ros/indigo/lib/python2.7/dist-packages
        export PYTHONPATH
        PKG_CONFIG_PATH=/opt/ros/indigo/lib/pkgconfig
        export PKG_CONFIG_PATH
        CMAKE_PREFIX_PATH=/opt/ros/indigo
        export CMAKE_PREFIX_PATH
        ROS_ETC_DIR=/opt/ros/indigo/etc/ros
        export ROS_ETC_DIR





%post

    sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
    apt-get update
    apt-get install -y ros-indigo-desktop-full
```

## Collection

 - Name: [ISU-HPC/ros](https://github.com/ISU-HPC/ros)
 - License: None

