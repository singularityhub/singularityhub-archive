---
id: 11865
name: "matthew-kusz/run-xterm"
branch: "master"
tag: "latest"
commit: "e84b6f2139c45388b17266f5a3a538d92ac3b484"
version: "7f84c294d0b31964c15c79142c8fd938"
build_date: "2019-12-19T14:34:30.406Z"
size_mb: 406.0
size: 136499231
sif: "https://datasets.datalad.org/shub/matthew-kusz/run-xterm/latest/2019-12-19-e84b6f21-7f84c294/7f84c294d0b31964c15c79142c8fd938.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/matthew-kusz/run-xterm/latest/2019-12-19-e84b6f21-7f84c294/
recipe: https://datasets.datalad.org/shub/matthew-kusz/run-xterm/latest/2019-12-19-e84b6f21-7f84c294/Singularity
collection: matthew-kusz/run-xterm
---

# matthew-kusz/run-xterm:latest

```bash
$ singularity pull shub://matthew-kusz/run-xterm:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:centos:7

%runscript
echo "Running xterm..." 
xterm

%post  
echo "Installing xterm..."
yum update -y
yum install -y vim-enhanced
yum install -y xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-apps
yum install -y xterm
yum clean expire-cache
echo "Done."
```

## Collection

 - Name: [matthew-kusz/run-xterm](https://github.com/matthew-kusz/run-xterm)
 - License: None

