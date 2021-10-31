---
id: 12730
name: "mcw-rcc/rstudio-server"
branch: "1.2.5042"
tag: "1.2.5042"
commit: "51252cda7426179c4b543ac64b1adb68ff3ed78e"
version: "49f1bfcb0654bd96ca748760c05708b06324fcb9c01c1841fd14da2b30763a01"
build_date: "2020-07-09T18:15:01.053Z"
size_mb: 843.0
size: 292298752
sif: "https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.2.5042/2020-07-09-51252cda-49f1bfcb/49f1bfcb0654bd96ca748760c05708b06324fcb9c01c1841fd14da2b30763a01.sif"
url: https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.2.5042/2020-07-09-51252cda-49f1bfcb/
recipe: https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.2.5042/2020-07-09-51252cda-49f1bfcb/Singularity
collection: mcw-rcc/rstudio-server
---

# mcw-rcc/rstudio-server:1.2.5042

```bash
$ singularity pull shub://mcw-rcc/rstudio-server:1.2.5042
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mcw-rcc/r-base:3.5.0

%help
    This container runs RStudio Server.

%labels
    Maintainer Matthew Flister

%apprun rserver
    exec rserver "${@}"

%runscript
    exec rserver "${@}"

%environment
    export PATH=/usr/lib/rstudio-server/bin:${PATH}

%setup
    install -Dv \
    pam_help.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/pam_help
    install -Dv \
    rserver.conf \
    ${SINGULARITY_ROOTFS}/etc/rstudio/rserver.conf

%post
    # create dirs and modulefile config
    yum install -y environment-modules
    mkdir -p /cm/local /cm/shared
    cat <<EOF >> /usr/share/Modules/init/.modulespath
    /cm/local/modulefiles
    /cm/shared/modulefiles
    /cm/shared/rcc/modulefiles
    EOF

    # install rstudio
    wget https://download2.rstudio.org/server/centos6/x86_64/rstudio-server-rhel-1.2.5042-x86_64.rpm
    yum install -y rstudio-server-rhel-1.2.5042-x86_64.rpm
    rm -rf rstudio-server-rhel-1.2.5042-x86_64.rpm
    yum clean all
    rm -rf /var/cache/yum/*
    echo "R_LIBS=/extR/library1:/extR/library2" > /opt/R/3.5.0/lib64/R/etc/Renviron.site
```

## Collection

 - Name: [mcw-rcc/rstudio-server](https://github.com/mcw-rcc/rstudio-server)
 - License: [MIT License](https://api.github.com/licenses/mit)

