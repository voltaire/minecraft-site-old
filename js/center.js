$('.centerMe').css({
    position:'absolute',
    left: ($(window).width() - $('.centerMe').outerWidth())/2,
    top: ($(window).height() - $('.centerMe').outerHeight())/2
});

$(window).resize(function(){

        $('.centerMe').css({
                position:'absolute',
                left: ($(window).width() - $('.centerMe').outerWidth())/2,
                top: ($(window).height() - $('.centerMe').outerHeight())/2
        });

});

$(window).resize();
