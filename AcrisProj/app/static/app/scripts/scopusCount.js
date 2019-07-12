$(document).ready(function () {
    $(document.getElementById("id_pubmedid")).change(function () {
        //alert("The text has been changed.");
        get_count();
    });
});



function get_count() {
    //alert("inside ajax."); // sanity check
    $.ajax({
        url: "/scopus_citation/", // the endpoint
        type: "GET", // http method
        data: { pubmedid: $('#id_pubmedid').val() }, // data sent with the post request

        // handle a successful response
        success: function (json) {
            //$('#post-text').val(''); // remove the value from the input
           // alert(json); // log the returned json to the console
            $("#id_citation_count").val(json.cit_count);
           // alert("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            //$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
            //    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};