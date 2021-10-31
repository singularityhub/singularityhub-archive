---
id: 13057
name: "funnell/schnapps_singularity"
branch: "master"
tag: "latest"
commit: "cb178f256c478d61cd6c6951f6a4a3e453b9438f"
version: "18c81d799c47a3465f0aec697aa6eb65"
build_date: "2020-07-17T21:23:38.448Z"
size_mb: 1334.0
size: 502280223
sif: "https://datasets.datalad.org/shub/funnell/schnapps_singularity/latest/2020-07-17-cb178f25-18c81d79/18c81d799c47a3465f0aec697aa6eb65.sif"
url: https://datasets.datalad.org/shub/funnell/schnapps_singularity/latest/2020-07-17-cb178f25-18c81d79/
recipe: https://datasets.datalad.org/shub/funnell/schnapps_singularity/latest/2020-07-17-cb178f25-18c81d79/Singularity
collection: funnell/schnapps_singularity
---

# funnell/schnapps_singularity:latest

```bash
$ singularity pull shub://funnell/schnapps_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: archlinux

%runscript
    echo "Schnapps"

%post
    echo "Schnapps"

    # set time zone
    ln -s /usr/share/zoneinfo/UTC /etc/localtime

    # set locale
    echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
    locale-gen
    echo 'LANG=en_US.UTF-8' > /etc/locale.conf

    # set the package mirror server
    echo 'Server = https://mirrors.kernel.org/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist
    # add fail-over servers
    echo 'Server = https://archlinux.honkgong.info/$repo/os/$arch' >> /etc/pacman.d/mirrorlist

    # install base software
    pacman -Syu --noconfirm git
    pacman -Syu --noconfirm --needed base-devel

    # install R
    pacman -Syu --noconfirm openblas
    pacman -Syu --noconfirm lapack
    pacman -Syu --noconfirm gcc-fortran
    pacman -Syu --noconfirm python
    pacman -Syu --noconfirm r

    # function to join array elements by separator
    function join_by {
        local d=$1
        shift
        echo -n "$1"
        shift
        printf "%s" "${@/#/$d}"
    }

    # install CRAN packages
    cran_packages=( \
        argparse \
        BiocManager \
        devtools \
        dplyr \
        readr \
        tidyr
    )
    cran_package_list=$( join_by "', '" ${cran_packages[@]} )
    R -e "install.packages(c('$cran_package_list'), repos = 'http://cran.us.r-project.org')"

    # install Bioconductor packages
    bioc_packages=( \
        ComplexHeatmap \
        GenomicRanges \
    )
    bioc_package_list=$( join_by "', '" ${bioc_packages[@]} )
    R -e "BiocManager::install(c('$bioc_package_list'))"

    # install devtools installable packages
    # this prevents an error when installing a dependency of schnapps
    Rscript -e 'x <- file.path(R.home("doc"), "html"); if (!file.exists(x)) {dir.create(x, recursive=TRUE); file.copy(system.file("html/R.css", package="stats"), x)}'
    github_auth_token="c61212ed2c2d88ee6e1c68a4739ba2c1dfca4f66"
    R -e "devtools::install_github('shahcompbio/schnapps', auth_token='$github_auth_token')"

    # Remove the packages downloaded to Pacman cache dir.
    pacman -Syu --noconfirm pacman-contrib
    paccache -r -k0
```

## Collection

 - Name: [funnell/schnapps_singularity](https://github.com/funnell/schnapps_singularity)
 - License: None

