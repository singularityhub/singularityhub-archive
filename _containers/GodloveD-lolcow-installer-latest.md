---
id: 1170
name: "GodloveD/lolcow-installer"
branch: "master"
tag: "latest"
commit: "554117e7e945766d4ac30d9187c36a179326adb0"
version: "d0b54f0eaac4abd8771b9651f31d513b"
build_date: "2021-03-07T10:44:31.429Z"
size_mb: 253
size: 101179423
sif: "https://datasets.datalad.org/shub/GodloveD/lolcow-installer/latest/2021-03-07-554117e7-d0b54f0e/d0b54f0eaac4abd8771b9651f31d513b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GodloveD/lolcow-installer/latest/2021-03-07-554117e7-d0b54f0e/
recipe: https://datasets.datalad.org/shub/GodloveD/lolcow-installer/latest/2021-03-07-554117e7-d0b54f0e/Singularity
collection: GodloveD/lolcow-installer
---

# GodloveD/lolcow-installer:latest

```bash
$ singularity pull shub://GodloveD/lolcow-installer:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: godlovedc/lolcow:latest

%runscript
    echo
    echo ===============================================
    echo Attempting to install lolcow in ~/lolcow
    echo ===============================================
    echo

    if [ -d "/home/$USER/lolcow" ]; then 
         echo "~/lolcow already exists"
         echo "will not overwrite"
         echo
         exit 1
    fi
  
    mkdir ~/lolcow
    cp -r GodloveD-lolcow-installer* ~/lolcow/image

    cd ~/lolcow
    cat > lolcow.sh <<"EOF"
#!/bin/bash
# if you want to bind some host directories...
# export SINGULARTY_BINDPATH=/some,/dirs,/to,/bind
dir=$(dirname  "$0")
cmd=$(basename "$0")
arg="$@"
singularity exec $dir/image $cmd $arg
EOF
    
    chmod 755 lolcow.sh

    ln -s lolcow.sh fortune
    ln -s lolcow.sh cowsay
    ln -s lolcow.sh lolcat

    cowsay 'type "export PATH=~/lolcow:$PATH" and enjoy fortune, cowsay, and lolcat!' |\
    lolcat
```

## Collection

 - Name: [GodloveD/lolcow-installer](https://github.com/GodloveD/lolcow-installer)
 - License: None

