---
id: 3876
name: "rgrandin/Singularity-Handbrake"
branch: "master"
tag: "fedora28"
commit: "edb2cbacf7577bed8a9f10a4c964713851027b28"
version: "2317bf407d265d996fb694916832ce1a"
build_date: "2018-08-08T03:56:32.216Z"
size_mb: 1007
size: 417480735
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-Handbrake/fedora28/2018-08-08-edb2cbac-2317bf40/2317bf407d265d996fb694916832ce1a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rgrandin/Singularity-Handbrake/fedora28/2018-08-08-edb2cbac-2317bf40/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-Handbrake/fedora28/2018-08-08-edb2cbac-2317bf40/Singularity
collection: rgrandin/Singularity-Handbrake
---

# rgrandin/Singularity-Handbrake:fedora28

```bash
$ singularity pull shub://rgrandin/Singularity-Handbrake:fedora28
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: fedora:28 


%runscript
    exec ghb


%apprun handbrake
    exec ghb


%post
    dnf install -y https://download0.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download0.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    dnf install -y http://rpms.famillecollet.com/fedora/28/remi/i386/remi-release-28-3.fc28.remi.noarch.rpm

    dnf --enablerepo=remi install -y libdvdcss

    dnf install -y handbrake handbrake-gui
```

## Collection

 - Name: [rgrandin/Singularity-Handbrake](https://github.com/rgrandin/Singularity-Handbrake)
 - License: None

