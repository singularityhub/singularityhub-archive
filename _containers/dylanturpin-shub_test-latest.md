---
id: 11728
name: "dylanturpin/shub_test"
branch: "master"
tag: "latest"
commit: "ea8454a3721ba768461b01a077598aeab8cab6f3"
version: "8836f9ce00453775359e31b1cc2c95e5"
build_date: "2019-11-27T21:26:01.253Z"
size_mb: 96.0
size: 37146655
sif: "https://datasets.datalad.org/shub/dylanturpin/shub_test/latest/2019-11-27-ea8454a3-8836f9ce/8836f9ce00453775359e31b1cc2c95e5.sif"
url: https://datasets.datalad.org/shub/dylanturpin/shub_test/latest/2019-11-27-ea8454a3-8836f9ce/
recipe: https://datasets.datalad.org/shub/dylanturpin/shub_test/latest/2019-11-27-ea8454a3-8836f9ce/Singularity
collection: dylanturpin/shub_test
---

# dylanturpin/shub_test:latest

```bash
$ singularity pull shub://dylanturpin/shub_test:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:16.04

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!" 
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [dylanturpin/shub_test](https://github.com/dylanturpin/shub_test)
 - License: None

