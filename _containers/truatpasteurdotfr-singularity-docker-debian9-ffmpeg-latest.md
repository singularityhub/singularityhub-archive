---
id: 5157
name: "truatpasteurdotfr/singularity-docker-debian9-ffmpeg"
branch: "master"
tag: "latest"
commit: "bb5573b2f2e923b6ee5424bf50763a7b22fe155b"
version: "7e19ed60984f5b405f6863dd21aa8c1c"
build_date: "2018-10-07T18:30:41.818Z"
size_mb: 384
size: 158109727
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-debian9-ffmpeg/latest/2018-10-07-bb5573b2-7e19ed60/7e19ed60984f5b405f6863dd21aa8c1c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-debian9-ffmpeg/latest/2018-10-07-bb5573b2-7e19ed60/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-debian9-ffmpeg/latest/2018-10-07-bb5573b2-7e19ed60/Singularity
collection: truatpasteurdotfr/singularity-docker-debian9-ffmpeg
---

# truatpasteurdotfr/singularity-docker-debian9-ffmpeg:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-debian9-ffmpeg:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9

%post
export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get -y upgrade
apt-get -y install ffmpeg  # that should be enough, imho 

# specific to my setup
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs

%runscript
echo "running ffmpeg from the container"
ffmpeg "$@"
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-debian9-ffmpeg](https://github.com/truatpasteurdotfr/singularity-docker-debian9-ffmpeg)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

