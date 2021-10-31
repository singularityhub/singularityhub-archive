---
id: 5380
name: "oliviermattelaer/singularity-recipe"
branch: "master"
tag: "python"
commit: "a9c6e9777ede248f6447ec8e3f3ecc2dd6316f7e"
version: "7ad0f058563d39cd90d7981d6883f26f"
build_date: "2018-10-30T15:18:48.355Z"
size_mb: 292
size: 125767711
sif: "https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/python/2018-10-30-a9c6e977-7ad0f058/7ad0f058563d39cd90d7981d6883f26f.simg"
url: https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/python/2018-10-30-a9c6e977-7ad0f058/
recipe: https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/python/2018-10-30-a9c6e977-7ad0f058/Singularity
collection: oliviermattelaer/singularity-recipe
---

# oliviermattelaer/singularity-recipe:python

```bash
$ singularity pull shub://oliviermattelaer/singularity-recipe:python
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
    python /usr/local/bin/helloworld.py $@


%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install  python
    #	        apt-get clean

%files
   helloworld.py /usr/local/bin

%labels
   author Olivier Mattelaer

%environment
    export PATH=$PATH:/usr/games
    export LC_ALL=C
```

## Collection

 - Name: [oliviermattelaer/singularity-recipe](https://github.com/oliviermattelaer/singularity-recipe)
 - License: None

