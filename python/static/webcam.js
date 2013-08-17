function pan(devid, dir){
    $.post("/pan", {'devid':devid, 'dir':dir});
}
function tilt(devid, dir){
    $.post("/tilt", {'devid':devid, 'dir':dir});
}

currentlyshown = "none";

function howitworks() {
    if (currentlyshown == "howitworks"){
	$('#infobox')[0].innerHTML="";
	currentlyshown = "none";
    }
    else {
	$('#infobox')[0].innerHTML=howitworks_text;
	currentlyshown = "howitworks";
    }
}

function press() {
    if (currentlyshown == "press"){
	$('#infobox')[0].innerHTML="";
	currentlyshown = "none";
    }
    else {
	$('#infobox')[0].innerHTML=press_text;
	currentlyshown = "press";
    }
}