---
id: 15891
name: "GeertvanGeest/test_shub"
branch: "main"
tag: "latest"
commit: "89592aba3de145636b222e5421a550aa88cc06d0"
version: "309ef2d664e3f4a637bd962945e2010d"
build_date: "2021-04-12T07:03:39.760Z"
size_mb: 186.0
size: 77590559
sif: "https://datasets.datalad.org/shub/GeertvanGeest/test_shub/latest/2021-04-12-89592aba-309ef2d6/309ef2d664e3f4a637bd962945e2010d.sif"
url: https://datasets.datalad.org/shub/GeertvanGeest/test_shub/latest/2021-04-12-89592aba-309ef2d6/
recipe: https://datasets.datalad.org/shub/GeertvanGeest/test_shub/latest/2021-04-12-89592aba-309ef2d6/Singularity
collection: GeertvanGeest/test_shub
---

# GeertvanGeest/test_shub:latest

```bash
$ singularity pull shub://GeertvanGeest/test_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:16.04

%labels
MAINTAINER Vanessasaur
SPECIES Dinosaur

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!"
exec /bin/bash /code/rawr.sh "$@"

%post
echo "This section happens once after bootstrap to build the image."
mkdir -p /code
apt-get update
apt-get -y install vim
echo 'echo $@' >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [GeertvanGeest/test_shub](https://github.com/GeertvanGeest/test_shub)
 - License: None

