$(document).ready(function() {
    $('.btn_del').click(function(e) {
        e.preventDefault();
        var id = $(this).data('id');
        $.ajax({
            type: 'POST',
            url: '/delete/' + id + '/',
            data: {
                csrfmiddlewaretoken: csrfToken, // Используем токен CSRF из глобальной переменной
                id: id
            },
            success: function() {
                window.location.href = '/mytrainings/';
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
                alert('Произошла ошибка при удалении!');
            }
        });
    });
});
