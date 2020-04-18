// console.log("test")


// 整个文档执行完才会执行这个函数
$(function () {
    $('#submit').click(function (event) {
        // 阻止默认提交表单的行为
        event.preventDefault();
        var email = $('input[name=email]').val();
        var password = $('input[name=password]').val();
        // var csrf_token = $('input[name=csrf_token]').val();
        var csrftoken = $('meta[name=csrf-token]').attr('content');

        $.ajaxSetup({
            "beforeSend": function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
            }
        });

        $.post({
            'url': '/login/',
            'data': {
                'email': email,
                'password': password,
                // 'csrf_token': csrf_token
            },
            'success': function (data) {
                console.log(data);
            },
            'fail': function (error) {
                console.log(error);
            }
        })
    })
});