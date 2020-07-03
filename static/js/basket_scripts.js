window.onload = function () {
    console.log('DOM loaded');
    $('.basket_list').on('change', 'input[type=number]', function (event) {
        console.log(event.target);
        $.ajax({
            url: '/basket/change/' + event.target.name + '/quantity/' + event.target.value + '/',
            success: function (data) {
                console.log(data)
            }
        });
    })
};