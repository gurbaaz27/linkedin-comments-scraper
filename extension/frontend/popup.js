$(document).ready(function() {
    $('form').on('submit', function(event) {
    $.ajax({
        data : {
            email : $('#email').val(),
            password: $('#password').val(),
            posturl: $('$posturl').val(),
            downloadpfp: $('$downloadpfp').val()
            },
            type : 'POST',
            url : 'https://gurbaaz.pythonanywhere.com/api'
            })
        .done(function(data) {
        $('#output').text(data.output).show();
    });
    event.preventDefault();
    });
});