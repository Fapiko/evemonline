angular.module('CacheModule', ['LocalStorageModule'])
    .provider('cacheService', function() {
        this.$get = ['localStorageService', function (localStorageService) {
            function getTimeInSeconds(offset) {
                if (offset == undefined) {
                    offset = 0;
                }

                offset = offset * 1000;

                return Math.floor((new Date().getTime() + offset) / 1000);
            }

            function calculateKey(key) {
                if (typeof key == 'object') {
                    var hashObject = new jsSHA(JSON.stringify(key), "ASCII");
                    key = hashObject.getHash("SHA-1", "HEX");
                }

                return key;
            }

            function set(key, value, timeout) {
                key = calculateKey(key);

                if (timeout == undefined) {
                    timeout = 60;
                }

                var cacheObject = {
                    timeout: getTimeInSeconds(timeout),
                    value: value
                }

                localStorageService.set(key, cacheObject);
            }

            function get(key) {
                key = calculateKey(key);

                var cacheObject = localStorageService.get(key);

                if (cacheObject == null) {
                    return false;
                }

                if (new Date().getTime() / 1000 > cacheObject.timeout) {
                    localStorageService.remove(key);
                    return false;
                }

                return cacheObject.value;
            }

            function clear(key) {
                key = calculateKey(key);

                localStorageService.remove(key);
            }

            return {
                set: set,
                get: get,
                clear: clear,
                clearAll: localStorageService.clearAll,
                cookie: localStorageService.cookie
            }
        }];
    });