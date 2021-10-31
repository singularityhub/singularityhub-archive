---
id: 3039
name: "ISU-HPC/salmon"
branch: "master"
tag: "latest"
commit: "136f45664a7463a1297ba550e31f92b11415b1d6"
version: "1044d61b1518c8f45fc23bf43d8b5a11"
build_date: "2018-06-04T20:25:01.631Z"
size_mb: 1175
size: 343478303
sif: "https://datasets.datalad.org/shub/ISU-HPC/salmon/latest/2018-06-04-136f4566-1044d61b/1044d61b1518c8f45fc23bf43d8b5a11.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/salmon/latest/2018-06-04-136f4566-1044d61b/
recipe: https://datasets.datalad.org/shub/ISU-HPC/salmon/latest/2018-06-04-136f4566-1044d61b/Singularity
collection: ISU-HPC/salmon
---

# ISU-HPC/salmon:latest

```bash
$ singularity pull shub://ISU-HPC/salmon:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
FROM: ubuntu:18.04

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%post

apt update
apt install -y git gcc make g++ cmake libboost-all-dev liblzma-dev libbz2-dev \
                ca-certificates zlib1g-dev curl unzip autoconf

# install salmon

cd /
export SALMON_VERSION=0.10.1
curl -k -L https://github.com/COMBINE-lab/salmon/archive/v${SALMON_VERSION}.tar.gz -o salmon-v${SALMON_VERSION}.tar.gz
tar xzf salmon-v${SALMON_VERSION}.tar.gz
cd salmon-${SALMON_VERSION}
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local
make
make install


cd /
rm -rf salmon-v${SALMON_VERSION}.tar.gz

# Add PATH

echo 'export PATH=/usr/local/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ISU-HPC/salmon](https://github.com/ISU-HPC/salmon)
 - License: None

