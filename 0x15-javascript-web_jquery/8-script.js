$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function (data) {
    $.each(data.results, function (index, result) {
      $('UL#list_movies').append('<li>' + result.title + '</li>');
    });
  });
});
