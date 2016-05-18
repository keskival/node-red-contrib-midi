#!/usr/bin/python

import logging
import sys
import time

import rtmidi
from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *

# This is an example for playing dynamic MIDI
# using the python-rtmidi from: https://github.com/khamaileon/python-rtmidi

# You also need aMIDI synthesizer, for example Fluidsynth daemon, which does this in software
# utilizing lots of CPU, or a sound card with MIDI support.

try:
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()

    # Use aconnect -o to show the ports. This is the index of the port to use.
    midiout.open_port(1)
    # Using the following shows you the interactive list of valid output ports.
    # midiout, port_name = open_midiport(port, "output")
except (EOFError, KeyboardInterrupt):
    sys.exit()

def play(note, instrument = 0, bank = 0):
  channel = 0
  bank_change = [BANK_SELECT, bank]
  program_change = [PROGRAM_CHANGE, instrument]
  note_on = [NOTE_ON, note, 112] # channel 1, middle C, velocity 112
  note_off = [NOTE_OFF, note, 0]
  midiout.send_message(bank_change)
  midiout.send_message(program_change)
  midiout.send_message(note_on)
  time.sleep(1)
  midiout.send_message(note_off)

print "grand piano sample, three notes"
play(60, 0)
play(62, 0)
play(63, 0)

midiout.close_port()
