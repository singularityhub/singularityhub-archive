---
id: 7693
name: "giovannipizzi/singularity-quantum-espresso"
branch: "master"
tag: "ansible-6.3"
commit: "df81cc42d6cf4fcb6bd382cbe5f1e6053bcb4f0b"
version: "2d981fcf09297357324f060b5297ab56"
build_date: "2020-04-28T08:35:36.747Z"
size_mb: 1998
size: 391520287
sif: "https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/ansible-6.3/2020-04-28-df81cc42-2d981fcf/2d981fcf09297357324f060b5297ab56.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/giovannipizzi/singularity-quantum-espresso/ansible-6.3/2020-04-28-df81cc42-2d981fcf/
recipe: https://datasets.datalad.org/shub/giovannipizzi/singularity-quantum-espresso/ansible-6.3/2020-04-28-df81cc42-2d981fcf/Singularity
collection: giovannipizzi/singularity-quantum-espresso
---

# giovannipizzi/singularity-quantum-espresso:ansible-6.3

```bash
$ singularity pull shub://giovannipizzi/singularity-quantum-espresso:ansible-6.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: marvelnccr/ubuntu-docker-base:2.2

%files
   playbook.yml /tmp/quantum-espresso-ansible-playbook.yml


%post
    ansible-galaxy install -p /tmp marvel-nccr.quantum_espresso
    ansible-playbook /tmp/quantum-espresso-ansible-playbook.yml
    apt-get -y clean
    cp --dereference /tmp//q-e-90a2aa88298f5005b8ab8f5fcc354c5870481d68/bin/*.x /usr/local/bin/

%environment
    export LC_ALL=en_US.UTF-8
    export ANSIBLE_ROLES_PATH=/tmp

%runscript
    echo "Quantum ESPRESSO is installed (using the marvel-nccr.quantum_espresso Ansible role) in this singularity file. Just run pw.x or one of the other Quantum ESPRESSO codes."
```

## Collection

 - Name: [giovannipizzi/singularity-quantum-espresso](https://github.com/giovannipizzi/singularity-quantum-espresso)
 - License: None

