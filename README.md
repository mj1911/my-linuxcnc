NOTE this is the ~/linuxcnc folder on a Raspberry Pi 4B + Mesa 7C80 + Flex GUI + Waveshare 22930 touchscreen + VistaCNC P2S pendant:
* https://store.mesanet.com/index.php?route=product/product&product_id=345
* https://www.gnipsel.com/linuxcnc/flexgui/index.html
* https://www.waveshare.com/product/raspberry-pi/displays/lcd-oled/15.6hp-capqled.htm?___SID=U
* https://vistacnc.com/b08_pendant_P2/pendant_p2-S.htm

These files are changing often and are likely borked as my machine is *still* being built.  You may look, but definitely do not blindly copy to your machine as it certainly will fail!  Each LinuxCNC install is fairly unique; this one possibly moreso than others.

This config is based off of a HostMot2 example here: https://github.com/LinuxCNC/linuxcnc/tree/master/configs/by_interface/mesa/hm2-stepper

NOTE that this config does NOT use P.I.D. loops at all, which makes it nice and snappy on an Rpi4B, but it has not been tested in production and may be found to be totally unsuitable.

### Possibly outdated example of the GUI:
![Using FlexGUI 1.0.2, November 2024](Screenshot_2024-11-10_08-13-18.png)
