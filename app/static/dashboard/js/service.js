'use strict';

/* Controllers */

var albumServices = angular.module('albumServices',['ngResource'])

	/*var baseUrl = 'http://54.218.19.56:8071'*/


albumServices.factory('Listpics',function($http, $log, $q){
	 
	return { query: function(){

			var url = '/PicsList';			
			var deferred = $q.defer();

			 $http.get(url)
				.success(function(data) {

					deferred.resolve({
						response: data});
				}).error(function(msg, code) {
		          deferred.reject(msg);
		          $log.error(msg, code);
		       });

			return deferred.promise; 	
		}
	}
});
