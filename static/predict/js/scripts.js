$(document).ready(function () {
    $('#man-search-field').on('input', function (e) {
        $.ajax({
            url: '/ajax_search_male/',
            data: {
                'search_request': $(this).val(),
            },
            dataType: 'json',
            success: function (data) {
                $('#result_man').empty();
                if (data.result_set.length == 0) {
                    $('#result_man').append($('<p>', { 'class': 'result' }).text('empty'));
                }
                else {
                    data.result_set.forEach(function (item) {
                        var p = $('<p>', { 'class': 'result' }).text(item);
                        $('#result_man').append(p);
                    });
                }
            }
        });

    });

    $('#woman-search-field').on('input', function (e) {
        $.ajax({
            url: "/ajax_search_female/",
            data: {
                'search_request': $(this).val(),
            },
            dataType: 'json',
            success: function (data) {
                $('#result_woman').empty();
                if (data.result_set.length == 0) {
                    $('#result_woman').append($('<p>', { 'class': 'result' }).text('empty'));
                }
                else {
                    data.result_set.forEach(function (item) {
                        var p = $('<p>', { 'class': 'result' }).text(item);
                        $('#result_woman').append(p);
                    });
                }
            }
        });

    });
    $(document).on('click', 'p.result', function(){
        value = $(this).text();
        if ($(this).parent().attr('id')=='result_man'){
            $('#man-search-field').val(value);
            $('#result_man').empty();
        }
        else{
            $('#woman-search-field').val(value);
            $('#result_woman').empty();
        }
    });
});