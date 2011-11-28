$(document).ready(function() {

    // For debugging
    $.ajaxSetup({"error":function(XMLHttpRequest,textStatus, errorThrown) {
	alert(textStatus);
	alert(errorThrown);
	alert(XMLHttpRequest.responseText);
    }});

    var options = {
	series:{
	    pie:{
		show: true
	    }
	},
	legend:{
	    show: false
	}
    };

    $('#pie a').click(function() {
 
	$.getJSON("/pie/", function(data) {
	    console.log(data);
	    //PLOT.setData(data);
	    //PLOT.setData(test);
	    //PLOT.draw();
	    $.plot($("#weekpiechart"),data,options);
	});

	return false;
    });
    
    
});