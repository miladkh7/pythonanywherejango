var app = angular.module("Varzeshyar", ["ngRoute"]);

app.factory("ShareData", function () {
    return { value: 0 }
});

app.config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when("/", {
        templateUrl: "homePage2.html"
    });
    $routeProvider.when("/home", {
        templateUrl: "homePage2.html"
    });
    $routeProvider.when("/discover", {
        templateUrl: "discoverPage.html"
    });
    $routeProvider.when("/together", {
        templateUrl: "togetherPage.html"
    });
}]);