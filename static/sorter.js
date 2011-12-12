
$(document).ready(function() {
    // default flags for task_name and task_start_time
    var task_name_ascend = true;
    var task_start_time_ascend = true;

    //sort by task_name click event 
    $('a[name="task_name"]').live('click',function() {
      
        // sort ascending
        if(task_name_ascend == true) {
            //grab HTML snippit from server - handler functionality  
            $('#task-table').load("/sorted/");  
            task_name_ascend = false;
        } 
        // sort descending
        else {
            $('#task-table').load("/sorted3/");  
            task_name_ascend = true;
        }
        //so that the click event will do the above actions only 
        return false;    
    });

    //sort by start time click event
    $('a[name="task_start_time"]').live('click', function() {
          
            //alert('in');
            // sort ascending
            if(task_start_time_ascend == true) {
                //grab HTML snippit from server - handler functionality  
                $('#task-table').load("/sorted2/");  
                task_start_time_ascend = false;
            }
            // sort descending
            else {
                $('#task-table').load("/sorted4/");  
                task_start_time_ascend = true;
            }
            //so that the click event will do the above actions only 
            return false;    
    });
});
