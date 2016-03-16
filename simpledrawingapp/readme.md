log of versions...  
1. ver11192015.html - this is a more improved version than the one outside this folder.  
<br>
2. ver112115.html - this is a canvas with 'onion-skin' functionality. hopefully on the way to something more useful for an aspiring animator like me! however, this version is still buggy because canvas0 (the initial canvas) seems to be active when it shouldn't be (i.e. if you go up a page and then go back to 0, it suddenly becomes permenently active).  
<br>
3. ver112215.html - I binded the spacebar to addLayer() function and utilized Bootstrap better for a uniform layout. I still can't figure out the problem with canvas0 but at least everything else seems to work okay. I think I'll take a break from this for a bit and learn about web scraping, but I hope I come back to this! 
<br>  
4. ver112915.html - added a color picker! well, more like custom color maker. I also learned that I need to be mindful of method names and how there are separate ones for jQuery and regular ECMAScript, i.e. val() and .value.  
<br>
5. ver121015.html - restructured the format so that the canvas is on the left and toolbar on the right. I also implemented a copy function so that whatever is drawn on one canvas can be copied on to the succeeding canvas. useful if you spent a long time  
drawing a background, for example. Getting the canvas to be drawn on properly was difficult after moving the canvas to the left. There was a huge offset initially, in which a pixel drawn was far from where you would click. To remedy this, I set the offset to be based on the container of the canvas (div id='picture') and subtracted a few pixels to the equation. Not perfect, but it produced a more satisfactory product. 
<br>    
6. ver012616.html - made the cloning feature applicable to any canvas, not just the last one as it previously was, by storing all pixel data of each canvas in an object. this may be helpful when manipulating pixels during filter application, for example. I hope to add filter features later. also fixed the buggy initial canvas (canvas0) by moving a couple variables outside the draw() function so that they could be overwritten appropirately. 
<br>    
see the current version here: http://syncopika.tumblr.com/htmldrawapp    
<hr>
***** new updates to this program will be here: https://github.com/syncopika/html_drawing_app *****

ideas:  
1. add undo/redo     
2. add color wheel  
3. more brushes (make a javascript library maybe?) 
4. import background pictures  
5. make gif?? :D  
