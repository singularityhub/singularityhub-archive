---
id: 520
name: "c1t4r/CiTAR-Containers"
branch: "master"
tag: "latest"
commit: "1aa4954b81a8af380c56419c60d2edf9b98e4a22"
version: "15b554e96058e7e85536a10aabcf3359"
build_date: "2017-10-24T10:52:23.345Z"
size_mb: 1527
size: 594362399
sif: "https://datasets.datalad.org/shub/c1t4r/CiTAR-Containers/latest/2017-10-24-1aa4954b-15b554e9/15b554e96058e7e85536a10aabcf3359.simg"
url: https://datasets.datalad.org/shub/c1t4r/CiTAR-Containers/latest/2017-10-24-1aa4954b-15b554e9/
recipe: https://datasets.datalad.org/shub/c1t4r/CiTAR-Containers/latest/2017-10-24-1aa4954b-15b554e9/Singularity
collection: c1t4r/CiTAR-Containers
---

# c1t4r/CiTAR-Containers:latest

```bash
$ singularity pull shub://c1t4r/CiTAR-Containers:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7
IncludeCmd: yes

%runscript
echo "This code is executed as default run script. For now invoke a bash shell..."
/bin/bash

%environment
# These environment settings are needed to make containers run the JUSTUS software stack
module() { eval `/usr/bin/modulecmd sh $*`; }
export MODULEPATH=/opt/bwhpc/ul/modulefiles:/opt/bwhpc/common/modulefiles
export PSM_SHAREDCONTEXTS_MAX=6 # do NOT allocate all HCs, leave remaining HCs for other MPI apps running simultaneously
export PS1="\[\033[01;32m\]\u@${SINGULARITY_CONTAINER}@\h\[\033[01;34m\] \w \$\[\033[00m\] "
# Now import user defined settings
for script in /custom/userenv/*.sh; do
    if [ -f "$script" ]; then
        . $script
    fi
done

%post
    echo "Installing JUSTUS software package list"
    yum -y install deltarpm
    yum -y --skip-broken install \
libXrender linux-firmware dos2unix perl-ExtUtils-Install libsepol hexedit libXi perl-DB_File perl-Compress-Raw-Zlib cairo gawk perl-XML-NamespaceSupport gcc-gnat nfs-utils os-prober ncurses ghostscript-fonts selinux-policy pinentry perl-Test-Simple lvm2 python-iniparse expat libmthca redhat-logos perl-Text-ParseWords libcgroup libthai python-chardet perl-Carp redhat-release-server xdg-utils numactl-devel vim-minimal perl-File-Path nss-softokn-freebl jbigkit-libs perl-Test-Harness perl rsh avahi-libs pth libutempter libgcrypt perl-Net-SSLeay nss-sysinit fipscheck file perl-Env grub2 shared-mime-info perl-HTTP-Daemon libpng12 libaio perl-IO-Socket-SSL bind-license cpp bind-utils libsndfile lustre-client systemd-libs boost-wave binutils boost-random dbus libogg lsscsi polkit-pkla-compat compat-glibc-headers kernel opensm-libs mesa-private-llvm device-mapper-multipath-libs perl-libintl pytz qt pygobject2 rpm-libs blas ghostscript-cups rpm-build-libs bison redhat-lsb-languages libXau iptables gssproxy apr glibc-devel vim-filesystem tzdata-java traceroute mesa-libGL libcap e2fsprogs cups-filters perl-Pod-Parser libgpg-error libXaw perl-Digest glibc-static libcroco dhclient perl-Digest-HMAC sysvinit-tools qt-settings sudo perl-Pod-Checker hardlink perftest gdbm rsync perl-URI perl-Pod-Usage perl-HTML-Format screen perl-constant glibc-common expect perl-Pod-Simple chkconfig m4 gdbm-devel bzip2-libs nss-softokn-freebl libXxf86vm findutils ed libcap-ng passwd tcl perl-HTTP-Cookies numactl-libs perl-File-CheckTree libXfont perl-autodie kmod-libs openssh-clients coreutils boost-thread redhat-lsb-submod-multimedia libmount boost-timer tar autogen-libopts boost-signals librdmacm perl-TermReadKey SMagent munge pycairo xorg-x11-fonts-Type1 cups-filters-libs python-setuptools libssh2 dejavu-sans-fonts dhcp-common numpy libtalloc GConf2 fontpackages-filesystem xterm ncurses-base vim-common iotop ncurses-libs gpgme htop libselinux libacl libXinerama libXdamage perl-XML-SAX-Base readline lockdev make net-tools gettext-libs perl-Socket6 perl-Digest-SHA libverto perl-Pod-LaTeX python-pycurl diffutils qrencode-libs quota-nls perl-podlators pigz perl-WWW-RobotRules perl-Encode perl-IO-stringy pciutils-libs perl-threads perl-XML-Twig perl-Exporter filesystem perl-Class-ISA perl-threads-shared glibc xinetd perl-Module-Pluggable perl-Scalar-List-Utils libstdc++ hostname perl-macros libdaemon libdb cracklib-dicts libuuid audit-libs libpwquality elfutils-libelf shadow-utils libquadmath libxml2 libidn perl-FCGI dracut libSM perl-Compress-Raw-Bzip2 elfutils-libs perl-TimeDate libffi perl-HTML-Parser libxml2-python libref_array rpcbind mesa-libglapi harfbuzz perl-libwww-perl java-1.7.0-openjdk-headless libgfortran libibcm libdb-devel lxc3-client-rdma openssh-server libstdc++-devel perl-Sys-Syslog kernel grep perl-Locale-Maketext mpfr boost-chrono ca-certificates boost-filesystem cups-libs libnes libusbx boost-locale util-linux boost-atomic device-mapper redhat-lsb-submod-security boost-iostreams kmod boost libibverbs foomatic-filters libxslt libgnome-keyring device-mapper-event-libs libss libvorbis SMutil kernel-tools-libs cronie-anacron kernel-devel device-mapper-event lua libcxgb3 mesa-dri-drivers mesa-libgbm gsm texlive-kpathsea javapackages-tools libselinux-utils automake python-backports-ssl_match_hostname cups-client p11-kit-trust texlive-dvipng-bin dejavu-fonts-common libcurl SDL openldap zip atlas libnfsidmap compat-libgfortran-41 yum redhat-lsb-core compat-gcc-44 lksctp-tools redhat-lsb-printing libXScrnSaver initscripts man-db libpath_utils perl-Proc-PID-File libXt liberation-fonts-common glibc-headers gcc-c++ libgnat-devel libX11 libXmu libXpm cups-filesystem pango cups environment-modules gcc-objc++ desktop-file-utils device-mapper-multipath libibverbs-utils librdmacm-utils srptools at python-devel xfsprogs mariadb-libs gsettings-desktop-schemas perl-Pod-Escapes ttmkfdir spax glibc libgfortran pcsc-lite-libs pyparsing emacs-filesystem fontconfig basesystem gpm-libs gcc-objc vim-enhanced redhat-lsb perl-devel lsof libX11-common sed libXrandr perl-Data-Dumper libassuan libattr libgcc libXcursor libestr popt poppler-utils libXft libmng poppler-data lockdev xorg-x11-xauth libipathverbs gcc-gfortran libunistring mgetty gettext groff-base perl-JSON perl-Digest-MD5 postfix pkgconfig perl-Pod-Plainer pyliblzma libnetfilter_conntrack crontabs python-kitchen tcp_wrappers-libs perl-Net-LibIDN quota perl-HTTP-Tiny perl-Business-ISBN-Data rootfiles libuser perl-Font-AFM pciutils libgcc perl-Filter perl-Socket perl-IO-HTML words bash perl-PathTools perl-B-Lint freetype perl-libs nss-util cracklib libcom_err dbus-libs mesa-libGLU libxcb mailcap sqlite lcms2 nss perl-CGI poppler grub2-tools perl-IO-Compress xz perl-HTTP-Date procps-ng glib2 openssl perl-HTTP-Negotiate libcollection perl-Text-Unidecode libnl3 perl-IO-Socket-IP avahi-glib bind-libs perl-XML-SAX libsemanage ntp perl-ExtUtils-MakeMaker cyrus-sasl-lib bind-libs-lite flac-libs libXcomposite krb5-libs boost-system alsa-lib pam boost-regex libverto-tevent python-libs boost-graph gzip boost-serialization device-mapper-libs boost-program-options systemd boost-math libibumad perl-Error python-lxml e2fsprogs-libs polkit SMruntime perl-Git compat-glibc cronie kernel-headers perl-local-lib lvm2-libs shifter-runtime hwdata libdrm texlive-kpathsea-bin systemtap-sdt-devel python-backports giflib libtasn1 grubby t1lib pygtk2 libtool curl python-dateutil dhcp-libs lapack flex policycoreutils singularity mailx lxfs-client compat-gcc-44-c++ redhat-lsb-cxx libgomp libXdmcp libobjc libini_config libxshmfence libtevent openjpeg-libs cronie-noanacron ipmitool mcelog parted gdb tcsh numactl bzip2 glibc-utils less dmidecode libquadmath libstdc++ libgnat which gcc pax libreport-filesystem info wget libXfixes gdk-pixbuf2 libestr sysstat pulseaudio-libs bc qt-x11 libnfnetlink numad perl-Encode-Locale glibc-static OpenIPMI-modalias acl infinipath-psm avahi perl-Digest-SHA1 ustr qt3 rsyslog pygpgme libmnl dapl pyxattr perl-parent perl-Business-ISBN rsh-server perl-HTML-Tree perl-Time-Local tzdata graphite2 yum-metadata-parser perl-Getopt-Long xz-libs hicolor-icon-theme strace gmp glibc-devel cpio perl-LWP-MediaTypes libICE qpdf-libs libfontenc perl-HTTP-Message nss-tools libbasicobjects perl-Text-Soundex libpng dbus-glib perl-XML-LibXML ntpdate mozjs17 patch kernel-devel libicu python boost-python libedit cryptsetup-libs boost-test systemd-sysv git lm_sensors-libs libtirpc munge-libs libpciaccess texlive-kpathsea-lib python-urlgrabber libasyncns python-nose texinfo stix-fonts python-matplotlib lxc3-timeout libpipeline jasper-libs nano psmisc liberation-mono-fonts libquadmath-devel hdparm gd libXext libjpeg-turbo keyutils mesa-libEGL libevent gtk2 mdadm ethtool yum-utils urw-fonts perl-XML-Parser infiniband-diags libXtst python-dmidecode libmlx4 rdate perl-Pod-Perldoc libcgroup-tools perl-ExtUtils-Manifest perl-Storable setup xorg-x11-font-utils time tcp_wrappers perl-File-Temp zlib perl-CPAN libtiff gnupg2 keyutils-libs nspr pth libgomp file-libs openssl-libs perl-HTML-Tagset fipscheck-lib nss-softokn perl-Time-HiRes atk logrotate perl-File-Listing libnl device-mapper-persistent-data openssh perl-Net-HTTP libdb-utils java-1.7.0-openjdk perl-ExtUtils-ParseXS pcre lustre-client-modules perl-Locale-Codes p11-kit libmpc libblkid boost-date-time kpartx boost-context rdma unzip autoconf iputils kernel-tools json-c libibmad mesa-filesystem python-javapackages texlive-base perl-Thread-Queue texlive-dvipng ghostscript rpm agg rpm-python redhat-lsb-desktop iproute smartmontools pixman 

    yum clean all
    mv /usr/bin/ssh /usr/bin/ssh_orig
    IMPORTDIR=$(mktemp -d)
    cd $IMPORTDIR
    git clone https://github.com/c1t4r/Plurality.git -b master
    cd Plurality/rootfs
    git checkout-index -a -f --prefix=$IMPORTDIR/
    find $IMPORTDIR/rootfs -type d -execdir rm -f {}/.gitignore \;
    rm -f /.singularity.d/actions/* 
    rsync --ignore-existing -rahlvp $IMPORTDIR/rootfs/ /
    cd /
    chmod -R a+rwx /opt/bwhpc/common /custom/*
    rm -rf $IMPORTDIR
```

## Collection

 - Name: [c1t4r/CiTAR-Containers](https://github.com/c1t4r/CiTAR-Containers)
 - License: None

