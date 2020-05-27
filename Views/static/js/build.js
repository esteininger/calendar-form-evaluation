function callFromServer(){
  $.ajax({
      'url': "/load",
      'method': "GET"
  }).done( function(data) {
    renderTable(data)
  })
}

function renderTable(data){

  var arr = new Array;
  $.each(data, function (index, value) {
      var tempArray = new Array;
      for (var o in value) {
          tempArray.push(value[o]);
      }
      arr.push(tempArray);
  })


  $('#example').dataTable( {
      data: arr,
      columns: [
          { "title": "summary" },
          { "title": "creator_email" },
          { "title": "end_datetime" },
          { "title": "start_datetime" }
      ]
  })
}

$(document).ready(function() {
  callFromServer();
});
