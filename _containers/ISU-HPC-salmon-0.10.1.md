---
id: 3040
name: "ISU-HPC/salmon"
branch: "master"
tag: "0.10.1"
commit: "04f63c561f9cb287c2ddbb86e3f232a677bf95a9"
version: "f6cba3daa0c2720499a4df6abc99c135"
build_date: "2018-06-05T00:16:53.139Z"
size_mb: 1175
size: 343482399
sif: "https://datasets.datalad.org/shub/ISU-HPC/salmon/0.10.1/2018-06-05-04f63c56-f6cba3da/f6cba3daa0c2720499a4df6abc99c135.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/salmon/0.10.1/2018-06-05-04f63c56-f6cba3da/
recipe: https://datasets.datalad.org/shub/ISU-HPC/salmon/0.10.1/2018-06-05-04f63c56-f6cba3da/Singularity
collection: ISU-HPC/salmon
---

# ISU-HPC/salmon:0.10.1

```bash
$ singularity pull shub://ISU-HPC/salmon:0.10.1
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

