


$(document).ready(function(){
  $("button#refresh").click(function(){
    console.log('refreshing tables');

    $.get("/refresh");
  });

  $("button#run").click(function(){
    var query = $('textarea#query').val();
    
    var x = document.getElementById("run");
    x.innerHTML = "running...";

    console.log(query);

    var data = {};
    data['query'] = query;

    console.log(data)

    $.get("/query", data).done(function (response, statusText, xhr) {

      console.log(response);
      console.log(xhr.status);
      x.innerHTML = "execute";

      if(xhr.status!=200)
      {
        document.getElementById("error-message").innerHTML = response;
      } else {
        document.getElementById("error-message").innerHTML = null;

        var table = document.getElementById("results");

        while(table.rows.length > 0) {
          table.deleteRow(0);
        }

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

              // var cell1 = row.insertCell(0);
              // var cell2 = row.insertCell(1);
              // var cell3 = row.insertCell(2);

              // cell1.innerHTML = response[key][0];
              // cell2.innerHTML = response[key][1];
              // cell3.innerHTML = response[key][2];
          }
      }
    }
    });
  });
});


function myFunction() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
