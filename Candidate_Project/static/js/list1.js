var list1 = angular.module('list1', []);

// have to configure angular to use {a a} bracket notation to avoid conflicts with Jinja engine
app.config(['$interpolateProvider', function(interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.startSymbol('a}');
}]);

list1.controller('listCtrl', function($scope) {

  $scope.music = [
    {artist: "Bowling for Soup", song: "1985", album: "A Hangover You Don't Deserve", year: "2004", favorite: false, edit: false },
    {artist: "Periphery", song: "Muramasa", album: "Periphery II: This Time It's Personal", year: "2012", favorite: true, edit: false},
    {artist: "Soundgarden", song: "Black Hole Sun", album: "Superunknown", year: "1994", favorite: false, edit: false }
  ];

  // Receives the new item entered in the input box and puts
  // it on the end of the array
  $scope.addEntry = function(newEntry) {

    // Check that the input box has a value
    if(!(newEntry === undefined || newEntry === "")){
      $scope.music.push({
        artist: newEntry.artist, song: newEntry.song, album: newEntry.album, year: newEntry.year, favorite: newEntry.favorite, edit: false
      });
      $scope.missingNewItemError = "";
    } else {

      // Show an error if no item was entered
      $scope.missingNewItemError = "Please Enter an Entry";
    }
  };

  $scope.deleteEntry = function(entry) {
    $scope.music.splice( $scope.music.indexOf(entry), 1 );
  }

});
