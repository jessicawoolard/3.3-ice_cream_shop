$(document).ready(function () {
    $(".btnShowHide").click(function () {
        if ($(this).val() == "Date Churned") {
            $(this).val($(this).attr('title'));
        } else {
            $(this).val("Date Churned");
        }
    });
});