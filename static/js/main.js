var request = new XMLHttpRequest();

$('#hn_value').keypress(function (e) {
  var key = e.which;
  if(key == 13){
    $(function (){
      data = document.querySelector('#hn_value').value.replace(/[`~!@#$%^&*()_|+=?;:'",.<>\{\}\[\]\\\/]/gi, '');
      if(data.length > 6){
        request.open('POST', '/request', true);
        request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
        request.send(data);
        request.onreadystatechange = function() {
          if(request.status == 200 && request.readyState == 4){
              var string_data = request.responseText;
              var json_data = JSON.parse(string_data);
              productsAdd(json_data)
          }
        }
      }
    });
  }
});
function productsAdd(hn_list) {
  $("#table_hosts tbody tr").remove()
  for(i = 0; i < hn_list.length; i++){
    $("#table_hosts tbody").append(
        "<tr>" +
          "<th scope='row'>"+hn_list[i][0]+"</th>" +
          "<td>"+hn_list[i][1]+"</td>" +
          "<td>"+hn_list[i][2]+"</td>" +
          "<td>"+hn_list[i][3]+"</td>" +
        "</tr>"
    );
  }
}