---
id: 7251
name: "powerPlant/pcl-srf"
branch: "master"
tag: "1.9.0"
commit: "c6e8c235f4943fe212ce3c8ce4968ae5b298dd86"
version: "9fe074405f722a4a748e74557cde9108"
build_date: "2019-02-15T00:23:15.733Z"
size_mb: 800
size: 198979615
sif: "https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.9.0/2019-02-15-c6e8c235-9fe07440/9fe074405f722a4a748e74557cde9108.simg"
url: https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.9.0/2019-02-15-c6e8c235-9fe07440/
recipe: https://datasets.datalad.org/shub/powerPlant/pcl-srf/1.9.0/2019-02-15-c6e8c235-9fe07440/Singularity
collection: powerPlant/pcl-srf
---

# powerPlant/pcl-srf:1.9.0

```bash
$ singularity pull shub://powerPlant/pcl-srf:1.9.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:29

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.9.0

%post
  ## Download build prerequisites
  dnf -y install boost boost-devel eigen3 eigen3-devel flann flann-devel gcc gcc-c++ make mlpack-bin mlpack-devel qhull qhull-devel vtk vtk-devel wget zlib zlib-devel

  cd /opt
  wget https://github.com/PointCloudLibrary/pcl/archive/pcl-1.9.0.tar.gz
  tar -xvf pcl-1.9.0.tar.gz
  cd /opt/pcl-pcl-1.9.0 && mkdir build && cd build
  cmake -DCMAKE_BUILD_TYPE=Release ..
  make -j$(nproc)
  make -j$(nproc) install

  ## Cleanup
  dnf -y erase eigen3-devel flann-devel gcc gcc-c++ make mlpack-devel qhull-devel wget zlib-devel
  dnf -y clean all
  rm -rf /opt/pcl*

%runscript
if [ $# -eq 0 ]; then
  echo -e 'This Singularity image cannot provide a single entrypoint. Please use `<image-name.simg> <CMD>` or `singularity exec <image-name.simg> <CMD>`, where <CMD> is one of the following:\n'
  exec ls /usr/local/bin
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/pcl-srf](https://github.com/powerPlant/pcl-srf)
 - License: None

