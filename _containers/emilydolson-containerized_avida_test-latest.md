---
id: 469
name: "emilydolson/containerized_avida_test"
branch: "master"
tag: "latest"
commit: "d8f1f50929293825d6cbf66d686035b9be12db27"
version: "9b73fcae3e9b2ad1331e205d0fa66ddf"
build_date: "2017-10-20T18:53:21.602Z"
size_mb: 298
size: 77889567
sif: "https://datasets.datalad.org/shub/emilydolson/containerized_avida_test/latest/2017-10-20-d8f1f509-9b73fcae/9b73fcae3e9b2ad1331e205d0fa66ddf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/emilydolson/containerized_avida_test/latest/2017-10-20-d8f1f509-9b73fcae/
recipe: https://datasets.datalad.org/shub/emilydolson/containerized_avida_test/latest/2017-10-20-d8f1f509-9b73fcae/Singularity
collection: emilydolson/containerized_avida_test
---

# emilydolson/containerized_avida_test:latest

```bash
$ singularity pull shub://emilydolson/containerized_avida_test:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

%files
/mnt/home/dolsonem/containerized_avida_test $SINGULARITY_ROOTFS/containerized_avida_test

%post  
echo "This section happens once after bootstrap to build the image."  
apt-get update
apt-get --assume-yes install criu

mkdir -p /mnt/home
mkdir -p /mnt/research
mkdir -p /mnt/dfs17
mkdir -p /mnt/ffs17
mkdir -p /mnt/local
mkdir -p /mnt/ls15
mkdir -p /opt/software
mkdir -p /code  

%runscript
echo "This gets run when you run the image!" 
SHELL="$(getent passwd $USER | awk -F: '{print $NF}')"
SHELL=${SHELL:-/bin/bash}
if [[ "$@" == "" ]]; then
  exec env -i TERM="$TERM" HOME="$HOME" $SHELL -l
else
  exec env -i TERM="$TERM" HOME="$HOME" $@
fi

cd $SINGULARITY_ROOTFS/containerized_avida_test/results/run_1
cp -r $SINGULARITY_ROOTFS/containerized_avida_test/configs .
./avida
```

## Collection

 - Name: [emilydolson/containerized_avida_test](https://github.com/emilydolson/containerized_avida_test)
 - License: None

