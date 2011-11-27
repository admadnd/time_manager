$(document).ready(function() {

    var data = [];
    $('#weekpiedat ul li > ul').each(function() {
	var category = $(this).children().filter(':first-child').text();
	var time = parseFloat($(this).children().filter(':last-child').text());
	/* flot cannot handle the time in seconds. Numbers too large. */
	time = time / 3600;

	elem = { label: category, data: time};
	data.push(elem);
    });
        
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

    $('#weekpiedat').hide();
    $.plot($("#weekpiechart"),data,options);
});