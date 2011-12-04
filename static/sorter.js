
$(document).ready(function() {
    //assign click event handler to an html element
    //sort by name ascending - click event
    $('#task_name a').click(function() {
      
        //grab HTML snippit from server - handler functionality  
        $('#sorted').load("/sorted/");  
        
        //so that the click event will do the above actions only 
        return false;    
    });
    //sort by start time ascending - click event
    $('#task_start_time a').click(function() {
          
            //grab HTML snippit from server - handler functionality  
            $('#sorted2').load("/sorted2/");  
            
            //so that the click event will do the above actions only 
            return false;    
        });
    //sort by name descending - click event
    $('#task_name2 a').click(function() {
      
        //grab HTML snippit from server - handler functionality  
        $('#sorted3').load("/sorted3/");  
        
        //so that the click event will do the above actions only 
        return false;    
    });
    //sort by start time descending- click event
    $('#task_start_time2 a').click(function() {
          
            //grab HTML snippit from server - handler functionality  
            $('#sorted4').load("/sorted4/");  
            
            //so that the click event will do the above actions only 
            return false;    
        });
});
