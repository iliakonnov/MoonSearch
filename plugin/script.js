var url = location.pathname.split("/");
var id = url.pop()
if (id == "") { id = url.pop(); }
$(".film-img-box").after(
'<div class="moonwalk_div">' +
    '<a class="moonwalk_a" target="_blank" href="http://moonwalk-iliago.rhcloud.com/'+id+'">Смотреть на moonwalk</a>' +
'</div>'
);
