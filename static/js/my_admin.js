window.onload = function () {
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
                }
            }
        }
        return cookieValue;
    };
    $(function () {
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
    });
        console.log('DOM loaded');
        $('.recover').on('click', '', function (event){
            console.log(event.target);
            $.post({
                url: 'user/recover/' + event.target.id + '/',
                success: function (data) {
                    $('.users_list').html(data.result);
                },
            });
        event.preventDefault();
        });
    }