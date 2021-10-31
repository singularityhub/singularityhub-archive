---
id: 13007
name: "timothydgreer/GSoC_2020"
branch: "master"
tag: "latest"
commit: "a88f615320b31e63acd0b3e1c5fef12f2697e860"
version: "d0de884cf89cf5aafd283068075b0912"
build_date: "2020-05-13T19:19:47.720Z"
size_mb: 79.0
size: 27725855
sif: "https://datasets.datalad.org/shub/timothydgreer/GSoC_2020/latest/2020-05-13-a88f6153-d0de884c/d0de884cf89cf5aafd283068075b0912.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/timothydgreer/GSoC_2020/latest/2020-05-13-a88f6153-d0de884c/
recipe: https://datasets.datalad.org/shub/timothydgreer/GSoC_2020/latest/2020-05-13-a88f6153-d0de884c/Singularity
collection: timothydgreer/GSoC_2020
---

# timothydgreer/GSoC_2020:latest

```bash
$ singularity pull shub://timothydgreer/GSoC_2020:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

%labels
MAINTAINER timothydgreer


%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This is singularity with tag"
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [timothydgreer/GSoC_2020](https://github.com/timothydgreer/GSoC_2020)
 - License: [MIT License](https://api.github.com/licenses/mit)

