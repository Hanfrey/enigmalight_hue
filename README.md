# Philips Hue Ambilight Clone with Enigmalight and this script.


Many thanks to [Krannich Hausautomation](http://blog.krannich.de/2015/12/ambilight-mit-enigmalight-und-philips-hue-bridge/) for his tutorial and basis of this script.
If you are new to this, follow his tutorial to get the key from your bridge and install the enigmalight. I had some problems with his script (no blue, big delay), so I rewrote most of his script.

Thanks to  [benknight](https://github.com/benknight/hue-python-rgb-converter) for his lib to transform the rgb to xy values.


### Usage

1. Install enigmalight
2. Make your enigmalight.cfg
3. Copy the engimalight_hue.py in the folder you specified in the enigmalight.cfg
4. Get an Key from your Hue Bridge
5. Insert the Key and IP in the Script, import the right Gamut for your Hue.
6. Start enigmalight


The script is prepared to use 3 Lamps. 

### Known issues:

Sometimes the color is not what i've excepted.
Too much hard coded stuff.
