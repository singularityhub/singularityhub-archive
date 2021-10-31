---
id: 1721
name: "jekriske/rstudio"
branch: "master"
tag: "1.1.423_desktop"
commit: "c76a1de2a7c90deeea8afcc999e47d9879fa6498"
version: "efaa2e667ed84dae88e5c1f703e2fac2"
build_date: "2020-01-09T08:22:45.698Z"
size_mb: 1400
size: 517050399
sif: "https://datasets.datalad.org/shub/jekriske/rstudio/1.1.423_desktop/2020-01-09-c76a1de2-efaa2e66/efaa2e667ed84dae88e5c1f703e2fac2.simg"
url: https://datasets.datalad.org/shub/jekriske/rstudio/1.1.423_desktop/2020-01-09-c76a1de2-efaa2e66/
recipe: https://datasets.datalad.org/shub/jekriske/rstudio/1.1.423_desktop/2020-01-09-c76a1de2-efaa2e66/Singularity
collection: jekriske/rstudio
---

# jekriske/rstudio:1.1.423_desktop

```bash
$ singularity pull shub://jekriske/rstudio:1.1.423_desktop
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jekriske/r-base

%labels
  Maintainer Jeff Kriske
  Version v0.0.5
  Rstudio_Version 1.1.423

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
                 https://download1.rstudio.org/rstudio-1.1.423-x86_64.rpm
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

