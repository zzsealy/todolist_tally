$(document).ready(function () {
    $('.card-panel').each(function () {
        $(this).mouseover(function () {
            // debugger;
            $(this).find('#change-todo-in-card').css({'display': 'block'});
        })
        $(this).mouseout(function () {
            $(this).find('#change-todo-in-card').css({'display': 'none'});
        })
    })



})

function edit_todo(e) {
    var $t = $(e);
    var url = $t.data('href')
    var id = $t.data('id')
    $.ajax({
        url: url,
        type: 'POST',
        data: JSON.stringify({'id': id}),
        contentType: 'application/json;charset=UTF-8',
        success: function (){

        },
        complete: function () {
            $('#todo-card' + id).load("http://127.0.0.1:8000/" + " .todo-body" + id);
        }
    })
    var done = $('.todo-body' + id).data('done');
            if (done==='True'){
                $('#text' + id).addClass("active-item");

            } else {
                $('#text' + id).addClass("inactive-item");
            }
}

// function erase(id){
//     body = document.getElementById(id);
//     // <SPAN style="TEXT-DECORATION: line-through">Line-through</SPAN>
//     $todo_span = $(body)
//     $todo_span.css({"text-decoration":"line-through"});
//
// }




