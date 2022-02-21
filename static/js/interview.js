
$(document).ready(function () {

  //GET SQL ANSWERS
  $.get("/questions_info", {}).done(function (response, statusText, xhr) {
      // x.innerHTML = "Execute";

      if(xhr.status!=200)
      {
        document.getElementById("error-message").innerHTML = response;
      } else {
        document.getElementById("error-message").innerHTML = null;
        document.getElementById("dataresetalert").style.visibility = "hidden";
        
        for (const [key, value] of Object.entries(response)) {

          BuildTable('results_'.concat(key), value['answer']['result'])
        }
        
    }
    });


  //SET UP SQL TEXTAREA
  var mime = 'text/x-mariadb';
  // get mime type
  if (window.location.href.indexOf('mime=') > -1) {
    mime = window.location.href.substr(window.location.href.indexOf('mime=') + 5);
  }
  window.editor = CodeMirror.fromTextArea(document.getElementById('query'), {
    mode: mime,
    indentWithTabs: true,
    lineNumbers: true,
    matchBrackets : true,
    autofocus: true,
    theme: 'base16-light',
    extraKeys: {"Ctrl-Space": "autocomplete"},
    hintOptions: {tables: {
      users: ["name", "score", "birthDate"],
      countries: ["name", "population", "size"]
    }}
    
  });
  window.editor.getDoc().setValue('SELECT * FROM Trade')

  $("button#refresh").click(function(){

    $.get("/refresh");
    window.location.reload();
    // document.getElementById("dataresetalert").style.visibility = "visible";
  });

  $("button#run").click(function(){
    // var query = $('textarea#query').val();

    var query = window.editor.getValue()
    
    var x = document.getElementById("run");
    x.innerHTML = "running...";

    var data = {};
    data['query'] = query;

    $.get("/query", data).done(function (response, statusText, xhr) {
      x.innerHTML = "Execute";

      if(xhr.status!=200)
      {
        document.getElementById("error-message").innerHTML = response;
      } else {
        document.getElementById("error-message").innerHTML = null;
        document.getElementById("dataresetalert").style.visibility = "hidden";

    
        BuildTable('results_table', response)
        
    }
    });
  });

  function BuildTable(table_id, response) {
      var table = document.getElementById(table_id);

      // delete any existing table
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
          }
      }
  }
});
