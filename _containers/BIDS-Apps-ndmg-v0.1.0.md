---
id: 1519
name: "BIDS-Apps/ndmg"
branch: "master"
tag: "v0.1.0"
commit: "3a63bab68ee0b07760eed2c8a1400925629e7c8d"
version: "73044bf715dc6d766cec324b4cede9b8"
build_date: "2020-07-29T06:45:52.709Z"
size_mb: 2018
size: 914759711
sif: "https://datasets.datalad.org/shub/BIDS-Apps/ndmg/v0.1.0/2020-07-29-3a63bab6-73044bf7/73044bf715dc6d766cec324b4cede9b8.simg"
url: https://datasets.datalad.org/shub/BIDS-Apps/ndmg/v0.1.0/2020-07-29-3a63bab6-73044bf7/
recipe: https://datasets.datalad.org/shub/BIDS-Apps/ndmg/v0.1.0/2020-07-29-3a63bab6-73044bf7/Singularity
collection: BIDS-Apps/ndmg
---

# BIDS-Apps/ndmg:v0.1.0

```bash
$ singularity pull shub://BIDS-Apps/ndmg:v0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bids/ndmg

%help
You are in the BIDS-ndmg container. To see help run
singularity run BIDS-ndmg.simg -h

%runscript
    exec ndmg_bids "$@"

%labels
Author greg.kiar@mail.mcgill.ca
Build-date 30/01/2018
Vendor Ubuntu
Version v0.1.0

%post
    echo "For more information on ndmg, go to:"
    echo "http://m2g.io"
```

## Collection

 - Name: [BIDS-Apps/ndmg](https://github.com/BIDS-Apps/ndmg)
 - License: None

