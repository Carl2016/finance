layui.use('element', function () {
    var $ = layui.jquery
        , element = layui.element; //Tab的切换功能，切换事件监听等，需要依赖element模块


    var titleArr =  new Array("首页");
    //var idArr =  new Array();
    //触发事件
    var active = {

        tabAdd: function (othis) {
            //新增一个Tab项
            const title = othis.text();
            if ($.inArray(title, titleArr) != -1) {
                // 存在，跳转到那个标签
                element.tabChange('demo', title); //切换到：用户管理
            } else {
                titleArr.push(title);
                element.tabAdd('demo', {
                    title: title //用于演示
                    , content: "<iframe frameborder='0' width='100%' height='100%' scrolling='no' src='"+othis.attr("data-url")+"' data-id='"+title+"' name='ifr_"+title+"' id='ifr_"+title+"' ></frame>"
                    , id:  title//实际使用一般是规定好的id，这里以时间戳模拟下
                });
                element.tabChange('demo', title); //切换到：用户管理
            }
            console.log(titleArr);
        }
        , tabDelete: function (othis) {
            //删除指定Tab项
            const title = othis.text();
            element.tabDelete('demo', title); //删除：
            titleArr.pop(title);
            console.log(titleArr);
            //othis.addClass('layui-btn-disabled');
        }
        , tabChange: function (othis) {
            //切换到指定Tab项
            const title = othis.text();
            element.tabChange('demo', title); //切换到：用户管理
        }
    };

    // 动作操作
    $('.site-demo-active').on('click', function () {
        var othis = $(this), type = othis.data('type');
        active[type] ? active[type].call(this, othis) : '';
    });

    $('.layui-tab-close').on('click', function () {
        alert(1111);
        var othis = $(this), type = "tabDelete";
        active[type] ? active[type].call(this, othis) : '';
    });

    //Hash地址的定位
    // var layid = location.hash.replace(/^#test=/, '');
    // element.tabChange('test', layid);
    //
    // element.on('tab(test)', function (elem) {
    //     location.hash = 'test=' + $(this).attr('lay-id');
    // });

});