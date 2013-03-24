$(document).ready(loadstreams);

function loadstreams() {
    $.getJSON('/streams', function(data) {
	$.each(data, function(devid, url) {
	    var newdiv = $(document.createElement('div'));
	    var newimg = $(document.createElement('img'));
	    newimg.attr('src', url);
	    $(newdiv).addClass('stream');	    
	    newdiv.appendTo($('#streams'));
	    newimg.appendTo(newdiv);
	}
    )}
)}
