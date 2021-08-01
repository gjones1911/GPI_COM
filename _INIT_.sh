#!/usr/bin/env sh

# Author: Gerald Jones
# Purpose: Initialize a new raspberry pi for general operation
#
echo "what is my pi name that will be used for message and communication?"
read PI_Name
echo "PI: $PI_Name will begin initial set up"
echo "Hang tight, I may need your input....."

# install git checkout -b branch_name
sudo apt update
sudo apt install git

#
echo "we have installed git:" git --version

# upgrade pip and set up tools
python3 -m pip --upgrade pip
sudo pip3 install --upgrade setuptools


# install virtual environment tools
python3 -m install --user virtualenv

# create generic starter environments
python3 -m venv matplot_lib_env
python3 -m venv tensorflow_env
python3 -m venv slack_env
python3 -m venv sadie_env
python3 -m venv learning_machines_env


# set some more general stuff for tensorflow but for


# switch to tensor flow environment and set up tensorflow
source /tensorflow_env/bin/activate
sudo pip3 install numpy==1.19.0
sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran python-dev libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev liblapack-dev cython libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev
sudo pip3 install keras_applications==1.0.8 --no-deps
sudo pip3 install keras_preprocessing==1.1.0 --no-deps
sudo pip3 install h5py==2.9.0
sudo pip3 install pybind11
pip3 install -U --user six wheel mock

wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.3.0-cp37-none-linux_armv7l_download.sh"
sudo chmod +x tensorflow-2.3.0-cp37-none-linux_armv7l_download.sh
/tensorflow-2.5.0-cp37-none-linux_armv7l_download.sh
sudo pip3 uninstall tensorflow
sudo -H pip3 install tensorflow-2.3.0-cp37-none-linux_armv7l.whl

# leave the tensor flow environment
deactivate


# get the matplot lib envi up
source matplot_lib_env/bin/activate
python3 -m pip install matplotlib
deactivate

# get the memory stuff

python3 -m pip install psutil
python3 -m pip install slack_sdk

