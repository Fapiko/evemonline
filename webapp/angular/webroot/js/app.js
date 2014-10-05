'use strict';

var eveApp = angular.module('eveApp', ['ngRoute', 'CacheModule'])
    .service('userService', ['cacheService', function(cacheService) {
        var getToken = function() {
            var token = cacheService.get('token');
            return token;
        }

        var setToken = function(token) {
            cacheService.set('token', data.token, 60 * 60 * 24 * 7);
        }

        return {
            getToken: getToken,
            setToken: setToken
        }
    }])
    .controller('LoginController',
        ['$scope', '$http', '$rootScope', 'userService', function($scope, $http, $rootScope, userService) {
        // Login validation
        $scope.validate = function(user) {
            $http.post('http://localhost:5000/session/create', user).success(function(data) {
                if (data.error) {
                    console.log(data.error);
                } else {
                    userService.setToken(data.token);
                }
            });
        }
    }])
    .directive('loginform', function() {
        console.log("directing");
        return {
            restrict: 'E',
            templateUrl: 'partials/login-form.html'
        }
    })
    .directive('loginnavpartial', ['$rootScope', 'userService', function($rootScope, userService) {
        var token = userService.getToken();
        console.log(token);

        var templateUrl;
        if (!token) {
            templateUrl = 'partials/login-nav-partial-anonymous.html';
        } else {
            templateUrl = 'partials/login-nav-partial-authenticated.html';
        }

        return {
            restrict: 'E',
            templateUrl: templateUrl
        }
    }]);

