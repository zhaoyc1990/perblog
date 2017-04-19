/*

@Name：不落阁整站模板源码 
@Author：Absolutely 
@Site：http://www.lyblogs.cn

*/
var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
var csrftoken = csrfitems[0].value;

layui.use(['jquery', 'flow'], function () {
    var $ = layui.jquery;
	var flow = layui.flow;
	
	    //信息流
    flow.load({
        elem: '.blog-main-left', //指定列表容器
        isAuto: true,
        end: '没有更多了',
        mb: 200,
        done: function (page, next) {
            var pages;  //总页数
            var lis = [];   //html
            if (page == 1) {
                next(lis.join(''), page < 999999);
                return;
            }
            $.ajax({
                type: 'post',
                url: '/api/article/next',
                contentType: 'application/json',
                data: JSON.stringify({ "currentIndex": page, "pageSize": 1, "type": 1 }),
                datatype: 'json',
                success: function (res) {
                    if (res.Success) {
                        lis.push(res.Data);
                        pages = res.SubCode;
                        next(lis.join(''), page < pages);
                    } else {
                        layer.msg('获取数据失败', { icon: 2 });
                    }
                },
                beforeSend: function(xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                error: function (e) {
                    layer.msg(e.responseText);
                }
            });
        }
    });

	
    $(function () {
        //播放公告
        playAnnouncement(3000);
    });
    function playAnnouncement(interval) {
        var index = 0;
        var $announcement = $('.home-tips-container>span');
        //自动轮换
        setInterval(function () {
            index++;    //下标更新
            if (index >= $announcement.length) {
                index = 0;
            }
            $announcement.eq(index).stop(true, true).fadeIn().siblings('span').fadeOut();  //下标对应的图片显示，同辈元素隐藏
        }, interval);
    }
});
