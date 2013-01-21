$('.hero-unit').css({
    position:'absolute',
    left: ($(window).width() - $('.hero-unit').outerWidth())/2,
    top: ($(window).height() - $('.hero-unit').outerHeight())/2
});

$(window).resize(function(){

        $('.hero-unit').css({
                position:'absolute',
                left: ($(window).width() - $('.hero-unit').outerWidth())/2,
                top: ($(window).height() - $('.hero-unit').outerHeight())/2
        });

});

$(window).resize();
