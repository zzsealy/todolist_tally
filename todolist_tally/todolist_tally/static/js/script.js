$(document).ready(function () {
    $('.tooltipped').tooltip({delay: 50});
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

function toggle_todo(e) {
    var $t = $(e);
    var url = $t.data('href')
    var id = $t.data('id')
    $.ajax({
        url: url,
        type: 'POST',
        async: false,
        data: JSON.stringify({'id': id}),
        contentType: 'application/json;charset=UTF-8',
        success: function (data){
            msg = data['msg'];
            M.toast({html:msg }, 2000);  // Materialize 提示
        },
        complete: function () {
            $('#todo-card' + id).load("http://localhost:8000/" + " .todo-body" + id);
        }
    })
}

$(document).on('click', '.edit-btn', function(){
    debugger;
    var $item = $(this).parent().parent();
    var item_id = $item.data('.id');
    var item_content = $('#text' + item_id).text();
    $item.hide();
    $item.after(' \
                <div class="row card-panel hoverable">\
                <input class="validate" id="edit-item-input" type="text" value="' + itemBody + '"\
                autocomplete="off" autofocus required> \
                </div> \
            ');
});





