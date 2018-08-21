#!/bin/bash
value=$(<settings/colour.txt)
DATE=$(date +"%Y-%m%d_%H%M%S")
echo "selected camera is $value"
if [ "$value" == "1" ]; then
echo "Using colour"
raspistill -vf -o /home/booth/photobooth_images/$DATE.jpg -q 100
else
echo "using bw"
raspistill -vf --colfx 128:128 -o /home/booth/photobooth_images/$DATE.jpg -q 100
fi
