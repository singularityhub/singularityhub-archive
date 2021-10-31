---
id: 15351
name: "romxero/pdftk-singularity"
branch: "main"
tag: "latest"
commit: "cc2f507efea9d1be50e12a7b7c4717c673b6516c"
version: "c3f6e4b20c8a98bbee53093eb4cb3961"
build_date: "2021-01-21T03:49:56.042Z"
size_mb: 486.0
size: 151425055
sif: "https://datasets.datalad.org/shub/romxero/pdftk-singularity/latest/2021-01-21-cc2f507e-c3f6e4b2/c3f6e4b20c8a98bbee53093eb4cb3961.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/pdftk-singularity/latest/2021-01-21-cc2f507e-c3f6e4b2/
recipe: https://datasets.datalad.org/shub/romxero/pdftk-singularity/latest/2021-01-21-cc2f507e-c3f6e4b2/Singularity
collection: romxero/pdftk-singularity
---

# romxero/pdftk-singularity:latest

```bash
$ singularity pull shub://romxero/pdftk-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos6.9

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#########
#%setup
#########

#Downlaod packages
%post



cat <<-'EOF' > /etc/yum.repos.d/CentOS-Base.repo
[C6.10-base]
name=CentOS-6.10 - Base
baseurl=http://vault.centos.org/6.10/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
enabled=1
metadata_expire=never

[C6.10-updates]
name=CentOS-6.10 - Updates
baseurl=http://vault.centos.org/6.10/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
enabled=1
metadata_expire=never

[C6.10-extras]
name=CentOS-6.10 - Extras
baseurl=http://vault.centos.org/6.10/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
enabled=1
metadata_expire=never

[C6.10-contrib]
name=CentOS-6.10 - Contrib
baseurl=http://vault.centos.org/6.10/contrib/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
enabled=0
metadata_expire=never

[C6.10-centosplus]
name=CentOS-6.10 - CentOSPlus
baseurl=http://vault.centos.org/6.10/centosplus/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
enabled=0
metadata_expire=never
EOF

  yum -y update
  yum -y install libgcj wget curl
  
  

#grabbing cfas
mkdir /pdftk_
cd /pdftk_
wget https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk-2.02-1.el6.x86_64.rpm
rpm -i pdftk-2.02-1.*.rpm

%environment
  export IMAGE_NAME="pdftk"
%runscript
###



#####
```

## Collection

 - Name: [romxero/pdftk-singularity](https://github.com/romxero/pdftk-singularity)
 - License: None

