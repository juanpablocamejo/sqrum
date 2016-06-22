var app = angular.module('app', [], function($httpProvider) {
  // Use x-www-form-urlencoded Content-Type
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
});

function MainCtrl($scope, $http) {
$scope.newUS = {rol_id:1, prioridad:1};
$scope.us = [];
$scope.roles=[];
$http.get('/api/user_story/').success(function(data){
            $scope.us = data;
            console.log(data)
        }).error(function(data) {
            console.log('Error: ' + data);
        });
$http.get('/api/rol/').success(function(data){
        console.log({roles:data});
        $scope.roles = data;
    }).error(function(data) {
            console.log('Error: ' + data);
        });

function $$Post(url,dto){
    var req = { method: 'POST', url: url, data: dto, headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    transformRequest: function(obj) {
      var str = [];
      for(var p in obj)
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
      return str.join("&");
    } };
    
    return $http(req);
}

$scope.CrearUS = function() {
    var dto = {
        rol_id: $scope.usRolId,
        estado_id: 1,
        quiero: $scope.usQuiero,
        para: $scope.usPara,
        estimacion: $scope.usEstimacion,
        prioridad: $scope.usPrioridad,
        obs: $scope.usObs
    };
    $$Post('/api/user_story/', dto).success(
        function() {
            console.log('POST OK');
        }).error(function(data) {
        console.log('Error: ' + data);
    });
};
}



app.controller('MainCtrl', MainCtrl);



