# High Res
<p style="display: flex; justify-content: center">
    <img src="high-res.png" style="">
</p>

## Summary
This patch changes the game's resolution to 1920x1080 pixels (Full HD).

## Details
Hooks are deployed to the following locations:
- The options screen's exit function (to set the resolution)
- The function that sets the resolution before the scene loads (to set the the resolution)
- The function that sets the resolution after the scene has already loaded (to set the the resolution)
- The function that sets the position of the UI elements on the right (to set them according to the resolution)
- The function that sets the position of the UI elements at the top (to set them according to the resolution)
- The function that renders all objects (to make the rectangle in the bottm right corner black)
- The function in `aim.dll` that decodes image files (to replace the acceleration map with the upscaled variant)
- The function that loads screen settings from accelMap.ini (to set the dimension of the acceleration map)

## Patch
The source code for this patch can be found [here](https://github.com/P3Modding/p3-lib/tree/master/mod-high-res).
