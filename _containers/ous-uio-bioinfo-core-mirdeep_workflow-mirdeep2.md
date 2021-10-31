---
id: 14313
name: "ous-uio-bioinfo-core/mirdeep_workflow"
branch: "master"
tag: "mirdeep2"
commit: "746bc193a37794de619d35aa6fdbd9deb308cb2f"
version: "9af661eacb0362e659803296d69c7117f6995e55c49fcf62befd5c0ff9f4cbe8"
build_date: "2020-11-04T14:21:52.183Z"
size_mb: 326.16015625
size: 342003712
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/mirdeep_workflow/mirdeep2/2020-11-04-746bc193-9af661ea/9af661eacb0362e659803296d69c7117f6995e55c49fcf62befd5c0ff9f4cbe8.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/mirdeep_workflow/mirdeep2/2020-11-04-746bc193-9af661ea/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/mirdeep_workflow/mirdeep2/2020-11-04-746bc193-9af661ea/Singularity
collection: ous-uio-bioinfo-core/mirdeep_workflow
---

# ous-uio-bioinfo-core/mirdeep_workflow:mirdeep2

```bash
$ singularity pull shub://ous-uio-bioinfo-core/mirdeep_workflow:mirdeep2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: forrestzhang/docker-mirdeep2:latest 

%environment
    PATH="/opt/software/mirdeep2:${PATH}"
    export PATH

%runscript
    echo "forrestzhang/docker-mirdeep2"
    echo "PATH=${PATH}"
    exec /bin/bash "$@"

%post
    sed s'/^test_input_files();/#test_input_files();/' /opt/software/mirdeep2/miRDeep2.pl > /opt/software/mirdeep2/miRDeep2.no_input_tests.pl
    chmod ugo+rwx /opt/software/mirdeep2/mapper.pl
    chmod ugo+rwx /opt/software/mirdeep2/miRDeep2.no_input_tests.pl
    mkdir /cluster /work /usit /projects
```

## Collection

 - Name: [ous-uio-bioinfo-core/mirdeep_workflow](https://github.com/ous-uio-bioinfo-core/mirdeep_workflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

