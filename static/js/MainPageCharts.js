
function initChartHajm(data1, data2) {
    var data = data1;
    console.log(data);
    //    [
    //    {
    //        value: 300,
    //        highlight: "#FF5A5E",
    //        label: "?????"
    //    },
    //    {
    //        value: 50,
    //        highlight: "#5AD3D1",
    //        label: "???????"
    //    },
    //    {
    //        value: 100,
    //        highlight: "#FFC870",
    //        label: "?????"
    //    },
    //    {
    //        value: 40,
    //        highlight: "#A8B3C5",
    //        label: "????????"
    //    },
    //    {
    //        value: 120,
    //        highlight: "#616774",
    //        label: "??????????? ????"
    //    }
    //
    //];
    var data2 = data2;
    //    [
    //    {
    //        value: 90,
    //        color: "#F7464A",
    //        highlight: "#FF5A5E",
    //        label: "?????"
    //    },
    //    {
    //        value: 25,
    //        color: "#46BFBD",
    //        highlight: "#5AD3D1",
    //        label: "???????"
    //    },
    //    {
    //        value: 100,
    //        color: "#FDB45C",
    //        highlight: "#FFC870",
    //        label: "?????"
    //    },
    //    {
    //        value: 16,
    //        color: "#949FB1",
    //        highlight: "#A8B3C5",
    //        label: "????????"
    //    },
    //    {
    //        value: 14.4,
    //        color: "#4D5360",
    //        highlight: "#616774",
    //        label: "??????????? ????"
    //    }
    //
    //];
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

$(document).ready(function () {
    data1 = [];
    data2 = [];
    colors = ["#F7464A","#46BFBD","#FDB45C","#949FB1","#4D5360"];
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
            datas = response['data']
            console.log('heerees');
            for (var i = 0; i < datas[0].length; i++) {
                data1.push(
                    {   value:datas[1][i],
                        color:colors[i],
                        label:datas[0][i]
                    }
                );
            }
            initChartHajm(data1,data2);

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
            console.log('heerees');
            for (var i = 0; i < datas[0].length; i++) {
                data2.push(
                    {   value:datas[1][i],
                        color:colors[i],
                        label:datas[0][i]
                    }
                );
            }
            initChartHajm(data1,data2);

        },
        complete: function () {
        },
        error: function (xhr, textStatus, thrownError) {
            alert("error doing something");
        }
    });



});
