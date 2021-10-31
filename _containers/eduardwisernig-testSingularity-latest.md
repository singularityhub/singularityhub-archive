---
id: 1038
name: "eduardwisernig/testSingularity"
branch: "master"
tag: "latest"
commit: "b863cb2f750f22599d2b621cfd37a5a75b5bbff6"
version: "b045fc94ff564a82dd11e31fd7a1f291"
build_date: "2017-12-19T06:40:02.597Z"
size_mb: 600
size: 196730911
sif: "https://datasets.datalad.org/shub/eduardwisernig/testSingularity/latest/2017-12-19-b863cb2f-b045fc94/b045fc94ff564a82dd11e31fd7a1f291.simg"
url: https://datasets.datalad.org/shub/eduardwisernig/testSingularity/latest/2017-12-19-b863cb2f-b045fc94/
recipe: https://datasets.datalad.org/shub/eduardwisernig/testSingularity/latest/2017-12-19-b863cb2f-b045fc94/Singularity
collection: eduardwisernig/testSingularity
---

# eduardwisernig/testSingularity:latest

```bash
$ singularity pull shub://eduardwisernig/testSingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

%labels
MAINTAINER Eduard Wisernig and Joe Melton, ECCC

%environment
BASE_DIR=/code
export BASE_DIR

%runscript
echo "Congratulations! You got the container running!"
cd /code/testSingularity
bin/testSingularity

%post
mkdir -p /code
cd /code
apt update
apt install vim make libnetcdff-dev git gfortran netcdf-bin nano -y -f -m
git clone https://github.com/eduardwisernig/testSingularity.git
cd testSingularity
mkdir bin
make
cd ..
chmod -R 777 testSingularity
```

## Collection

 - Name: [eduardwisernig/testSingularity](https://github.com/eduardwisernig/testSingularity)
 - License: None

