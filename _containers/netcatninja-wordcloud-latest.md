---
id: 8707
name: "netcatninja/wordcloud"
branch: "master"
tag: "latest"
commit: "692dec99c7e283caadc4b22bbdc0f97e8d8c8fd6"
version: "20fc0a25f66e3dce529f82b62594f12d"
build_date: "2019-04-29T05:02:48.477Z"
size_mb: 858
size: 259928095
sif: "https://datasets.datalad.org/shub/netcatninja/wordcloud/latest/2019-04-29-692dec99-20fc0a25/20fc0a25f66e3dce529f82b62594f12d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/netcatninja/wordcloud/latest/2019-04-29-692dec99-20fc0a25/
recipe: https://datasets.datalad.org/shub/netcatninja/wordcloud/latest/2019-04-29-692dec99-20fc0a25/Singularity
collection: netcatninja/wordcloud
---

# netcatninja/wordcloud:latest

```bash
$ singularity pull shub://netcatninja/wordcloud:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%help
    Install Python 3.6 and make a word cloud

%runscript
    /opt/python3/bin/python3.6 -V
    echo "We are going to make a word cloud."
    echo "Text: $1"
    echo "Image: $2"
    /opt/python3/bin/wordcloud_cli --text $1 --imagefile $2 
    curl --upload-file $2 https://transfer.sh
    
%environment
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
    export PATH=/opt/python3/bin:/usr/bin:/usr/local/sbin:/bin:/usr/local/bin:/usr/sbin:/sbin

%post
    apt-get -y update && apt-get install -y --no-install-recommends  \
    build-essential ca-certificates curl git libssl-dev lolcat wget zlib1g-dev
    cd /opt && wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz && \
    tar xf Python-3.6.8.tar.xz && cd Python-3.6.8 && ./configure --prefix=/opt/python3 && \
    make && make altinstall && ln -s /opt/python3/bin/python3.6 /opt/python3/bin/python3
    /opt/python3/bin/pip3.6 install wordcloud

%labels
    Author Brie Carranza
```

## Collection

 - Name: [netcatninja/wordcloud](https://github.com/netcatninja/wordcloud)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

