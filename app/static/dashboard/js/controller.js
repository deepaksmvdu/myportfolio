var albumControllers = angular.module('albumControllers',[])

albumControllers.controller('baseCtrl', ['$scope', '$rootScope', '$stateParams', '$state', '$http', '$filter', '$location','listImg',
	function (a, rootScope, stateParams, state, http, filter,location,listImg) {
	a.listimages =  listImg["response"]
	

}])