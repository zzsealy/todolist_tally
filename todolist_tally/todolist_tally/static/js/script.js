$(document).ready(function () {
    $('#todo-card').mouseover(function (){
        $('#change-todo-in-card').css({'display':'block'});
    })
    $('#todo-card').mouseout(function (){
        $('#change-todo-in-card').css({'display':'none'});
    });

})

function edit_todo(e){
    $t = $(e);
    url = $t.data('href')
    id = $t.data('id')

    $.ajax({
        url : url,
        type: 'POST',
        data: JSON.stringify({'id':id }),
        contentType: 'application/json;charset=UTF-8',
    })

    body_id = 'body' + id;
    erase(body_id)
}

function erase(id){
    body = document.getElementById(id);
    // <SPAN style="TEXT-DECORATION: line-through">Line-through</SPAN>
    $todo_span = $(body)
    $todo_span.css({"text-decoration":"line-through"});

}




