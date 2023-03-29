var korea = {};
$.getJSON("assets/korea.json", function (json) {
    korea = json;
    console.log(korea);
});

$(".land").on("click", function () {
    var id = $(this).attr("id");
    //alert(id);
    if (!id) return;
    var cities = korea.korea.city;
    var city = getCityById(cities, id);
    if (city.length > 0) {
        var cityinfo = city[0];
        $("#name_ko").text(cityinfo.name_ko);
        // $("#name_full").text(cityinfo.name_full);
        // $("#info").text(cityinfo.info);
    }
});

function getCityById(data, id) {
    return data.filter(
        function (data) { return data.id == id }
    );
}
