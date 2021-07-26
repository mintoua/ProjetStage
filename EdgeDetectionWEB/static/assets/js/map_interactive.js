$(document).ready(function() {
  

    var pays = {
        "cm": { name: "Cameroun"},
        "ci": { name: "Côte d'ivoire"},
        "gq": { name: "Guinee_equatoriale"},
        "ga": { name: "Gabon"},
        "td": { name: "Tchad"},
        "cg": { name: "Congo_brazzaville"},
    }

    $("path[id='cm']").css({
        fill:  '#0C4B33',
    })
    $("path[id='ci']").css({
        fill:  '#0C4B33',
    })
    $("path[id='td']").css({
        fill:  '#0C4B33',
    })
    $("path[id='cg']").css({
        fill:  '#0C4B33',
    })
    $("g[id='gq'] path").css({
        fill:  '#0C4B33',
    })
    $("g[id='ga'] path").css({
        fill:  '#0C4B33',
    })
})