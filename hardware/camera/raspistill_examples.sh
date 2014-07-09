# A very small picture - with 5 second preview:
# raspistill -o junk.jpg -w 100 -h 100

# Slightly larger pic, with 10 second preview
# raspistill -o junk.jpg -w 700 -h 700 -t 10000

# And flip horizontally:
# raspistill -o junk.jpg -w 700 -h 700 -t 10000 -hf

# And flip vertically:
# raspistill -o junk.jpg -w 700 -h 700 -t 10000 -vf

# Useful if the camera is upside down
# raspistill -o junk.jpg -w 700 -h 700 -t 30000  -rot 180
