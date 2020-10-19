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
    // 用户验证
    console.log("进来了")
    error = $('.error').data('error');
    if (error !== '') {
        M.toast({html: error}, 2000);
    }
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
        success: function (data) {
            msg = data['msg'];
            M.toast({html: msg}, 2000);  // Materialize 提示
        },
        complete: function () {
        }
    })
}

function edit_item(e) {
    // 输入的时候编辑输入任何内容都会触发这个函数
    var $edit_input = $('#edit-item-input');
    var value = $edit_input.val().trim();
    if (e.which !== 13 || !value) {
        return;
    }
    $edit_input.val('');

    if (!value) {
        M.toast({html: "请输入内容！"});
        return;
    }
    var url = $edit_input.parent().prev().data('href');
    var id = $edit_input.parent().prev().data('id');
    $.ajax({
        type: 'PUT',
        url: url,
        data: JSON.stringify({'id': id, 'content': value}),
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            $('#body' + id).html(value);
            $edit_input.parent().prev().data('body', value);
            remove_edit_input();
            M.toast({html: data.msg},2000);
        },
        complete: function () {
            $('#todo-card' + id).load("http://localhost:8000/" + " .todo-body" + id);
        }
    })
}

// edit item
$(document).on('keyup', '#edit-item-input', edit_item.bind(this));

// 编辑没有修改内容返回页面状态显示todo
function remove_edit_input() {
    var $edit_input = $('#edit-item-input');
    $edit_input.parent().prev().show();
    $edit_input.parent().remove();
};

function del_todo(e) {
    // debugger;
    var url = $(e).data('href');
    var $item = $(e).parent().parent().parent();
    var id = $item.data('id');
    $.ajax({
        type: 'POST',
        url: url,
        data: JSON.stringify({'id': id}),
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            M.toast({html: data.msg}, 1000);
        },
        complete: function () {
            setTimeout("window.location.reload()", 1000);
        }
    })
}

$(document).on('click', '.edit-btn', function () {
    var $item = $(this).parent().parent().parent();
    var item_id = $item.data('id');
    var item_content = $('#text' + item_id).text();
    // debugger;
    $item.hide();
    // 点击编辑变成输入框
    $item.after(' \
                <div class="row card-panel hoverable">\
                <input class="validate" id="edit-item-input" type="text" value="' + item_content + '"\
                autocomplete="off" autofocus required> \
                </div> \
            ');
    // 按键检测
    var $edit_input = $('#edit-item-input');
    $(document).on('keydown', function (e) {
        if (e.keyCode === 27) {
            remove_edit_input();
        }
    });

    // 鼠标移开编辑
    $edit_input.on('focusout', function () {
        remove_edit_input();
    })
});





