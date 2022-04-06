jQuery(document).ready(function($){
$('.to_close_or_open_1').bind('click',open_and_close);
    function open_and_close(e){
        if($(this).find('.to_close_or_open_3').text()=='(-показать-)'){
        $(this).find('.to_close_or_open_3').text('(-скрыть-)');
        $(this).find('.to_close_or_open_3').css({'color':'#990000'});
        }
        else{
        $(this).find('.to_close_or_open_3').text('(-показать-)');
        $(this).find('.to_close_or_open_3').css({'color':'#006622'});
        }
    $(this).next('.to_close_or_open_2').toggle(200);
    }
});