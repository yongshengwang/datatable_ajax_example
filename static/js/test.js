$(document).ready(function() {

    $('#example').dataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "../get/"
        },
        "columnDefs": [
            {"targets": 0, "data": "name" },
            {"targets": 1, "data": "age" },
            {
            "targets": 2,
            "data": 'link',
             "render": function ( data, type, full, meta ) {
                 return '<button onclick=alert('+
                     data.id+') value='+data.id+'>'+
                     data.action+'</button>';
             }
        } ]
    } );
} );