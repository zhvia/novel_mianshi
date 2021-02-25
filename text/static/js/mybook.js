
window.onload = function() {
    $(".add_book").click(function () {
        let book_id = $(this).prop("id")
        $.ajax({
            type: "post",
            url: "/my_book/" + book_id,
            data: {'book_id': book_id},
            success: function (data) {
                if (data === 'fail') {
                    alert('不可重复添加')
                } else {
0
                    alert('添加成功')
                }
                console.log(data)
            },

            error: function (data) {//请求出错
                alert("出错");
            },
        });

    })
}