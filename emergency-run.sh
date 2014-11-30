#!/bin/bash
my_dir=`dirname $0`
source $my_dir/config
$my_dir/set-wallpaper.sh $default_image
$my_dir/run.py
