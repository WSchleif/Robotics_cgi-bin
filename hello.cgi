#!/bin/bash

#change GPIO18 to PWM for audio
gpio -g mode 18 ALT5

#play sound file
sudo aplay /home/pi/hello_42.wav

#switch GPIO18 back to input
gpio -g mode 18 IN

#change GPIO12 and GPIO13 back to PWM
gpio -g mode 12 PWM
gpio -g mode 13 PWM

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
