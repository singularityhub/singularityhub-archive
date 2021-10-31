---
id: 3545
name: "rgrandin/Singularity-Photography"
branch: "master"
tag: "latest"
commit: "f5721b73caa8831da8d79729c7b237f8e801937f"
version: "c0176872347dfab6afcd6a2a40f3796c"
build_date: "2020-05-10T18:40:25.351Z"
size_mb: 1328
size: 629014559
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-Photography/latest/2020-05-10-f5721b73-c0176872/c0176872347dfab6afcd6a2a40f3796c.simg"
url: https://datasets.datalad.org/shub/rgrandin/Singularity-Photography/latest/2020-05-10-f5721b73-c0176872/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-Photography/latest/2020-05-10-f5721b73-c0176872/Singularity
collection: rgrandin/Singularity-Photography
---

# rgrandin/Singularity-Photography:latest

```bash
$ singularity pull shub://rgrandin/Singularity-Photography:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic 
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    echo ""
    echo "Available programs:"
    echo "    Panorama Stitching"
    echo "        hugin"
    #echo "    Panorama Viewing"
    #echo "        Panini"
    echo "    RAW Photo Editing"
    echo "        darktable"
    echo "        rawtherapee" 
    #echo "        lightzone"
    echo "    HDR Photos"
    echo "        luminance-hdr"
    #echo "        hdrmerge"
    echo "    Photo Combination"
    echo "        photocollage"
    echo ""
    echo "Run a program with:    singularity exec <Container Name> <PROGRAM>"
    echo ""


%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    
    apt-get -y install software-properties-common #python-software-properties
    add-apt-repository ppa:ubuntuhandbook1/apps
    add-apt-repository ppa:dhor/myway

    apt-get -y update

    apt-get -y --force-yes install vim hugin darktable rawtherapee photocollage luminance-hdr
```

## Collection

 - Name: [rgrandin/Singularity-Photography](https://github.com/rgrandin/Singularity-Photography)
 - License: None

