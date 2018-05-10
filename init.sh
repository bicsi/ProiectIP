#!/bin/bash

function init_submodules() {
    git submodule update --init --recursive
}

function init_colorization() {
    pushd extern/colorization
    bash ./models/fetch_release_models.sh
    popd

    pushd extern
    patch -p1 < caffe_use_cpu.patch
    popd
}

function init_python_requirements() {
    sudo apt install python3-pip python-pip
    sudo pip3 install -r requirements.txt

    # Debian only, for now.
    ./install_caffe.sh
}

function init_avatars_population() {
    pushd extern/avatars
    python3 download_avatars_kaggle_dataset.py
    popd
}


init_submodules
init_python_requirements
init_colorization
init_avatars_population
