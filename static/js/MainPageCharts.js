
function initChartHajm(data1, data2) {
    var data = [
        {
            value: 300,
            color: "#F7464A",
            highlight: "#FF5A5E",
            label: "?????"
        },
        {
            value: 50,
            color: "#46BFBD",
            highlight: "#5AD3D1",
            label: "???????"
        },
        {
            value: 100,
            color: "#FDB45C",
            highlight: "#FFC870",
            label: "?????"
        },
        {
            value: 40,
            color: "#949FB1",
            highlight: "#A8B3C5",
            label: "????????"
        },
        {
            value: 120,
            color: "#4D5360",
            highlight: "#616774",
            label: "??????????? ????"
        }

    ];
    var data2 = [
        {
            value: 90,
            color: "#F7464A",
            highlight: "#FF5A5E",
            label: "?????"
        },
        {
            value: 25,
            color: "#46BFBD",
            highlight: "#5AD3D1",
            label: "???????"
        },
        {
            value: 100,
            color: "#FDB45C",
            highlight: "#FFC870",
            label: "?????"
        },
        {
            value: 16,
            color: "#949FB1",
            highlight: "#A8B3C5",
            label: "????????"
        },
        {
            value: 14.4,
            color: "#4D5360",
            highlight: "#616774",
            label: "??????????? ????"
        }

    ];
    var ctx = document.getElementById("Hajm").getContext("2d");
    new Chart(ctx).PolarArea(data, {
        responsive: true,
    });
    ctx = document.getElementById("Arzesh").getContext("2d");
    new Chart(ctx).PolarArea(data2, {
        responsive: true,
    });
    console.log($("#sel1").val());
}

$(document).ready(function () {

    console.log("in my js")
    $.ajax({
        url: "/maingroup",
        dataType: "json",
        data: {
            "time_slot": 12,
            "type": "trade",
            "end_date": "1394/08/26"
        },
        type: "GET",
        success: function (response) {
            console.log("im heeree");
            var rawdata = response['data'][1];
            var sum = 0;
            for (var i = 0; i < rawdata.length; i++) {
                sum += rawdata[i];
            }
        },
        complete: function () {
        },
        error: function (xhr, textStatus, thrownError) {
            alert("error doing something");
        }
    });

    initChartHajm(1, 2);


});
