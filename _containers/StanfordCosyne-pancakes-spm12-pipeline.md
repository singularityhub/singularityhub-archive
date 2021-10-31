---
id: 1596
name: "StanfordCosyne/pancakes"
branch: "master"
tag: "spm12-pipeline"
commit: "599d0ad5fba9ac24932650f569df856fe6556459"
version: "80787c6348ffc81c92098989dda27b57"
build_date: "2018-02-13T08:25:31.530Z"
size_mb: 4109
size: 1864642591
sif: "https://datasets.datalad.org/shub/StanfordCosyne/pancakes/spm12-pipeline/2018-02-13-599d0ad5-80787c63/80787c6348ffc81c92098989dda27b57.simg"
url: https://datasets.datalad.org/shub/StanfordCosyne/pancakes/spm12-pipeline/2018-02-13-599d0ad5-80787c63/
recipe: https://datasets.datalad.org/shub/StanfordCosyne/pancakes/spm12-pipeline/2018-02-13-599d0ad5-80787c63/Singularity
collection: StanfordCosyne/pancakes
---

# StanfordCosyne/pancakes:spm12-pipeline

```bash
$ singularity pull shub://StanfordCosyne/pancakes:spm12-pipeline
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: StanfordCosyne/pancakes:spm12

# 
# sudo singularity build spm12 Singularity.spm12
# sudo singularity build --sandbox spm12-dev Singularity.spm12
#

%files
    spm12-pipeline.scif
    preprocessmri
    preprocessfmri

%post

    #############################
    # Scientific Filesystem
    #############################

    /opt/conda/bin/pip install scif
    /opt/conda/bin/scif install /spm12-pipeline.scif    
    rm -rf /spm

%runscript

    HOME=$(mktemp -d --suffix=.matlab)
    export HOME

    if [ $# -eq 0 ]
        then
        exec ${SPM_EXEC} script $@
    else
        exec scif run "$@"
    fi
```

## Collection

 - Name: [StanfordCosyne/pancakes](https://github.com/StanfordCosyne/pancakes)
 - License: None

