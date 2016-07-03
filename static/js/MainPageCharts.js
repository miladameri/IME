
function initChartHajm(data1, data2) {
    var data = data1;
    var data2 = data2;
    var canvas = document.getElementById("Hajm");
    var ctx = document.getElementById("Hajm").getContext("2d");
    var mine = new Chart(ctx).Pie(data, {
        responsive: true,
        scaleShowLabels: true,
        scaleLabel: "<%=label%>",
        scaleFontSize: 120,
        legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"><%if(segments[i].label){%><%=segments[i].label%><%}%></span></li><%}%></ul>"

    });
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "extra content");
    newDiv.innerHTML = mine.generateLegend();
    canvas.parentNode.parentNode.appendChild(newDiv);
    //console.log(canvas.parentNode.nextSibling);
    //canvas.parentNode.nextSibling.nodeValue = mine.generateLegend();
    ////console.log(canvas.closest('.extra'));
    ////canvas.closest('.extra').html(mine.generateLegend());
    console.log(mine.generateLegend());
    //ctx = document.getElementById("Arzesh").getContext("2d");
    //new Chart(ctx).Pie(data2, {
    //    percentageInnerCutout : 50,
    //    responsive: true
    //});
    //console.log($("#sel1").val());
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

    //$.ajax({
    //    url: "/maingroup",
    //    dataType: "json",
    //    data: {
    //        "time_slot": 12,
    //        "type": "value_KRials",
    //        "end_date": "1392/08/26"
    //    },
    //    type: "GET",
    //    success: function (response) {
    //        datas = response['data']
    //        for (var i = 0; i < datas[0].length; i++) {
    //            data2.push(
    //                {
    //                    value: datas[1][i],
    //                    color: colors[i],
    //                    label: datas[0][i]
    //                }
    //            );
    //        }
    //        initChartHajm(data1, data2);
    //
    //    },
    //    complete: function () {
    //    },
    //    error: function (xhr, textStatus, thrownError) {
    //        alert("error doing something");
    //    }
    //});
}
