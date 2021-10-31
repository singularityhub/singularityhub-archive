---
id: 3966
name: "omento/singularity"
branch: "master"
tag: "cent7"
commit: "a8db86bcf785eec38cac90ad4cd002109db8ea9b"
version: "64b446622f4d6995bc91aee8a4c2feec"
build_date: "2018-08-16T17:20:05.712Z"
size_mb: 291
size: 86814751
sif: "https://datasets.datalad.org/shub/omento/singularity/cent7/2018-08-16-a8db86bc-64b44662/64b446622f4d6995bc91aee8a4c2feec.simg"
url: https://datasets.datalad.org/shub/omento/singularity/cent7/2018-08-16-a8db86bc-64b44662/
recipe: https://datasets.datalad.org/shub/omento/singularity/cent7/2018-08-16-a8db86bc-64b44662/Singularity
collection: omento/singularity
---

# omento/singularity:cent7

```bash
$ singularity pull shub://omento/singularity:cent7
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-7/7.5.1804/os/$basearch/
Include: yum yum-plugin-ovl vim-minimal less man which tzdata

%labels
    Maintainer omento

%help
A baseline container of CentOS 7

%environment
    LC_ALL=C
    LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib:/usr/lib64:/usr/lib
    TZ='America/New_York'

    export LC_ALL LD_LIBRARY_PATH TZ

%post
    ## Clear yum cache
    yum clean all
    rm -rf /var/cache/yum

    ## Lock mirror location, disable fastest mirror, and update
    sed -i '18ienabled=0' /etc/yum.repos.d/CentOS-Base.repo
    sed -i '27ienabled=0' /etc/yum.repos.d/CentOS-Base.repo
    sed -i '35ienabled=0' /etc/yum.repos.d/CentOS-Base.repo
    printf "[C7.5-base]\nname=CentOS-7.5.1804 - Base\nbaseurl=http://mirror.centos.org/centos-7/7.5.1804/os/\$basearch/\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7\nenabled=1\n\n[C7.5-updates]\nname=CentOS-7.5.1804 - Updates\nbaseurl=http://mirror.centos.org/centos-7/7.5.1804/updates/\$basearch/\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7\nenabled=1\n\n[C7.5-extras]\nname=CentOS-7.5.1804 - Extras\nbaseurl=http://mirror.centos.org/centos-7/7.5.1804/extras/\$basearch/\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7\nenabled=1\n\n[C7.5-centosplus]\nname=CentOS-7.5.1804 - CentOSPlus\nbaseurl=http://mirror.centos.org/centos-7/7.5.1804/centosplus/\$basearch/\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7\nenabled=0\n\n[C7.5-fasttrack]\nname=CentOS-7.5.1804 - CentOSPlus\nbaseurl=http://mirror.centos.org/centos-7/7.5.1804/fasttrack/\$basearch/\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7\nenabled=0\n" > /etc/yum.repos.d/CentOS-7.5.repo
    sed -i 's|enabled=1|enabled=0|g' /etc/yum/pluginconf.d/fastestmirror.conf
    echo "Repos fixed: Updating..."
    yum -y update
    yum clean all
    rm -rf /var/cache/yum

%test
    echo "Image Build Date: $(date)"
    cat /etc/centos-release

%runscript
    cat /etc/centos-release
    echo "Image Build Date: 16.08.2018"
```

## Collection

 - Name: [omento/singularity](https://github.com/omento/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

