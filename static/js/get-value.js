$(document).ready(function(){
    $('#buttonASC').click(function(){
        $.getJSON('/process/orderBy',{
            orderBy: $('button[name=orderByASC]').val()
        })
    })
})

$(document).ready(function(){
    $('#buttonDESC').click(function(){
        $.getJSON('/process/orderBy',{
            orderBy: $('button[name=orderByDESC]').val()
        })
    })
})
//DOM manipulációval kicserélni az adatokat!!!