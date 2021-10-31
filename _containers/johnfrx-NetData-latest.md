---
id: 10406
name: "johnfrx/NetData"
branch: "master"
tag: "latest"
commit: "d76577410fd967643e44017bcf2050d3973aa84b"
version: "fa3376203c4d492389d9f19aa088d419"
build_date: "2019-07-30T09:47:08.763Z"
size_mb: 474.0
size: 171073567
sif: "https://datasets.datalad.org/shub/johnfrx/NetData/latest/2019-07-30-d7657741-fa337620/fa3376203c4d492389d9f19aa088d419.sif"
url: https://datasets.datalad.org/shub/johnfrx/NetData/latest/2019-07-30-d7657741-fa337620/
recipe: https://datasets.datalad.org/shub/johnfrx/NetData/latest/2019-07-30-d7657741-fa337620/Singularity
collection: johnfrx/NetData
---

# johnfrx/NetData:latest

```bash
$ singularity pull shub://johnfrx/NetData:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%runscript
    exec echo "Centos7 image for use with globus"


%post
    #echo "The post section is where you can install, and configure your container."
    #
        adduser netdata
        mkdir /var/lib/netdata
        chown -R netdata:netdata /var/lib/netdata
        yum -y install autoconf automake curl gcc git libmnl-devel libuuid-devel openssl-devel libuv-devel lz4-devel Judy-devel make nc pkgconfig python zlib-devel
        git clone https://github.com/netdata/netdata.git --depth=100
        cd netdata
        echo | ./netdata-installer.sh
```

## Collection

 - Name: [johnfrx/NetData](https://github.com/johnfrx/NetData)
 - License: None

