---
id: 8771
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "deeptools"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "d096f52689f50da37bb4d43762f18997"
build_date: "2019-09-24T17:41:40.692Z"
size_mb: 3209
size: 1028837407
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/deeptools/2019-09-24-5f15386e-d096f526/d096f52689f50da37bb4d43762f18997.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/deeptools/2019-09-24-5f15386e-d096f526/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/deeptools/2019-09-24-5f15386e-d096f526/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:deeptools

```bash
$ singularity pull shub://jlboat/BioinfoContainers:deeptools
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
        libglib2.0-0 libxext6 libsm6 libxrender1 \
        git mercurial subversion
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
        /bin/bash ~/anaconda.sh -b -p /opt/conda && \
        rm ~/anaconda.sh && \
        ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
        echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
        echo "conda activate base" >> ~/.bashrc
    apt-get install -y curl grep sed dpkg && \
        TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
        curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
        dpkg -i tini.deb && \
        rm tini.deb && \
        apt-get clean
    /opt/conda/bin/conda install -c bioconda deeptools
    /opt/conda/bin/conda clean -a

%runscript
    exec /opt/conda/bin/"$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

