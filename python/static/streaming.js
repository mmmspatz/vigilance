$(document).ready(loadstreams);

function imclick(url){
    window.location=url;
}

function loadstreams() {
    $.getJSON('/streams', function(data) {
	$.each(data, function(devid, url) {
	    var newdiv = $(document.createElement('div'));
	    var newimg = $(document.createElement('img'));
	    newimg.attr('src', url);
	    newimg.attr('onclick', 'imclick(\'/single/'+ devid +'\')');
	    newimg.attr('style', 'cursor:pointer');
	    $(newdiv).addClass('stream');	    
	    newdiv.appendTo($('#streams'));
	    newimg.appendTo(newdiv);
	}
    )}
)}
