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
            "data": null,
            "defaultContent": "<button>Click!</button>"
        } ]
    } );
} );/**
 * Created by Tiny on 2015/7/4.
 */

//$('#example').dataTable( {
//  "columnDefs": [ {
//    "targets": 0,
//    "data": "download_link",
//    "render": function ( data, type, full, meta ) {
//      return '<a href="'+data+'">Download</a>';
//    }
//  } ]
//} );