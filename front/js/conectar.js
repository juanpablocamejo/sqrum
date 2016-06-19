var app = angular.module('app', []);

function MainCtrl($scope, $http) {

$scope.us = [];
$http.get('/api/user_story/').success(function(data){
            $scope.us = data;
            console.log(data)
        }).error(function(data) {
            console.log('Error: ' + data);
        });
}

app.controller('MainCtrl', MainCtrl);



