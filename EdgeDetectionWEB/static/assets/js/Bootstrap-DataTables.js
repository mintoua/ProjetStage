var mSortingString = [];
var disableSortingColumn = 4;
mSortingString.push({ "bSortable": false, "aTargets": [disableSortingColumn] });

$(function() {
        var table = $('#example').dataTable({
            "paging": true,
            "ordering": true,
            "info": true,
            "aaSorting": [],
            "orderMulti": true,
            "aoColumnDefs": mSortingString

        });
});
$(function() {
        var table = $('#example2').dataTable({
            "paging": true,
            "ordering": true,
            "info": true,
            "aaSorting": [],
            "orderMulti": true,
            "aoColumnDefs": mSortingString

        });
});