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
    var submit_time = 0;
    //评论和留言的编辑器的验证
    layui.form().verify({
        content: function (value) {
            if (Date.parse(new Date())-submit_time < 10000) {
                return "着什么急"
            }
            value = $.trim(layedit.getText(editIndex));
            if (value == "") return "自少得有d一个字吧";
            layedit.sync(editIndex);
        },
        replyContent: function (value) {
            if (Date.parse(new Date())-submit_time < 10000) {
                return "着什么急"
            }
            if (value=="") return "自少得有一个字吧";
            value = $.trim(layedit.getText(editIndex));
            layedit.sync(editIndex);
        }
    });
    //监听评论提交
    form.on('submit(formRemark)', function (data) {
        var index = layer.load(1);
        var artid = $("#artid").text();
        var name = data.field.name;
        var email = data.field.email;
        var website = data.field.website;
        //模拟评论提交
        $.ajax({
            type: 'post',
            url: '/api/article/rely',
            contentType: 'application/json',
            data: JSON.stringify({ "content": data.field.editorContent, "artid": artid, "name": name, "email": email, "website": website}),
            datatype: 'json',
            success: function (res) {
                layer.close(index);
                if (res.Success) {
                    formadd( data.field.editorContent,res)
                } else {
                    if (typeof(res.message)!= "undefined"){
                        layer.msg("<span style='color:#777777;'>" + res.message +"</span>", { icon: 2 });
                    } else {
                        layer.msg("<span style='color:#777777;'>评论失败</span>", { icon: 2 });
                    }
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
    function formadd( data, res) {

        //var content = data.field.editorContent;
        var content = data
        if (typeof(name) == 'undefined' || name == ''){
            name = '未知'
        }
        if (res.website == '') {
            var html = '<li><div class="comment-parent" id="comment-'+ res.id +'"><img src="' + res.avatar + '"alt="absolutely"/><div class="info"><span class="username">'+ res.name +'</span><span class="time">' + res.time +'</span></div><div class="content">' + res.content + '</div><p class="info info-footer"><span class="time" style="color:#BBBBBB;">您的评论，将在博主审核后，出现在这里</span></p></div></li>';
        } else {
            var html = '<li><div class="comment-parent" id="comment-'+ res.id +'"><img src="' + res.avatar + '"alt="absolutely"/><div class="info"><a target="_blank" href="' + res.website +'"> <span class="username">'+ res.name +'</span></a><span class="time">' + res.time +'</span></div><div class="content">' + res.content + '</div><p class="info info-footer"><span class="time" style="color:#BBBBBB;">您的评论，将在博主审核后，出现在这里</span></p></div></li>';
        }
        $('.blog-comment').append(html);
        $('#remarkEditor').val('');
        editIndex = layui.layedit.build('remarkEditor', {
            height: 150,
            tool: ['face', '|', 'left', 'center', 'right', '|', 'link'],
        });
        layer.msg("评论成功", { icon: 1 });
        location.hash="#comment-" + res.id;
        topindex = $(document).scrollTop();
        $(document).scrollTop(topindex-70);
    }
    //监听留言回复提交
    form.on('submit(formReply)', function (data) {
        var index = layer.load(1);
        var artid = $("#artid").text();
        var art_reply_id = data.field.replyid;
        var message = data.field.replyContent;
        var name = data.field.username;
        var website = data.field.website;
        var email = data.field.email;
        $.ajax({
            type: 'post',
            url: '/api/article/rely',
            contentType: 'application/json',
            data: JSON.stringify({ "art_rely": art_reply_id, "content": message, "name": name, "email": email, "website": website, "artid":artid}),
            datatype: 'json',
            success: function (res) {
                layer.close(index);
                if (res.Success) {
                    if (res.website == ""){
                        var html = '<div class="comment-child" id="comment-'+ res.id +'"><img src="' + res.avatar +'"alt="Absolutely"/><div class="info"><span class="username">' + res.name + '</span><span>' + message + '</span></div><p class="info"><span class="time">'+ res.time + '</span></p><p class="info"><span style="color:#BBBBBB;">您的回复，将在博主审核后，出现在这里</span></p></div>';

                    } else {
                        var html = '<div class="comment-child" id="comment-'+ res.id +'"><img src="' + res.avatar +'"alt="Absolutely"/><div class="info"><a target="_blank" href="' + res.website +'" <span class="username">' + res.name + '</span></a><span>回复</span><p class="info">' + message + '</p></div><p class="info"><span class="time">'+ res.time + '</span></p><p class="info"><span style="color:#BBBBBB;">您的回复，将在博主审核后，出现在这里</span></p></div>';

                    }
                    $(data.form).find('textarea').val('');
                    $(data.form).find('.user-info').val('');
                    $(data.form).parent('.replycontainer').before(html).siblings('.comment-parent').children('p').children('a').click();
                    layer.msg("回复成功", { icon: 1 });
                    location.hash="#comment-" + res.id;
                    topindex = $(document).scrollTop();
                    $(document).scrollTop(topindex-70);
                } else {
                    if (typeof(res.message)!= "undefined"){
                        layer.msg("<span style='color:#777777;'>" + res.message +"</span>", { icon: 2 });
                    } else {
                        layer.msg("<span style='color:#777777;'>评论失败</span>", { icon: 2 });
                    }
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

});
function btnReplyClick(elem) {
    var $ = layui.jquery;
    $(elem).parent('p').parent('.comment-parent').siblings('.replycontainer').toggleClass('layui-hide');
    if ($(elem).text() == '回复') {
        $(elem).text('收起')
    } else {
        $(elem).text('回复')
    }
}