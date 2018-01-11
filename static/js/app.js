var app = angular.module('venus-app', ["highcharts-ng"]);
app.controller('indexCtrl', function($scope, $http) {
    $scope.chart_show = false;
    $scope.name = "平安银行"; // 默认000001平安银行
    $scope.chartConfig = {};
    // 执行搜索分析
    $scope.search = function() {

        // 获取基本信息
        $http({
            method: "GET",
            url: "/data/base/" + $scope.code
        }).then(function successCallback(response) {
            var data = response.data;
            $scope.name = data.name;
        }, function errorCallback(response) {
            console.log(response);
        });

        // 获取K线图数据
        $http({
            method: "GET",
            url: "/kchart/code/" + $scope.code
        }).then(function successCallback(response) {
            $scope.chart_show = true;
            var data = response.data;
            $scope.chartConfig = {
                chartType: "stock",
                chart: {
                    // type: 'map',
                    height: 1024,
                    width: 1024
                },
                rangeSelector: {
                    selected: 2
                },
                title: {
                    text: $scope.name + "历史股价"
                },
                plotOptions: {
                    series: {
                        showInLegend: true
                    }
                },
                tooltip: {
                    split: false,
                    shared: true
                },
                series: [{
                    // type: 'line',
                    id: $scope.code,
                    name: $scope.name,
                    data: data
                }]
            };
        }, function errorCallback(response) {
            // 请求失败执行代码
            console.log(response);
        });
    };
});
