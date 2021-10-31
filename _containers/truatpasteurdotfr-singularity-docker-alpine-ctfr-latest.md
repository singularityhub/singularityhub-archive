---
id: 2028
name: "truatpasteurdotfr/singularity-docker-alpine-ctfr"
branch: "master"
tag: "latest"
commit: "bf2d9573897850f447e6a26a1381bc2171b72818"
version: "6cd640cef08d0e78caf1aae2ea67782d"
build_date: "2018-03-13T01:25:23.365Z"
size_mb: 99
size: 32112671
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-ctfr/latest/2018-03-13-bf2d9573-6cd640ce/6cd640cef08d0e78caf1aae2ea67782d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-alpine-ctfr/latest/2018-03-13-bf2d9573-6cd640ce/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-alpine-ctfr/latest/2018-03-13-bf2d9573-6cd640ce/Singularity
collection: truatpasteurdotfr/singularity-docker-alpine-ctfr
---

# truatpasteurdotfr/singularity-docker-alpine-ctfr:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-alpine-ctfr:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:3.7
# more details at https://github.com/UnaPibaGeek/ctfr

%runscript
echo "running ctfr.py  from the container:"
python3 /ctfr/ctfr.py "$@"

%post
echo "Hello from inside the container"
apk update
apk upgrade
apk add py3-pip python3-dev python3  git
git clone https://github.com/UnaPibaGeek/ctfr.git
cd /ctfr && pip3 install -r requirements.txt

touch /singularity-`date +%Y%m%d-%H%M%S`

# specific to my setup, required if you don't have overlay support (CentOS-6)
# CentOS-7 host can ignore that mkdir line
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-alpine-ctfr](https://github.com/truatpasteurdotfr/singularity-docker-alpine-ctfr)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

