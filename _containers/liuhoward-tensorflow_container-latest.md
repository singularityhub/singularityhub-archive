---
id: 7948
name: "liuhoward/tensorflow_container"
branch: "master"
tag: "latest"
commit: "c3b39d588144dad87af04d9f64a8c22f97560d89"
version: "946472cb0773ed781e3e9829f868e733"
build_date: "2019-04-10T23:02:51.466Z"
size_mb: 3380
size: 1689133087
sif: "https://datasets.datalad.org/shub/liuhoward/tensorflow_container/latest/2019-04-10-c3b39d58-946472cb/946472cb0773ed781e3e9829f868e733.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/liuhoward/tensorflow_container/latest/2019-04-10-c3b39d58-946472cb/
recipe: https://datasets.datalad.org/shub/liuhoward/tensorflow_container/latest/2019-04-10-c3b39d58-946472cb/Singularity
collection: liuhoward/tensorflow_container
---

# liuhoward/tensorflow_container:latest

```bash
$ singularity pull shub://liuhoward/tensorflow_container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: howard15/tensorflow:latest

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
    #apt-get -y update
    #apt-get -y install fortune cowsay lolcat

%environment
    #export LC_ALL=C
    #export PATH=/usr/games:$PATH

%runscript

%test
  # test that script is a success
```

## Collection

 - Name: [liuhoward/tensorflow_container](https://github.com/liuhoward/tensorflow_container)
 - License: None

