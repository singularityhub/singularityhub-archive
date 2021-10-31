---
id: 10585
name: "stephansmit/pointwise_containers"
branch: "master"
tag: "latest"
commit: "8f6f9ecd766630970e90a0c42704ca2664d63fde"
version: "39ff16d0187c9f4fe045b61dc30f3367"
build_date: "2020-08-07T11:49:05.960Z"
size_mb: 2142.0
size: 1403985951
sif: "https://datasets.datalad.org/shub/stephansmit/pointwise_containers/latest/2020-08-07-8f6f9ecd-39ff16d0/39ff16d0187c9f4fe045b61dc30f3367.sif"
url: https://datasets.datalad.org/shub/stephansmit/pointwise_containers/latest/2020-08-07-8f6f9ecd-39ff16d0/
recipe: https://datasets.datalad.org/shub/stephansmit/pointwise_containers/latest/2020-08-07-8f6f9ecd-39ff16d0/Singularity
collection: stephansmit/pointwise_containers
---

# stephansmit/pointwise_containers:latest

```bash
$ singularity pull shub://stephansmit/pointwise_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    echo Update apt-get
    apt-get -y update &&     apt-get -y install libglu1 libxrender-dev libxcursor1 libxft2 libxinerama1 
    apt-get -y install libxt6 libgl1 libx11-xcb1 qt5-default libxss1
    echo 'Installing Pointwise requirements'
    apt-get update &&     apt-get install -y default-jre libglib2.0-0 libgconf2-4 dos2unix wget 
    echo 'Download the Pointwise files'
    wget -O /opt/pw-V18.0R3-linux_x86_64-jre.sh https://transfer.sh/UspLZ/installer.sh 
    chmod -R 777 /opt/pw-V18.0R3-linux_x86_64-jre.sh

    echo 'Installing Pointwise via Terminal'
    printf 'o\n2\n\n\n\n\n\n\n\n1\n/opt/pointwise/\n\n' | /opt/pw-V18.0R3-linux_x86_64-jre.sh -c
   
%runscript
    exec '$@'
```

## Collection

 - Name: [stephansmit/pointwise_containers](https://github.com/stephansmit/pointwise_containers)
 - License: None

