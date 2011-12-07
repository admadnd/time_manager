$(document).ready(function() {

    // For debugging
    $.ajaxSetup({"error":function(XMLHttpRequest,textStatus, errorThrown) {
	alert(textStatus);
	alert(errorThrown);
	alert(XMLHttpRequest.responseText);
    }});

        $('#pie a').click(function() {
 
	    $.getJSON("/pie/", function(data) {
	        console.log(data);

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


	        $.plot($("#weekpiechart"),data,options);
	    })

        return false;
    });

    $('#weeklyline a').click(function() {
        
        $.getJSON("/weeklyline/", function(data) {

            $.plot($("#weeklylinegraph"),data,[]);
        });

        return false;

    });    

    $('#timeline a').click(function() {
        
        $.getJSON("/timeline/", function(data) {

            var options = {
                series:{
                    lines:{
                        show: true,   
                        fill: true
                    }
                },
                xaxis:{
                    show:true,
                    mode:"time",
                    timeformat:"%y/%m/%d %h:%S%P"
                },
                yaxis:{
                    show:false
                }
            };

            $.plot($("#timelinegraph"),data,options);
        });

        return false;

    });    


        
});
