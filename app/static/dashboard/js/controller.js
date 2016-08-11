var albumControllers = angular.module('albumControllers',[])

albumControllers.controller('baseCtrl', ['$scope', '$rootScope', '$stateParams', '$state', '$http', '$filter', '$location','trendsData','$interval',
	function (a, rootScope, stateParams, state, http, filter,location,trendsData,$interval) {
		a.value = ''
	     a.getseatchresult = function(params) {
              a.value = params
               trendsData.query(params).then(function (get_list) {
                a.tweets = get_list['response']['data']
           },function (error){
                   console.log("error")
            });
        }
    var intervalPromise = $interval(function () { 
           
          trendsData.query(a.value).then(function (get_list) {
                a.tweets = get_list['response']['data']
           },function (error){
                   console.log("error")
            });
           

     }, 50000);      
	

}])