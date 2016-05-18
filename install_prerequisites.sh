sudo apt-get install fluidsynth
sudo apt-get install cython
sudo apt-get install libasound2-dev libjack-dev
# Optional
sudo apt-get install libportmidi-dev
sudo pip install mido
mkdir lib
cd lib
git clone https://github.com/khamaileon/python-rtmidi
cd python-rtmidi
sudo pip install .
cd ..
cd ..

