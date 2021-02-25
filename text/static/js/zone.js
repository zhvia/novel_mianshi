window.onload=function (){
    $('#zone_button').click(function (){
        console.log('sjaghfujsabij')
        $("#name").removeAttr('disabled')
        $("#phone").removeAttr('disabled')
        $(".select").removeAttr('disabled')
        // $("#phone").attr('disabled',false)
        // $(".select").attr('disabled', false)
        $(this).val('确定')
        $(this).attr('disabled',true)
        $("#zone_submit").attr('disabled',false)
    })
}