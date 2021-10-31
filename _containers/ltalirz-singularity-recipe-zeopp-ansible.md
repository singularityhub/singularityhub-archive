---
id: 7983
name: "ltalirz/singularity-recipe-zeopp"
branch: "master"
tag: "ansible"
commit: "2024304e981845f50d73e035559ef2df31841bb2"
version: "dc8bbf823e5eed2c8c997cdf0e51778e"
build_date: "2019-10-08T18:37:30.597Z"
size_mb: 702
size: 198422559
sif: "https://datasets.datalad.org/shub/ltalirz/singularity-recipe-zeopp/ansible/2019-10-08-2024304e-dc8bbf82/dc8bbf823e5eed2c8c997cdf0e51778e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ltalirz/singularity-recipe-zeopp/ansible/2019-10-08-2024304e-dc8bbf82/
recipe: https://datasets.datalad.org/shub/ltalirz/singularity-recipe-zeopp/ansible/2019-10-08-2024304e-dc8bbf82/Singularity
collection: ltalirz/singularity-recipe-zeopp
---

# ltalirz/singularity-recipe-zeopp:ansible

```bash
$ singularity pull shub://ltalirz/singularity-recipe-zeopp:ansible
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: marvelnccr/ubuntu-docker-base:2.2

%files
   playbook.yml /tmp/playbook.yml


%post
    ansible-galaxy install -p /tmp marvel-nccr.zeopp
    ansible-playbook /tmp/playbook.yml
    apt-get -y clean
    cp --dereference /tmp/zeoplusplus/network /usr/local/bin/
    cp --dereference /tmp/zeoplusplus/voro++/src/voro++ /usr/local/bin/

%environment
    export LC_ALL=en_US.UTF-8
    export ANSIBLE_ROLES_PATH=/tmp

%runscript
    echo "zeo++ is installed using the marvel-nccr.zeopp Ansible role. Just run network or voro++."
```

## Collection

 - Name: [ltalirz/singularity-recipe-zeopp](https://github.com/ltalirz/singularity-recipe-zeopp)
 - License: None

