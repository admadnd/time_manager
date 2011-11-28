
$(document).ready(function() {
    //assign click event handler to an html element
    $('#task_name a').click(function() {
      
        //grab HTML snippit from server - handler functionality  
        $('#sorted').load("/sorted/");  
        
        //so that the click event will do the above actions only 
        return false;    
    });

});
