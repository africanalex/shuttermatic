#!/bin/bash
value=$(<settings/camera.txt)
DATE=$(date +"%Y-%m%d_%H%M%S")
echo "selected camera is $value"
if [ "$value" == "1" ]; then
echo "Using picam"
raspistill -o /home/booth/photobooth_images/$DATE.jpg -q 100
else
echo "using dslr"
gphoto2 --capture-image-and-download --filename /home/booth/photobooth_images/$DATE.jpg
fi
