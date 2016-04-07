var album = angular.module('album', [
  'albumControllers',
  'ui.router',
  'albumServices',
  'angular-loading-bar'

  ]);
album.config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.parentSelector = '#loading-bar-container';
    cfpLoadingBarProvider.spinnerTemplate = '<div><span class="fa fa-spinner">This is Only for u ...</div>';
    cfpLoadingBarProvider.includeSpinner = true;
     }])

album.config(function($stateProvider,$urlRouterProvider,$httpProvider,$sceProvider) {

	  $sceProvider.enabled(false);
  
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/404");

  var randomString =  function (len, an){
    an = an&&an.toLowerCase();
    var str="", i=0, min=an=="a"?10:0, max=an=="n"?10:62;
    for(;i++<len;){
      var r = Math.random()*(max-min)+min <<0;
      str += String.fromCharCode(r+=r>9?r<36?55:61:48);
    }
    return str;
  }

  var random_str = randomString(3);
  
  $stateProvider


    .state('index',{
      url:"/",
      cache: false,
      resolve: {
          
        listImg: function(Listpics){

              var randomString =  function (len, an){
                an = an&&an.toLowerCase();
                var str="", i=0, min=an=="a"?10:0, max=an=="n"?10:62;
                for(;i++<len;){
                  var r = Math.random()*(max-min)+min <<0;
                  str += String.fromCharCode(r+=r>9?r<36?55:61:48);
                }
                return str;
            }
            var random = randomString(3);

          return Listpics.query()
        } 
      },
      controller:'baseCtrl',
      templateUrl:'static/dashboard/partials/base.html?'+random_str
    })
});