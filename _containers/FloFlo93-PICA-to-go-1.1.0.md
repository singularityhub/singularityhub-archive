---
id: 5135
name: "FloFlo93/PICA-to-go"
branch: "master"
tag: "1.1.0"
commit: "cef7afa4096ff2743cf3396485245ca7335949ef"
version: "b6b16e0155c2d7e0ad870be007d9fdb4"
build_date: "2019-07-27T18:17:10.045Z"
size_mb: 857
size: 330362911
sif: "https://datasets.datalad.org/shub/FloFlo93/PICA-to-go/1.1.0/2019-07-27-cef7afa4-b6b16e01/b6b16e0155c2d7e0ad870be007d9fdb4.simg"
url: https://datasets.datalad.org/shub/FloFlo93/PICA-to-go/1.1.0/2019-07-27-cef7afa4-b6b16e01/
recipe: https://datasets.datalad.org/shub/FloFlo93/PICA-to-go/1.1.0/2019-07-27-cef7afa4-b6b16e01/Singularity
collection: FloFlo93/PICA-to-go
---

# FloFlo93/PICA-to-go:1.1.0

```bash
$ singularity pull shub://FloFlo93/PICA-to-go:1.1.0
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# curl (to install Java 10)
%appinstall curl
yum install curl
 
# java-jre10 
%appinstall java-jre10
curl -L -b "oraclelicense=a" -O http://download.oracle.com/otn-pub/java/jdk/10.0.2+13/19aef61b38124481863b1413dce1855f/jre-10.0.2_linux-x64_bin.rpm
yum -y localinstall jre-10.0.2_linux-x64_bin.rpm

# tar
%appinstall tar
yum -y install tar

# xz
%appinstall xz
yum -y install xz

# pica-to-go
%appinstall pica-to-go
curl -LO https://github.com/FloFlo93/PICA-to-go/releases/download/1.1.0/PICA-to-go-1.1.0.tar.xz
tar -xf PICA-to-go-1.1.0.tar.xz
rm -rf PICA-to-go-1.1.0.tar.xz
mkdir /opt/pica-to-go/
mv bin /opt/pica-to-go/

# numpy
%appinstall numpy
yum -y install numpy

# runscript
%runscript 
/opt/pica-to-go/bin/pica-to-go $@
```

## Collection

 - Name: [FloFlo93/PICA-to-go](https://github.com/FloFlo93/PICA-to-go)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

