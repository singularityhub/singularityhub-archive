---
id: 8924
name: "nceglia/scrna-pipeline"
branch: "master"
tag: "latest"
commit: "a39650260bcb48a714149de17925eb0f77e0ee3d"
version: "0b92acbece8c30541d0a7f922a7bd8fb"
build_date: "2019-05-21T02:41:10.553Z"
size_mb: 5663
size: 2514837535
sif: "https://datasets.datalad.org/shub/nceglia/scrna-pipeline/latest/2019-05-21-a3965026-0b92acbe/0b92acbece8c30541d0a7f922a7bd8fb.simg"
url: https://datasets.datalad.org/shub/nceglia/scrna-pipeline/latest/2019-05-21-a3965026-0b92acbe/
recipe: https://datasets.datalad.org/shub/nceglia/scrna-pipeline/latest/2019-05-21-a3965026-0b92acbe/Singularity
collection: nceglia/scrna-pipeline
---

# nceglia/scrna-pipeline:latest

```bash
$ singularity pull shub://nceglia/scrna-pipeline:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nceglia/scrna-pipeline:dev

%help
scrna pipeline meant to be run on juno mskcc.

%files
    lsf.template /codebase/cellranger-3.0.2/martian-cs/v3.2.0/jobmanagers/lsf.template
    run /bin/run

%environment
    export PATH=/codebase/cellranger-3.0.2:$PATH
    export PATH=$PATH:/common/juno/OS7/10.1/linux3.10-glibc2.17-x86_64/bin/
    export NPY_MKL_FORCE_INTEL=GNU

%post
    ln -s /usr/lib/R/lib /usr/local/lib/R/
    chmod 777 /bin/run
    chmod 775 /
    cd /codebase/SCRNApipeline; git pull
    

%runscript
    exec run "$@"
```

## Collection

 - Name: [nceglia/scrna-pipeline](https://github.com/nceglia/scrna-pipeline)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

