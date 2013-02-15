$(document).ready(function() {
    $('.mcstatus').load('http://mc.voltaire.sh/mcstatus');
    var refreshId = setInterval(function() {
        $('.mcstatus').load('http://mc.voltaire.sh/mcstatus');
    }, 300000);
    $.ajaxSetup({ cache: false });
});
