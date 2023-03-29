var korea = {};
$.getJSON("korea.json", function (json) {
    korea = json;
    //console.log(korea);
});

$(".land").on("mouseenter", function () {
    var id = $(this).attr("id");
    //alert(id);
    if (!id) return;
    var cities = korea.korea.city;
    var city = getCityById(cities, id);
    if (city.length > 0) {
        var cityinfo = city[0];
        $("#name_ko").text(cityinfo.name_ko);
        
    }
});

$(".land").on("mouseleave", function () {
    $("#name_ko").text("");
});

function getCityById(data, id) {
    return data.filter(
        function (data) { return data.id == id }
    );
}