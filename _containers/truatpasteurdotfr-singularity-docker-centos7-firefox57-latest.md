---
id: 985
name: "truatpasteurdotfr/singularity-docker-centos7-firefox57"
branch: "master"
tag: "latest"
commit: "c1856949b2caecde89c646598503152a618f7e17"
version: "fa2f040c615beb5ff80a6be188eb0e73"
build_date: "2021-02-08T19:37:43.894Z"
size_mb: 612
size: 221327391
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-firefox57/latest/2021-02-08-c1856949-fa2f040c/fa2f040c615beb5ff80a6be188eb0e73.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-centos7-firefox57/latest/2021-02-08-c1856949-fa2f040c/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-firefox57/latest/2021-02-08-c1856949-fa2f040c/Singularity
collection: truatpasteurdotfr/singularity-docker-centos7-firefox57
---

# truatpasteurdotfr/singularity-docker-centos7-firefox57:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-centos7-firefox57:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7

%post
yum -y update && yum -y upgrade

# you need to create the top level directories since there is no overlay on CentOS-6
# specific to my setup
mkdir -p /local-storage /mnt/beegfs /baycells/home /baycells/scratch /c6/shared /c6/eb /local/gensoft2 /c6/shared/rpm /Bis/Scratch2 /mnt/beegfs /pasteur

# https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US
# 
yum -y install tar bzip2 wget curl
# installing in /opt/firefox
curl 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US' | awk -F'"' '/href/ {print "wget -O - ",$2,"| tar -C /opt  -xjvf -"}'| sh

# pulling from the chrome dependancy chain
yum -y install \
GConf2 \
adwaita-cursor-theme \
adwaita-icon-theme \
alsa-lib \
at \
at-spi2-atk \
at-spi2-core \
atk \
avahi-libs \
bc \
cairo \
cairo-gobject \
colord-libs \
cronie \
cronie-anacron \
crontabs \
cups-client \
cups-libs \
dconf \
desktop-file-utils \
ed \
emacs-filesystem \
file \
fontconfig \
fontpackages-filesystem \
freetype \
gdk-pixbuf2 \
gettext \
gettext-libs \
glib-networking \
gnutls \
graphite2 \
groff-base \
gsettings-desktop-schemas \
gtk-update-icon-cache \
gtk3 \
harfbuzz \
hicolor-icon-theme \
hwdata \
jasper-libs \
jbigkit-libs \
json-glib \
lcms2 \
less \
libX11 \
libX11-common \
libXScrnSaver \
libXau \
libXcomposite \
libXcursor \
libXdamage \
libXext \
libXfixes \
libXft \
libXi \
libXinerama \
libXrandr \
libXrender \
libXt \
libXtst \
libXxf86vm \
libcroco \
libdrm \
libepoxy \
libgomp \
libgusb \
libjpeg-turbo \
libmodman \
libpciaccess \
libpipeline \
libpng \
libproxy \
libsoup \
libthai \
libtiff \
libunistring \
libusbx \
libxcb \
libxshmfence \
m4 \
mailx \
make \
man-db \
mariadb-libs \
mesa-libEGL \
mesa-libGL \
mesa-libgbm \
mesa-libglapi \
mozjs17 \
nettle \
pango \
patch \
pixman \
polkit \
polkit-pkla-compat \
postfix \
psmisc \
redhat-lsb-core \
redhat-lsb-submod-security \
rest \
spax \
stix-fonts \
systemd-sysv \
sysvinit-tools \
time \
trousers \
wget \
which \
xdg-utils                                             
yum -y install mesa-dri-drivers libcanberra-gtk2 libcanberra adwaita-gtk2-theme PackageKit-gtk3-module

%runscript

# you need to bind mount /run for dconf...
/opt/firefox/firefox "$@"
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-centos7-firefox57](https://github.com/truatpasteurdotfr/singularity-docker-centos7-firefox57)
 - License: None

