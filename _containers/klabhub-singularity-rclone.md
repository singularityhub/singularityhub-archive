---
id: 9373
name: "klabhub/singularity"
branch: "master"
tag: "rclone"
commit: "c89f7024ef0eb6cd2fdc45c1af281bdb8062cfc5"
version: "552687df4a6320a64c562e0bcd85cdb6"
build_date: "2020-12-22T06:06:21.091Z"
size_mb: 36
size: 12328991
sif: "https://datasets.datalad.org/shub/klabhub/singularity/rclone/2020-12-22-c89f7024-552687df/552687df4a6320a64c562e0bcd85cdb6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/klabhub/singularity/rclone/2020-12-22-c89f7024-552687df/
recipe: https://datasets.datalad.org/shub/klabhub/singularity/rclone/2020-12-22-c89f7024-552687df/Singularity
collection: klabhub/singularity
---

# klabhub/singularity:rclone

```bash
$ singularity pull shub://klabhub/singularity:rclone
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.5

%labels
    MAINTAINER Victor Sande <victorsv at gmail>
    APP rclone
    VERSION v1.41

%help
    Interact with several Cloud storage endpoints
    Syntax: [options] subcommand <parameters> <parameters...>
    Official docs: https://rclone.org/docs/


%post
    export RCLONE_VERSION=current
    export ARCH=amd64
    apk --no-cache add ca-certificates fuse wget 
    cd /tmp 
    wget -q http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip 
    unzip /tmp/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip 
    mv /tmp/rclone-*-linux-${ARCH}/rclone /usr/bin 
    rm -r /tmp/rclone* 

%runscript
    /usr/bin/rclone "$@"


##############################
# RClone
##############################

%apphelp rclone
    Interact with several Cloud storage endpoints
    Syntax: [options] subcommand <parameters> <parameters...>
    Official docs: https://rclone.org/docs/

%apprun rclone
    /usr/bin/rclone "$@"

CMD ["--version"]
```

## Collection

 - Name: [klabhub/singularity](https://github.com/klabhub/singularity)
 - License: None

