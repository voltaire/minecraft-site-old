var images = [
    "http://mc.voltaire.sh/i/bg1.png",
    "http://mc.voltaire.sh/i/nightmountain.png",
    "http://mc.voltaire.sh/i/nokbarmountain.png",
    "http://mc.voltaire.sh/i/hillsstorage.png",
    "http://mc.voltaire.sh/i/nightcheney.png",
    "http://mc.voltaire.sh/i/nokbarmountain2.png",
    "http://mc.voltaire.sh/i/thunderbase.png"
];
        
$(images).each(function(){
    $('<img/>')[0].src = this; 
});
        
var index = 0;
        
$.backstretch(images[index], {speed: 500});
        
setInterval(function() {
    index = (index >= images.length - 1) ? 0 : index + 1;
    $.backstretch(images[index]);
}, 5000);
