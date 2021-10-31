---
id: 1172
name: "whit2333/shub"
branch: "master"
tag: "dd4hep"
commit: "0332f523a87ad2d2a209f1a423c1a7d871d48d2a"
version: "180cddf2a27e9460ec1415664478beb2"
build_date: "2018-01-01T00:44:31.242Z"
size_mb: 3943
size: 1763577887
sif: "https://datasets.datalad.org/shub/whit2333/shub/dd4hep/2018-01-01-0332f523-180cddf2/180cddf2a27e9460ec1415664478beb2.simg"
url: https://datasets.datalad.org/shub/whit2333/shub/dd4hep/2018-01-01-0332f523-180cddf2/
recipe: https://datasets.datalad.org/shub/whit2333/shub/dd4hep/2018-01-01-0332f523-180cddf2/Singularity
collection: whit2333/shub
---

# whit2333/shub:dd4hep

```bash
$ singularity pull shub://whit2333/shub:dd4hep
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:whit2333/dd4hep-base:latest

%labels
MAINTAINER Derp
SPECIES butt

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!" 
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
apt-get install vim  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [whit2333/shub](https://github.com/whit2333/shub)
 - License: None

