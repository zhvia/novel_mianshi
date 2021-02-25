window.onload = function () {
    $("#id_name").blur(function () {
        let username = $('#id_name').val()
        let check1 = /^[0-9]+$/
        let checkEn = /[`!@#$%^&*()_+<>?:",{}.\/;'\\ ]/
        let checkCn = /[·！#￥（—）：；“”‘、，|《。》？【】\\]/
        if (username.length < 4) {
            $('#msg_name').text('请最少输入4个字符串的用户名')
        } else {
            if (check1.test(username)) {
                $('#msg_name').text('不可以是全数字')
            } else {
                if (checkEn.test(username) || checkCn.test(username)) {
                    $('#msg_name').text('不可以含有非法字符')
                } else {
                    $('#msg_name').text('')
                }
            }
        }

    })


    $('#id_psw').blur(
        function () {
            if ($("#id_psw").val().length === 0) {
                $('#msg_psw').text('请输入密码')
            } else {
                $('#msg_psw').text('')
            }
        }
    )


    $('#re_psw').blur(function (){
        if ($("#id_psw").val() === $('#re_psw').val()){
            $('#msg_re_psw').text('')
        }
        else {
            $('#msg_re_psw').text('密码不一致')
        }
    })

    $('#register_form').submit(function (){
        let name = $('#id_name').val()
        let psw = $('#id_psw').val()
        let code = $('#code_input').val()
        if (name === '' || code === '' || psw === ''){
            alert('请输入账号密码')
            return false
        }
        else {
            return true
        }
    })



}