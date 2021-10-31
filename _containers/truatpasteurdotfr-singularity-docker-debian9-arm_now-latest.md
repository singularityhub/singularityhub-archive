---
id: 2030
name: "truatpasteurdotfr/singularity-docker-debian9-arm_now"
branch: "master"
tag: "latest"
commit: "109268b28f167f0e30768138e5426d58a60e19c3"
version: "4f0ecad265e884c198427c81d444a761"
build_date: "2018-03-13T01:25:23.405Z"
size_mb: 1089
size: 388223007
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-debian9-arm_now/latest/2018-03-13-109268b2-4f0ecad2/4f0ecad265e884c198427c81d444a761.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-debian9-arm_now/latest/2018-03-13-109268b2-4f0ecad2/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-debian9-arm_now/latest/2018-03-13-109268b2-4f0ecad2/Singularity
collection: truatpasteurdotfr/singularity-docker-debian9-arm_now
---

# truatpasteurdotfr/singularity-docker-debian9-arm_now:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-debian9-arm_now:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:stretch
# more details at https://github.com/nongiach/arm_now

%runscript
echo "running arm_now  from the container:"
arm_now "$@"

%post
echo "Hello from inside the container"
sed -i -e 's,http://deb.debian.org,http://cdn-fastly.deb.debian.org,g' /etc/apt/sources.list
apt-get update && apt-get -y upgrade
apt-get -y install python3-pip python3-dev python3  git qemu  e2tools
git clone https://github.com/nongiach/arm_now
cd /arm_now && pip3 install -r requirements.txt && pip3 install .
# e2tools qemu

touch /singularity-`date +%Y%m%d-%H%M%S`

# specific to my setup, required if you don't have overlay support (CentOS-6)
# CentOS-7 host can ignore that mkdir line
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-debian9-arm_now](https://github.com/truatpasteurdotfr/singularity-docker-debian9-arm_now)
 - License: [MIT License](https://api.github.com/licenses/mit)

