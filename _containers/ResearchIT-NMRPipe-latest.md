---
id: 2480
name: "ResearchIT/NMRPipe"
branch: "master"
tag: "latest"
commit: "ec04622479931ba858000e11e9c1c90588e075e1"
version: "330ca2fa55263139b1c6392a17819342"
build_date: "2018-06-11T18:30:27.451Z"
size_mb: 2349
size: 735768607
sif: "https://datasets.datalad.org/shub/ResearchIT/NMRPipe/latest/2018-06-11-ec046224-330ca2fa/330ca2fa55263139b1c6392a17819342.simg"
url: https://datasets.datalad.org/shub/ResearchIT/NMRPipe/latest/2018-06-11-ec046224-330ca2fa/
recipe: https://datasets.datalad.org/shub/ResearchIT/NMRPipe/latest/2018-06-11-ec046224-330ca2fa/Singularity
collection: ResearchIT/NMRPipe
---

# ResearchIT/NMRPipe:latest

```bash
$ singularity pull shub://ResearchIT/NMRPipe:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/ 
#MirrorURL: https://download.fedoraproject.org/pub/fedora/linux/releases/%{OSVERSION}/Everything/$basearch/os/
Include: yum

%environment

%post
yum update -y
yum install -y @"Development Tools"
yum install -y epel-release
yum install -y libgomp cmake3 vim glibc.i686 libgomp.i686 tcsh xterm wget curl unzip lzma gzip zstd lz4
yum install -y git gcc-c++ gcc xorg-x11-fonts-100dpi xorg-x11-fonts-ISO8859-1-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-ISO8859-1-75dpi libX11 libXext libX11 libXext.i686 xterm.i686 libXfont.i686
DEST=/opt/nmrpipe
if [ ! -d $DEST ];
then 
	mkdir $DEST
	pushd $DEST
	wget https://www.ibbr.umd.edu/nmrpipe/NMRPipeX.tZ
	wget https://www.ibbr.umd.edu/nmrpipe/install.com
	wget https://www.ibbr.umd.edu/nmrpipe/binval.com
	wget https://www.ibbr.umd.edu/nmrpipe/s.tZ
	wget https://www.ibbr.umd.edu/nmrpipe/dyn.tZ
	wget https://www.ibbr.umd.edu/nmrpipe/talos.tZ
	wget https://spin.niddk.nih.gov/bax/software/smile/plugin.smile.tZ
	tcsh install.com +type linux212_64
	rm -f *.com *.tZ
	popd
fi
ls -la $DEST
cat << EOF > /etc/profile.d/nmrpipe.csh
setenv SHELL /usr/bin/tcsh
set prompt = '[nmrPipe %n@%m]$ '
if (-e /opt/nmrpipe/com/nmrInit.linux212_64.com) then
        source /opt/nmrpipe/com/nmrInit.linux212_64.com
     endif
if (-e /opt/nmrpipe/dynamo/com/dynInit.com) then
        source /opt/nmrpipe/dynamo/com/dynInit.com
     endif
EOF

%runscript
exec /usr/bin/tcsh
```

## Collection

 - Name: [ResearchIT/NMRPipe](https://github.com/ResearchIT/NMRPipe)
 - License: None

