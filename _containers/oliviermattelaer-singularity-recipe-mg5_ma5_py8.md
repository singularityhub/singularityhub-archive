---
id: 5633
name: "oliviermattelaer/singularity-recipe"
branch: "master"
tag: "mg5_ma5_py8"
commit: "181d4caac36ca16b057431da34fb963681ac15b8"
version: "5ca2dcd491421950ac17319871eb3111"
build_date: "2020-10-08T16:24:35.140Z"
size_mb: 4238
size: 2283933727
sif: "https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/mg5_ma5_py8/2020-10-08-181d4caa-5ca2dcd4/5ca2dcd491421950ac17319871eb3111.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/oliviermattelaer/singularity-recipe/mg5_ma5_py8/2020-10-08-181d4caa-5ca2dcd4/
recipe: https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/mg5_ma5_py8/2020-10-08-181d4caa-5ca2dcd4/Singularity
collection: oliviermattelaer/singularity-recipe
---

# oliviermattelaer/singularity-recipe:mg5_ma5_py8

```bash
$ singularity pull shub://oliviermattelaer/singularity-recipe:mg5_ma5_py8
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: oliviermattelaer/singularity-recipe:mg5_alone

%runscript
    /usr/mg5amcnlo/bin/mg5_aMC


%post
    # PY8 specific
    apt-get -y install rsync
    # MA5 specific
    cd /usr
    echo "install pythia8;" > cmd.py8
    ./mg5amcnlo/bin/mg5 cmd.py8

    # for PY8
    chmod 777 /usr/mg5amcnlo/HEPTools/pythia8/bin/pythia8-config
```

## Collection

 - Name: [oliviermattelaer/singularity-recipe](https://github.com/oliviermattelaer/singularity-recipe)
 - License: None

