---
id: 6123
name: "jose-d/container-recipes"
branch: "master"
tag: "latest"
commit: "ab65ecc87ab5fad63952cabb78bb622325215316"
version: "4d91cc1ed0bdc52abcb2579930132c08"
build_date: "2019-01-04T21:39:45.010Z"
size_mb: 3311
size: 1882890271
sif: "https://datasets.datalad.org/shub/jose-d/container-recipes/latest/2019-01-04-ab65ecc8-4d91cc1e/4d91cc1ed0bdc52abcb2579930132c08.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jose-d/container-recipes/latest/2019-01-04-ab65ecc8-4d91cc1e/
recipe: https://datasets.datalad.org/shub/jose-d/container-recipes/latest/2019-01-04-ab65ecc8-4d91cc1e/Singularity
collection: jose-d/container-recipes
---

# jose-d/container-recipes:latest

```bash
$ singularity pull shub://jose-d/container-recipes:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:stretch

%labels

AUTHOR jose@FZU


%post

export DEBIAN_FRONTEND=noninteractive

# update, just for case
apt-get update && apt-get -y upgrade

# some goodies
apt-get install -y vim wget

# deps of cadabra
apt-get install -y python3 libpython3.5 libboost-date-time1.62.0 adwaita-icon-theme at-spi2-core blt cpp cpp-6 dbus dconf-gsettings-backend dconf-service dvipng fontconfig fontconfig-config fonts-cabin fonts-comfortaa fonts-croscore fonts-crosextra-caladea fonts-crosextra-carlito fonts-dejavu-core fonts-dejavu-extra fonts-droid-fallback fonts-ebgaramond fonts-ebgaramond-extra fonts-font-awesome fonts-freefont-otf fonts-freefont-ttf fonts-gfs-artemisia fonts-gfs-complutum fonts-gfs-didot fonts-gfs-neohellenic fonts-gfs-olga fonts-gfs-solomos fonts-junicode fonts-lato fonts-linuxlibertine fonts-lmodern fonts-lobster fonts-lobstertwo fonts-lyx fonts-noto-hinted fonts-noto-mono fonts-oflb-asana-math fonts-roboto-hinted fonts-sil-gentium fonts-sil-gentium-basic fonts-sil-gentiumplus fonts-sil-gentiumplus-compact fonts-stix fonts-texgyre ghostscript glib-networking glib-networking-common glib-networking-services gsettings-desktop-schemas gsfonts gtk-update-icon-cache hicolor-icon-theme ipython isympy isympy-common javascript-common krb5-locales libapparmor1 libasound2 libasound2-data libatk-bridge2.0-0 libatk1.0-0 libatk1.0-data libatkmm-1.6-1v5 libatspi2.0-0 libauthen-sasl-perl libavahi-client3 libavahi-common-data libavahi-common3 libblas-common libblas3 libboost-filesystem1.62.0 libboost-program-options1.62.0 libboost-regex1.62.0 libboost-system1.62.0 libbsd0 libcairo-gobject2 libcairo2 libcairomm-1.0-1v5 libcolord2 libcroco3 libcups2 libcupsfilters1 libcupsimage2 libdatrie1 libdbus-1-3 libdconf1 libdrm-amdgpu1 libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libdrm2 libedit2 libegl1-mesa libencode-locale-perl libepoxy0 libfile-basedir-perl libfile-desktopentry-perl libfile-homedir-perl libfile-listing-perl libfile-mimeinfo-perl libfile-which-perl libfont-afm-perl libfontconfig1 libfontenc1 libfreetype6 libgail-common libgail18 libgbm1 libgd3 libgdbm3 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-common libgfortran3 libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libglib2.0-0 libglib2.0-data libglibmm-2.4-1v5 libglu1-mesa libgmpxx4ldbl libgpm2 libgraphite2-3 libgs9 libgs9-common libgssapi-krb5-2 libgtk-3-0 libgtk-3-bin libgtk-3-common libgtk2.0-0 libgtk2.0-bin libgtk2.0-common libgtkmm-3.0-1v5 libharfbuzz-icu0 libharfbuzz0b libhtml-form-perl libhtml-format-perl libhtml-parser-perl libhtml-tagset-perl libhtml-tree-perl libhttp-cookies-perl libhttp-daemon-perl libhttp-date-perl libhttp-message-perl libhttp-negotiate-perl libice6 libicu57 libijs-0.35 libio-html-perl libio-socket-ssl-perl libipc-system-simple-perl libisl15 libjbig0 libjbig2dec0 libjpeg62-turbo libjs-jquery libjs-jquery-ui libjson-glib-1.0-0 libjson-glib-1.0-common libk5crypto3 libkeyutils1 libkpathsea6 libkrb5-3 libkrb5support0 liblapack3 liblcms2-2 libldap-2.4-2 libldap-common libllvm3.9 liblwp-mediatypes-perl liblwp-protocol-https-perl libmailtools-perl libmpc3 libmpfr4 libncurses5 libnet-dbus-perl libnet-http-perl libnet-smtp-ssl-perl libnet-ssleay-perl libnspr4 libnss3 libopenjp2-7 libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 libpangomm-1.4-1v5 libpaper-utils libpaper1 libpciaccess0 libpcrecpp0v5 libperl5.24 libpixman-1-0 libpng16-16 libpoppler64 libpotrace0 libproxy1v5 libptexenc1 libpython-stdlib libpython2.7-minimal libpython2.7-stdlib libquadmath0 librest-0.7-0 librsvg2-2 librsvg2-common libruby2.3 libsasl2-2 libsasl2-modules libsasl2-modules-db libsensors4 libsigc++-2.0-0v5 libsm6 libsoup-gnome2.4-1 libsoup2.4-1 libssl1.0.2 libsynctex1 libtcl8.6 libtexlua52 libtexluajit2 libtext-iconv-perl libthai-data libthai0 libtie-ixhash-perl libtiff5 libtimedate-perl libtk8.6 libtxc-dxtn-s2tc liburi-perl libutempter0 libwayland-client0 libwayland-cursor0 libwayland-egl1-mesa libwayland-server0 libwebp6 libwebpdemux2 libwebpmux2 libwww-perl libwww-robotrules-perl libx11-6 libx11-data libx11-protocol-perl libx11-xcb1 libxau6 libxaw7 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-render0 libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxdmcp6 libxext6 libxfixes3 libxft2 libxi6 libxinerama1 libxkbcommon0 libxml-parser-perl libxml-twig-perl libxml-xpathengine-perl libxml2 libxmu6 libxmuu1 libxpm4 libxrandr2 libxrender1 libxshmfence1 libxss1 libxt6 libxtst6 libxv1 libxxf86dga1 libxxf86vm1 libyaml-0-2 libyaml-tiny-perl libzzip-0-13 lmodern netbase perl perl-modules-5.24 perl-openssl-defaults poppler-data preview-latex-style prosper ps2eps python python-backports-shutil-get-terminal-size python-chardet python-decorator python-enum34 python-gmpy python-imaging python-ipython python-ipython-genutils python-matplotlib-data python-minimal python-mpmath python-numpy python-pathlib2 python-pexpect python-pickleshare python-pil python-pkg-resources python-prompt-toolkit python-ptyprocess python-pyglet python-pygments python-simplegeneric python-six python-sympy python-sympy-doc python-traitlets python-wcwidth python2.7 python2.7-minimal python3-cycler python3-dateutil python3-matplotlib python3-mpmath python3-numpy python3-pil python3-pyparsing python3-six python3-tk python3-tz rake rename ruby ruby-did-you-mean ruby-minitest ruby-net-telnet ruby-power-assert ruby-test-unit ruby2.3 rubygems-integration sgml-base shared-mime-info t1utils tcl tcl8.6 tex-common tex-gyre texlive texlive-base texlive-binaries texlive-extra-utils texlive-font-utils texlive-fonts-extra texlive-fonts-extra-doc texlive-fonts-recommended texlive-fonts-recommended-doc texlive-generic-extra texlive-generic-recommended texlive-latex-base texlive-latex-base-doc texlive-latex-extra texlive-latex-extra-doc texlive-latex-recommended texlive-latex-recommended-doc texlive-pictures texlive-pictures-doc texlive-pstricks texlive-pstricks-doc tipa tk tk8.6 tk8.6-blt2.5 ttf-adf-accanthis ttf-adf-gillius ttf-adf-universalis ttf-bitstream-vera ucf unzip uuid-runtime x11-common x11-utils x11-xserver-utils xbitmaps xdg-user-dirs xdg-utils xkb-data xml-core xterm zip

# cadabra2:
cd /tmp/ && wget https://cadabra.science/packages/debian9/cadabra2-2.1.9-stretch.deb -P /tmp && dpkg -i /tmp/cadabra2-2.1.9-stretch.deb

%environment

    export PROMPT_COMMAND=true
    export XDG_RUNTIME_DIR=/dev/shm/${USER}/sdg_runtime_dir

%runscript
    cadabra2-gtk
```

## Collection

 - Name: [jose-d/container-recipes](https://github.com/jose-d/container-recipes)
 - License: None

