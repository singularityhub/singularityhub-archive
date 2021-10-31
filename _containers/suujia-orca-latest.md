---
id: 3908
name: "suujia/orca"
branch: "linuxbrew"
tag: "latest"
commit: "d18aa69cb0772fab2f8ec6dc3525c28e19d14a25"
version: "4c4aab7e2cb608fcfb94bb03483cefe1"
build_date: "2018-08-13T18:43:12.908Z"
size_mb: 2669
size: 1434456095
sif: "https://datasets.datalad.org/shub/suujia/orca/latest/2018-08-13-d18aa69c-4c4aab7e/4c4aab7e2cb608fcfb94bb03483cefe1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/suujia/orca/latest/2018-08-13-d18aa69c-4c4aab7e/
recipe: https://datasets.datalad.org/shub/suujia/orca/latest/2018-08-13-d18aa69c-4c4aab7e/Singularity
collection: suujia/orca
---

# suujia/orca:latest

```bash
$ singularity pull shub://suujia/orca:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
	# print out software versions installed by linuxbrew
	find /Software/brew/Cellar -maxdepth 2 -print | sed 's|/Software/brew/Cellar||g' | sed 's|^/||' | grep "/" | sed 's|/|\t|' | sort | awk '{print $1, $2, "Homebrew"}' | column -t | sort -u --ignore-case

%post
	sed -i 's/$/ universe/' /etc/apt/sources.list
	locale-gen "en_US.UTF-8"
	dpkg-reconfigure locales
	export LANGUAGE="en_US.UTF-8"
	echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
	echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers

    mkdir /Software /scratch
	chmod 777 /scratch
	chmod +t /scratch
	chmod 777 /Software

    apt-get update \
        && apt-get install -y --no-install-recommends \
                bzip2 \
                ca-certificates \
                curl \
                file \
                fonts-dejavu-core \
                g++ \
                git \
                locales \
                make \
                openssh-client \
                patch \
                sudo \
                uuid-runtime \
        && rm -rf /var/lib/apt/lists/*

	useradd -m -s /bin/bash linuxbrew
	su -c 'cd /Software && git clone https://github.com/Linuxbrew/brew.git' linuxbrew

    export HOMEBREW_NO_ANALYTICS=1 HOMEBREW_NO_AUTO_UPDATE=1 
    su -c '/Software/brew/bin/brew tap homebrew/core' linuxbrew
    rm -rf ~/.cache

    # test brew install brewsci tools 
    su -c '/Software/brew/bin/brew update' linuxbrew
    su -c '/Software/brew/bin/brew tap brewsci/bio' linuxbrew
    su -c '/Software/brew/bin/brew install \
    matplotlib \
    nextflow' linuxbrew

    sed -i 's|PATH=$PATH:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin|PATH="/Software/brew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"|' /environment
```

## Collection

 - Name: [suujia/orca](https://github.com/suujia/orca)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

