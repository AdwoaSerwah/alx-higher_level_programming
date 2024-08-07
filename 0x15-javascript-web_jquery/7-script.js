$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(url, function (result) {
    $('DIV#character').text(result.name);
  });
});
