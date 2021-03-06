﻿/*

@Name：不落阁整站模板源码 
@Author：Absolutely 
@Site：http://www.lyblogs.cn

*/
var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
var csrftoken = csrfitems[0].value;
layui.use(['element', 'jquery', 'form', 'layedit'], function () {
    var element = layui.element();
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
            value = $.trim(layedit.getText(editIndex));
            if (value == "") return "自少得有一个字吧";
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

    //Hash地址的定位
    var layid = location.hash.replace(/^#tabIndex=/, '');
    if (layid == "") {
        element.tabChange('tabAbout', 1);
    }
    element.tabChange('tabAbout', layid);

    element.on('tab(tabAbout)', function (elem) {
        location.hash = 'tabIndex=' + $(this).attr('lay-id');
    });

    //监听留言提交
    form.on('submit(formLeaveMessage)', function (data) {
        var index = layer.load(1);
        var message = data.field.editorContent;
        var name = data.field.name;
        var email = data.field.email;
        var website = data.field.website;
        $.ajax({
            type: 'post',
            url: '/api/message',
            contentType: 'application/json',
            data: JSON.stringify({ "content": message, "name": name, "email": email, "website": website}),
            datatype: 'json',
            success: function (res) {
                layer.close(index);
                if (res.Success) {
                    if( res.website == "") {
                        var html = '<li><div class="comment-parent" id="comment-'+ res.id +'"><img src="' + res.avatar + '"alt="模拟留言"/><div class="info"><span class="username">' + res.name + '</span></div><div class="content">' + message + '</div><p class="info"><span style="color:#BBBBBB;">您的留言，将在博主审核后，出现在这里</span></p><p class="info info-footer"><span class="time">'+ res.time + '</span><a class="btn-reply"href="javascript:;" onclick="btnReplyClick(this)">回复</a></p></div></li>';

                    } else {
                        var html = '<li><div class="comment-parent" id="comment-'+ res.id +'"><img src="' + res.avatar + '"alt="模拟留言"/><div class="info"><a target="_blank" href="' + res.website + '"><span class="username">' + res.name + '</span></a></div><div class="content">' + message + '</div><p class="info"><span style="color:#BBBBBB;">您的留言，将在博主审核后，出现在这里</span></p><p class="info info-footer"><span class="time">'+ res.time + '</span><a class="btn-reply"href="javascript:;" onclick="btnReplyClick(this)">回复</a></p></div></li>';

                    }
                    $('.blog-comment').append(html);
                    $('#remarkEditor').val('');
                    editIndex = layui.layedit.build('remarkEditor', {
                        height: 150,
                        tool: ['face', '|', 'left', 'center', 'right', '|', 'link'],
                    });
                    layer.msg("留言成功", { icon: 1 });
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

    //监听留言回复提交
    form.on('submit(formReply)', function (data) {
        var index = layer.load(1);
        var message_reply_id = data.field.replyid;
        var message = data.field.replyContent;
        var name = data.field.username;
        var website = data.field.website;
        var email = data.field.email;
        $.ajax({
            type: 'post',
            url: '/api/message',
            contentType: 'application/json',
            data: JSON.stringify({ "id": message_reply_id, "content": message, "name": name, "email": email, "website": website}),
            datatype: 'json',
            success: function (res) {
                layer.close(index);
                if (res.Success) {
                    if (res.website == ""){
                        var html = '<div class="comment-child" id="comment-'+ res.id +'"><img src="' + res.avatar +'"alt="Absolutely"/><div class="info"><span class="username">' + res.name + '</span><span>' + message + '</span></div><p class="info"><span style="color:#BBBBBB;">您的回复，将在博主审核后，出现在这里</span></p><p class="info"><span class="time">'+ res.time + '</span></p></div>';

                    } else {
                        var html = '<div class="comment-child" id="comment-'+ res.id +'"><img src="' + res.avatar +'"alt="Absolutely"/><div class="info"><a target="_blank" href="' + res.website +'" <span class="username">' + res.name + '</span></a><span>' + message + '</span></div><p class="info"><span style="color:#BBBBBB;">您的回复，将在博主审核后，出现在这里</span></p><p class="info"><span class="time">'+ res.time + '</span></p></div>';

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
systemTime();

function systemTime() {
    //获取系统时间。
    var dateTime = new Date();
    var year = dateTime.getFullYear();
    var month = dateTime.getMonth() + 1;
    var day = dateTime.getDate();
    var hh = dateTime.getHours();
    var mm = dateTime.getMinutes();
    var ss = dateTime.getSeconds();

    //分秒时间是一位数字，在数字前补0。
    mm = extra(mm);
    ss = extra(ss);

    //将时间显示到ID为time的位置，时间格式形如：19:18:02
    document.getElementById("time").innerHTML = year + "-" + month + "-" + day + " " + hh + ":" + mm + ":" + ss;
    //每隔1000ms执行方法systemTime()。
    setTimeout("systemTime()", 1000);
}

//补位函数。
function extra(x) {
    //如果传入数字小于10，数字前补一位0。
    if (x < 10) {
        return "0" + x;
    }
    else {
        return x;
    }
}