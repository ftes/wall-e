#!/bin/bash
file="$(mktemp)"
wget -q $1 -O $file
DISPLAY=:0.0 feh --bg-fill $file
