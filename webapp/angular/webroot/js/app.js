'use strict';

var eveApp = angular.module('eveApp', ['ngRoute', 'CacheModule'])
    .service('userService', ['cacheService', '$q', '$http', function(cacheService, $q, $http) {
        var getToken = function() {
            var token = cacheService.get('token');
            return token;
        }

        var setToken = function(token) {
            cacheService.set('token', token, 60 * 60 * 24 * 7);
        }

        var getUser = function(token) {
            var deferred = $q.defer();

            $http.get('http://localhost:5000/user?token=' + token).success(function(data) {
                deferred.resolve(data);
            });

            return deferred.promise;
        }

        return {
            getToken: getToken,
            setToken: setToken,
            getUser: getUser
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
        return {
            restrict: 'E',
            templateUrl: 'partials/login-form.html'
        }
    })
    .directive('loginnavpartial', ['$rootScope', 'userService', function($rootScope, userService) {
        var token = userService.getToken();
        var templateUrl;

        if (!token) {
            templateUrl = 'partials/login-nav-partial-anonymous.html';
        } else {
            templateUrl = 'partials/login-nav-partial-authenticated.html';
        }

        userService.getUser(token).then(function(user) {
            $rootScope.user = user;
        });

        return {
            restrict: 'E',
            templateUrl: templateUrl
        }
    }]);

