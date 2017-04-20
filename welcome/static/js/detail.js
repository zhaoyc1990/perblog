/*

@Name：不落阁整站模板源码 
@Author：Absolutely 
@Site：http://www.lyblogs.cn

*/
var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
var csrftoken = csrfitems[0].value;
prettyPrint();
layui.use(['form', 'layedit'], function () {
    var form = layui.form();
    var $ = layui.jquery;
    var layedit = layui.layedit;

    //评论和留言的编辑器
    var editIndex = layedit.build('remarkEditor', {
        height: 150,
        tool: ['face', '|', 'left', 'center', 'right', '|', 'link'],
    });
    //评论和留言的编辑器的验证
    layui.form().verify({
        content: function (value) {
            value = $.trim(layedit.getText(editIndex));
            if (value == "") return "自少得有一个字吧";
            layedit.sync(editIndex);
        }
    });

    //监听评论提交
    form.on('submit(formRemark)', function (data) {
        var index = layer.load(1);
        var artid = $("#artid").text()
        //模拟评论提交
        $.ajax({
            type: 'post',
            url: '/api/article/rely',
            contentType: 'application/json',
            data: JSON.stringify({ "content": data.field.editorContent, "artid": artid}),
            datatype: 'json',
            success: function (res) {
                if (res.Success) {
                    formadd(index, res.data, res.avatar, res.name, res.time)
                } else {
                    layer.msg('评论失败', { icon: 2 });
                }
            },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            error: function (e) {
                layer.msg(e.responseText);
            }
        });
        return false;
    });

    //data 提交的内容，avatar头像
    function formadd(index, data, avatar, name, time) {
        layer.close(index);
        //var content = data.field.editorContent;
        var content = data
        if (typeof(name) == 'undefined' || name == ''){
            name = '未知'
        }
        var html = '<li><div class="comment-parent"><img src="' + avatar + '"alt="absolutely"/><div class="info"><span class="username">'+ name +'</span><span class="time">' + time +'</span></div><div class="content">' + content + '</div></div></li>';
        $('.blog-comment').append(html);
        $('#remarkEditor').val('');
        editIndex = layui.layedit.build('remarkEditor', {
            height: 150,
            tool: ['face', '|', 'left', 'center', 'right', '|', 'link'],
        });
        layer.msg("评论成功", { icon: 1 });
    }
});