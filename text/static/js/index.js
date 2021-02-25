

window.onload=function () {

    // 注销
    $("#logout").click(function (){
        window.location.href='/logout/'
    })

    // //
    // $("#search_button").click(function (){
    //     let search_info = $("#search_input").val()
    //     $.ajax({
    //         url:'http://127.0.0.1:8000/ajax_search/',
    //         headers: {'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()},
    //         data:{'search_info': search_info},
    //         method: 'post',
    //         dataType: 'json',
    //         success(data){
    //             if (data){
    //                 for(var i=0;i<data.length;i++){
    //                     $('#child').html('<li>'+data[i]['fields']['book_name']+'</li>'+'<li>'+data[i]['fields']['book_author']+'</li>')
    //                 }
    //             }
    //         }
    //     })
    // })
}


//登录按钮  和  注销按钮  的切换
$(document).ready(function (){
        if ($.cookie('username') && ($.cookie('username'))!==''){
            $("#login").css('display','none')
        }
        else {
            $("#logout").css('display','none')
        }

    }



)