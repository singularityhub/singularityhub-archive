---
id: 2282
name: "jekriske/rstudio"
branch: "master"
tag: "1.1.442_desktop"
commit: "848ab02e5c9beda6a1e84af962388842c8b53413"
version: "e312e0fac80aac2c8fe9606c720f7f0c"
build_date: "2020-10-21T08:49:22.160Z"
size_mb: 1342
size: 499593247
sif: "https://datasets.datalad.org/shub/jekriske/rstudio/1.1.442_desktop/2020-10-21-848ab02e-e312e0fa/e312e0fac80aac2c8fe9606c720f7f0c.simg"
url: https://datasets.datalad.org/shub/jekriske/rstudio/1.1.442_desktop/2020-10-21-848ab02e-e312e0fa/
recipe: https://datasets.datalad.org/shub/jekriske/rstudio/1.1.442_desktop/2020-10-21-848ab02e-e312e0fa/Singularity
collection: jekriske/rstudio
---

# jekriske/rstudio:1.1.442_desktop

```bash
$ singularity pull shub://jekriske/rstudio:1.1.442_desktop
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jekriske/r-base

%labels
  Maintainer Jeff Kriske
  Version v0.0.5
  Rstudio_Version 1.1.442

%help
  This will run Rstudio Desktop

%runscript
  exec rstudio "$@"

%apprun rstudio
  exec rstudio "$@"

%post
  yum update -y
  yum install -y libxbcommon \
                 libxkbcommon \
                 libxkbcommon-x11 \
                 mesa-dri-drivers \
                 dejavu-sans-mono-fonts \
                 abattis-cantarell-fonts \
                 open-sans-fonts \
                 xorg-x11-server-utils \
                 https://download1.rstudio.org/rstudio-1.1.442-x86_64.rpm
  yum clean all && rm -rf /var/cache/yum
  cat <<EOT >> /etc/fonts/local.conf
    <match target="font">
    <edit name="autohint" mode="assign">
      <bool>true</bool>
    </edit>
    <edit name="hinting" mode="assign">
      <bool>true</bool>
    </edit>
    <edit mode="assign" name="hintstyle">
      <const>hintslight</const>
    </edit>
    <edit mode="assign" name="lcdfilter">
      <const>lcddefault</const>
    </edit>
    </match>
EOT
```

## Collection

 - Name: [jekriske/rstudio](https://github.com/jekriske/rstudio)
 - License: None

