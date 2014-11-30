#!/bin/bash
file=$1

if ps -e | grep -q "i3"; then
        # using feh (e.g. for i3-wm)
        DISPLAY=:0.0 feh --bg-fill $file
else
	# using gnome
	gsettings set org.gnome.desktop.background picture-uri file://$file
fi
