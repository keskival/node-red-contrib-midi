#!/bin/bash
sudo killall fluidsynth
sleep 1
sudo fluidsynth -si -a pulseaudio -m alsa_seq /usr/share/sounds/sf2/FluidR3_GM.sf2 &
sleep 1
aconnect -o

