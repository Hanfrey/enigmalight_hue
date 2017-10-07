# Philips Hue Ambilight Clone with Enigmalight and this script.


Many thanks to [Krannich Hausautomation](http://blog.krannich.de/2015/12/ambilight-mit-enigmalight-und-philips-hue-bridge/) for his tutorial and basis of this script.
If you are new to this, follow his tutorial to get the key from your bridge and install the enigmalight. I had some problems with his script (no blue, big delay), so I rewrote most of his script.

Thanks to  [benknight](https://github.com/benknight/hue-python-rgb-converter) for his lib to transform the rgb to xy values.

The Idea is pretty simple, instead of sending the extracted color from the enigmalight to the LEDs connected it sends them to this script which then makes a rest call to your hue bridge.
It only makes 1 rest call per second because the hue bridge is pretty slow, and saving the rest calls you will not get the right color to the tv picture.


### SEE IT IN ACTION

[![Enigmalight](https://img.youtube.com/vi/52k0y1JipzE/0.jpg)](https://www.youtube.com/watch?v=52k0y1JipzE)


### Usage

1. Install enigmalight 
2. Make your enigmalight.cfg
3. Copy the engimalight_hue.py in the folder you specified in the enigmalight.cfg
4. Get an Key from your Hue Bridge
5. Insert the Key and IP in the Script, import the right Gamut for your Hue.
6. Start enigmalight


The script is prepared to use 3 Lamps.  This are the 3 Lamps URLs. If you want a 4th you need to do some copy paste driven development . The Number you get from your bridge.

	
    	lurl = url + '2/state'
    	rurl = url + '1/state'
    	burl = url + '4/state'


### Known issues:

Sometimes the color is not what i've excepted.
Too much hard coded stuff.
 

 ### CONTRIBUTE

 This is more or less a proof of concept. Feel free to contribute.


 