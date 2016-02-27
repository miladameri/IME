
function initChartHajm(data1, data2) {
    var data = data1;
    var data2 = data2;
    var ctx = document.getElementById("Hajm").getContext("2d");
    new Chart(ctx).Pie(data, {
        responsive: true,
    });
    ctx = document.getElementById("Arzesh").getContext("2d");
    new Chart(ctx).Pie(data2, {
        responsive: true,
    });
    console.log($("#sel1").val());
}

function mainPageCharts() {

    data1 = [];
    data2 = [];
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"];
    $.ajax({
        url: "/maingroup",
        dataType: "json",
        data: {
            "time_slot": 12,
            "type": "trade",
            "end_date": "1392/08/26"
        },
        type: "GET",
        success: function (response) {
            console.log(response);
            datas = response['data']
            for (var i = 0; i < datas[0].length; i++) {
                data1.push(
                    {
                        value: datas[1][i],
                        color: colors[i],
                        label: datas[0][i]
                    }
                );
            }
            initChartHajm(data1, data2);

        },
        complete: function () {
        },
        error: function (xhr, textStatus, thrownError) {
            alert("error doing something");
        }
    });

    $.ajax({
        url: "/maingroup",
        dataType: "json",
        data: {
            "time_slot": 12,
            "type": "value_KRials",
            "end_date": "1392/08/26"
        },
        type: "GET",
        success: function (response) {
            datas = response['data']
            for (var i = 0; i < datas[0].length; i++) {
                data2.push(
                    {
                        value: datas[1][i],
                        color: colors[i],
                        label: datas[0][i]
                    }
                );
            }
            initChartHajm(data1, data2);

        },
        complete: function () {
        },
        error: function (xhr, textStatus, thrownError) {
            alert("error doing something");
        }
    });
}
