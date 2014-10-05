'use strict';

var eveApp = angular.module('eveApp', [])
    .controller('LoginController', function($scope) {
        $scope.validate = function(user) {
            console.log(user);
        }
    })
    .directive('loginform', function() {
        console.log("directing");
        return {
            restrict: 'E',
            templateUrl: 'partials/login-form.html'
        }
    });
