---
id: 3875
name: "rgrandin/Singularity-Handbrake"
branch: "master"
tag: "latest"
commit: "b28377750dcdc37406d8bcc9352d3f04efb9b81f"
version: "1066e54878bd752774fdc267db8f0870"
build_date: "2019-09-09T13:42:25.850Z"
size_mb: 1007
size: 417480735
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-Handbrake/latest/2019-09-09-b2837775-1066e548/1066e54878bd752774fdc267db8f0870.simg"
url: https://datasets.datalad.org/shub/rgrandin/Singularity-Handbrake/latest/2019-09-09-b2837775-1066e548/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-Handbrake/latest/2019-09-09-b2837775-1066e548/Singularity
collection: rgrandin/Singularity-Handbrake
---

# rgrandin/Singularity-Handbrake:latest

```bash
$ singularity pull shub://rgrandin/Singularity-Handbrake:latest
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

