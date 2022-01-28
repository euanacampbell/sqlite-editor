


$(document).ready(function(){

  $("button#refresh").click(function(){
    console.log('refreshing tables');

    $.get("/refresh");
    document.getElementById("dataresetalert").style.visibility = "visible";
  });

  $("button#run").click(function(){
    var query = $('textarea#query').val();
    
    var x = document.getElementById("run");
    x.innerHTML = "running...";

    var data = {};
    data['query'] = query;

    $.get("/query", data).done(function (response, statusText, xhr) {
      x.innerHTML = "RUN";

      if(xhr.status!=200)
      {
        document.getElementById("error-message").innerHTML = response;
      } else {
        document.getElementById("error-message").innerHTML = null;
        document.getElementById("dataresetalert").style.visibility = "hidden";

        var table = document.getElementById("results");

        // delete any existing table
        while(table.rows.length > 0) {
          table.deleteRow(0);
        }

        // build new table
        for (var key in response) {
          if (response.hasOwnProperty(key)) {
              var row = table.insertRow(-1);

              var i;
              var cellValue = ''
              for (i = 0; i < response[key].length; i++) { 
                var cell = row.insertCell(i);
                if (response[key][i] === undefined || response[key][i] === null){
                  cellValue = 'NULL'
                } else {
                  cellValue = response[key][i]
                }
                cell.innerHTML = cellValue;
              }
          }
      }
      
    }
    });
  });
});
