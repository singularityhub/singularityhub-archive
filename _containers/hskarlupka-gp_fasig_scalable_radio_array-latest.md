---
id: 1425
name: "hskarlupka/gp_fasig_scalable_radio_array"
branch: "master"
tag: "latest"
commit: "141b6ff4df3583e671f50cfac0e7f79894562608"
version: "e305e0c153b452e99ed905bee7886af1"
build_date: "2018-01-22T17:59:49.670Z"
size_mb: 769
size: 279040031
sif: "https://datasets.datalad.org/shub/hskarlupka/gp_fasig_scalable_radio_array/latest/2018-01-22-141b6ff4-e305e0c1/e305e0c153b452e99ed905bee7886af1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hskarlupka/gp_fasig_scalable_radio_array/latest/2018-01-22-141b6ff4-e305e0c1/
recipe: https://datasets.datalad.org/shub/hskarlupka/gp_fasig_scalable_radio_array/latest/2018-01-22-141b6ff4-e305e0c1/Singularity
collection: hskarlupka/gp_fasig_scalable_radio_array
---

# hskarlupka/gp_fasig_scalable_radio_array:latest

```bash
$ singularity pull shub://hskarlupka/gp_fasig_scalable_radio_array:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:7

%labels
MAINTAINER hskarlupka

%files
full_sim.py /full_sim.py

%post
yum install -y git

yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
 && yum install -y python36u \
                   python36u-pip

pip3.6 install git+https://github.com/bhokansonfasig/pyrex#egg=pyrex \
               numpy 

mkdir -p /cvmfs
mkdir -p /data
chmod 777 /data
```

## Collection

 - Name: [hskarlupka/gp_fasig_scalable_radio_array](https://github.com/hskarlupka/gp_fasig_scalable_radio_array)
 - License: None

