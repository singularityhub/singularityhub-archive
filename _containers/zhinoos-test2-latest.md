---
id: 12768
name: "zhinoos/test2"
branch: "master"
tag: "latest"
commit: "50d09a64e5f2f3ac75cec9bde5e012c5fbc8fc91"
version: "9cea22571e85c79270af538c95e6f88d"
build_date: "2020-04-21T15:04:24.630Z"
size_mb: 95.0
size: 37040159
sif: "https://datasets.datalad.org/shub/zhinoos/test2/latest/2020-04-21-50d09a64-9cea2257/9cea22571e85c79270af538c95e6f88d.sif"
url: https://datasets.datalad.org/shub/zhinoos/test2/latest/2020-04-21-50d09a64-9cea2257/
recipe: https://datasets.datalad.org/shub/zhinoos/test2/latest/2020-04-21-50d09a64-9cea2257/Singularity
collection: zhinoos/test2
---

# zhinoos/test2:latest

```bash
$ singularity pull shub://zhinoos/test2:latest
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
exec https://github.com/zhinoos/test2/blob/master/rawr.sh
%/bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
%apt-get install vim  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [zhinoos/test2](https://github.com/zhinoos/test2)
 - License: None

