---
id: 14785
name: "fburic/candia"
branch: "master"
tag: "def"
commit: "846a742b25ba7a699ea843600f8ff7816b03fd76"
version: "a852d11776cc54f32f30263d5920c04feb7d250f5da9805d0e39f92dc24b6c6d"
build_date: "2021-04-16T13:16:50.424Z"
size_mb: 4256.8671875
size: 4463648768
sif: "https://datasets.datalad.org/shub/fburic/candia/def/2021-04-16-846a742b-a852d117/a852d11776cc54f32f30263d5920c04feb7d250f5da9805d0e39f92dc24b6c6d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fburic/candia/def/2021-04-16-846a742b-a852d117/
recipe: https://datasets.datalad.org/shub/fburic/candia/def/2021-04-16-846a742b-a852d117/Singularity
collection: fburic/candia
---

# fburic/candia:def

```bash
$ singularity pull shub://fburic/candia:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.8.3

%files
    candia_env.yaml
    
%post
    mkdir -p /cephyr
    mkdir -p /local
    mkdir -p /apps
    mkdir -p /usr/share/lmod/lmod
    mkdir -p /var/hasplm
    mkdir -p /var/opt/thinlinc
    mkdir -p /usr/lib64
    touch /usr/lib64/libdlfaker.so
    touch /usr/lib64/libvglfaker.so
    touch /usr/bin/nvidia-smi

    apt-get update && apt-get install -y --no-install-recommends libgomp1 libicu-dev  build-essential libcurl4-openssl-dev libxml2-dev libssl-dev r-base pandoc libz-dev

    /opt/conda/bin/conda env update --name base --file candia_env.yaml --prune

    ######
    # Workaround: Use conda JDK package since Spark looks for older Java 1.8.0 in system dir
    ######
    mkdir -p /usr/lib/jvm/java-1.8.0-openjdk-amd64/bin
    ln -s /opt/conda/bin/java /usr/lib/jvm/java-1.8.0-openjdk-amd64/bin/java

    ######
    # Workaround: C libraries installed by conda as dependencies are a bit ouf date so we use the system ones
    # Ref: https://conda.continuum.narkive.com/nGVLDlYz/r-jupyter-cxxabi-version-not-found
    ######
    mv /opt/conda/lib/libstdc++.so.6 /opt/conda/lib/libstdc++.so.6_conda
    mv /opt/conda/lib/libgomp.so.1 /opt/conda/lib/libgomp.so.1_conda
    ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /opt/conda/lib/libstdc++.so.6
    ln -s /usr/lib/x86_64-linux-gnu/libgomp.so.1 /opt/conda/lib/libgomp.so.1

    # Avoid warnings about locale
    echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
    locale-gen && update-locale LANG=en_US.UTF-8


    #####
    # Install R pacakges
    #####
    R -e "install.packages('devtools', dependencies = T)" && R -e "library('devtools'); install_version('tidyverse', version='1.3.0'); install_version('data.table', version='1.12.8')"
    R -e "install.packages(c('feather', 'filesstrings', 'optparse', 'yaml'))"



%environment
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/conda/lib


%runscript
    exec "$@"
```

## Collection

 - Name: [fburic/candia](https://github.com/fburic/candia)
 - License: [Other](None)

