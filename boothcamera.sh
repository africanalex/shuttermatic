#!/bin/bash

DATE=$(date +"%Y-%m%d_%H%M%S")
raspistill -o /home/pi/photobooth_images/$DATE.jpg -q 100
