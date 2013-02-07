$(document).ready(function() {
    $('.qwebirc').load('http://mc.voltaire.sh:3989');
    var refreshId = setInterval(function() {
        $('.qwebirc').load('http://mc.voltaire.sh:3989');
    }, 15000);
    $.ajaxSetup({ cache: false });
});
